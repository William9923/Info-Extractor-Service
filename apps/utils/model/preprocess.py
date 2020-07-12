from abc import ABCMeta, abstractmethod
from copy import copy
from nltk.tokenize import word_tokenize , sent_tokenize 
from flask import Markup

class Preprocessor(object):
    @abstractmethod
    def preprocess(self, request):
        pass

class TextPreprocessor(Preprocessor):
    def preprocess(self, request):
        data = {}
        data["keyword"] = request["keyword"].lower()
        text = sent_tokenize(request["content"])
 
        text_processed = copy(text)

        for i in range(len(text)):
            text_processed[i] = Markup(text[i].strip().lower().replace('\n','')).striptags()

        word_tokenized = []
        for row in text_processed:
            word_tokenized.append(word_tokenize(row))

        data['content'] = word_tokenized
        return data