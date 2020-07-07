from flask import Blueprint, render_template, abort

from apps.utils.config import generate_prefix_key

text =  Blueprint('text', __name__, url_prefix= generate_prefix_key() + "/text")

@text.route('/')
def text_service():
    return "Text service test"

