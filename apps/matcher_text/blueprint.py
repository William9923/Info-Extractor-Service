from flask import Blueprint, render_template, abort, request, jsonify
import logging

from apps.utils.config import generate_prefix_key

from apps.matcher_text.service import TextService
from apps.utils.model.algorithm import AlgorithmFactory
from apps.utils.model.validation import TextForm

LOG = logging.getLogger(__name__)
text =  Blueprint('text', __name__, url_prefix= generate_prefix_key() + "/text")

@text.route('/', methods=['GET'])
def text_service():

    LOG.info("Text Service Called")
    factory = AlgorithmFactory()
    try :
        algo = factory.getAlgo(request.args.get("algo"))
    except Exception :
        LOG.error("Failed to parse algorithm. Using default algorith : regex")
        algo = factory.getAlgo("regex") # default algorithm

    service = TextService(algo)

    keyword = request.args['keyword']
    content = request.args['content']

    LOG.info("Injecting service data")
    service.data = {
        'keyword' : keyword,
        'content' : content,
    }

    LOG.info("Executing Text service")
    return service.do()
