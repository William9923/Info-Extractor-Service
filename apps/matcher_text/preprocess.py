from flask import request, Markup
from copy import copy

from apps.utils.model.preprocess import *

class TextPreprocessor():
    def preprocess(self, request):
        data = {}
        data["keyword"] = request["keyword"].lower()
        text = request["content"]

        if text[-1] != '.' or text[-1] != '!' or text[-1] != '?':
            text += '.'
        text = text.strip()
        text = '. '.join(text.splitlines())
        text = text.split('. ')
        text_processed = copy(text)
        for i in range(len(text)):
            text_processed[i] = Markup(text[i].strip().lower().replace('\n','')).striptags()
        data['content'] = text_processed
        return data
            

            
