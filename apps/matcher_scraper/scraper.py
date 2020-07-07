from flask import Blueprint, render_template, abort

from apps.utils.config import generate_prefix_key

scraper =  Blueprint('scraper', __name__, url_prefix=generate_prefix_key() + "/scraper")

@scraper.route('/')
def scraper_service():
    return "Scraper service test"