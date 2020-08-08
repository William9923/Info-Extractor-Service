from flask import Blueprint, render_template, abort, request, jsonify, current_app
import logging 

from apps.utils.config import generate_prefix_key

from apps.matcher_scraper.service import ScrapperService
from apps.utils.model.algorithm import AlgorithmFactory
from apps.utils.model.validation import ScrapperForm

LOG = logging.getLogger(__name__)
scraper =  Blueprint('scraper', __name__, url_prefix=generate_prefix_key() + "/scraper")

@scraper.route('/', methods=['GET'])
def scraper_service():
    LOG.info("Scrapper Service Called")
    
    factory = AlgorithmFactory()
    try :
        algo = factory.getAlgo(request.args.get("algo"))
    except ValueError :
        LOG.error("Failed to parse algorithm. Using default algorith : regex")
        algo = factory.getAlgo("regex")

    keyword = request.args['keyword'];
    url = request.args['url']

    service = ScrapperService(algo)

    LOG.info("Injecting service data")
    service.data = {
        'keyword' : keyword,
        'url' : url,
    }

    LOG.info("Executing Scrapper service")
    return service.do()
