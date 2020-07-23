from flask import Blueprint, render_template, abort, request, jsonify, current_app
import logging 

from apps.utils.config import generate_prefix_key

from apps.matcher_scraper.service import ScrapperService
from apps.utils.model.algorithm import AlgorithmFactory
from apps.utils.model.validation import ScrapperForm

LOG = logging.getLogger(__name__)
scraper =  Blueprint('scraper', __name__, url_prefix=generate_prefix_key() + "/scraper")

@scraper.route('/', methods=['POST', 'GET'])
def scraper_service():
    LOG.info("Scrapper Service Called")
    form = ScrapperForm(request.form)
    if request.method == "POST" :
        if form.validate():
            factory = AlgorithmFactory()
            try :
                algo = factory.getAlgo(request.form["algo"])
            except ValueError :
                LOG.error("Failed to parse algorithm. Using default algorith : regex")
                algo = factory.getAlgo("regex")

            service = ScrapperService(algo)

            LOG.info("Injecting service data")
            service.data = {
                'keyword' : request.form.get('keyword'),
                'url' : request.form.get('url'),
            }

            LOG.info("Executing Scrapper service")
            return service.do()
        else :

            LOG.warning("Data Form not filled correctly. Beware of malicious attemps!!")
            return jsonify({
                "error" : "Prerequiste data not filled correctly"
            })


    return jsonify({
        "message" : "Welcome to Scrapper Matcher Service"
    })