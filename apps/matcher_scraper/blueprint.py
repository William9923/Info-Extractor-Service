from flask import Blueprint, render_template, abort, request, jsonify

from apps.utils.config import generate_prefix_key

from apps.matcher_scraper.service import *
from apps.utils.model.algorithm import *
from apps.utils.model.preprocess import *
from apps.utils.model.output import *
from apps.utils.model.validation import *

scraper =  Blueprint('scraper', __name__, url_prefix=generate_prefix_key() + "/scraper")

@scraper.route('/', methods=['POST', 'GET'])
def scraper_service():
    form = ScrapperForm(request.form)
    if request.method == "POST" :
        if form.validate():
            factory = AlgorithmFactory()
            try :
                algo = factory.getAlgo(request.form["algo"])
            except ValueError :
                # log information
                algo = factory.getAlgo("regex")


            # inject the dependencies into the service
            service = ScrapperService(algo)

            # inject data needed
            service.data = {
                'keyword' : request.form.get('keyword'),
                'url' : request.form.get('url'),
            }

            # exec the service
            return service.do()
        else :
            return jsonify({
                "error" : "Prerequiste data not filled correctly"
            })


    return jsonify({
        "message" : "Welcome to Scrapper Matcher Service"
    })