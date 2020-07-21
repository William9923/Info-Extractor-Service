from abc import ABCMeta, abstractmethod
from copy import copy
from nltk.tokenize import word_tokenize , sent_tokenize 
from flask import Markup
from typing import Dict, Any
import requests
from bs4 import BeautifulSoup

class Preprocessor(object):
    @abstractmethod
    def preprocess(self, request):
        pass

class TextPreprocessor(Preprocessor):
    def preprocess(self, request) -> Dict[str, Any]:
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

class WebPreprocessor(Preprocessor):
    def preprocess(self, request)  -> Dict[str, Any] :
        data = {}
        data["keyword"] = request["keyword"].lower()
        r = requests.get(request["url"])
        full_text = self.get_content(r)

        text = sent_tokenize(full_text)
        text_processed = copy(text)

        for i in range(len(text)):
            text_processed[i] = Markup(text[i].strip().lower().replace('\n','')).striptags()

        word_tokenized = []
        for row in text_processed:
            word_tokenized.append(word_tokenize(row))

        data['content'] = word_tokenized
        return data


    def get_content(self,r):
        soup = BeautifulSoup(r.content, 'html.parser')
        return soup.get_text()
