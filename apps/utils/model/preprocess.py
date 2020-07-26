from abc import ABCMeta, abstractmethod
from copy import copy
from nltk.tokenize import word_tokenize , sent_tokenize 
from flask import Markup
from typing import Dict, Any
import requests
from bs4 import BeautifulSoup
import logging
from typing import List

from apps.utils.model.error import PreprocessingException

LOG = logging.getLogger(__name__)

class Preprocessor(object):
    @abstractmethod
    def preprocess(self, request):
        pass

    def tokenizing(self, text) -> List[List[str]]:
        text_processed = copy(text)
        for i in range(len(text)):
            text_processed[i] = Markup(text[i].strip().replace('\n','')).striptags()

        word_tokenized = []
        for row in text_processed:
            word_tokenized.append(word_tokenize(row))

        return word_tokenized

class TextPreprocessor(Preprocessor):
    def preprocess(self, request) -> Dict[str, Any]:
        data = {}
        data["keyword"] = request["keyword"].lower()
        text = sent_tokenize(request["content"])

        data['content'] = self.tokenizing(text)
        LOG.info(f"Content Summary : {data['content']}")
        return data

class URLPreprocessor(Preprocessor):
    def preprocess(self, request)  -> Dict[str, Any] :
        data = {}
        data["keyword"] = request["keyword"].lower()
        r =  self.make_request(request["url"])

        full_text = self.get_content(r)
        text = sent_tokenize(full_text)

        data['content'] = self.tokenizing(text)
        LOG.info(f"Content Summary : {data['content']}")
        return data

    def make_request(self, url: str) -> Any:
        r = requests.get(url)

        if not r.ok: # 4xx or 5xx
            LOG.error(f"4xx or 5xx url web scrapping detected. URL : {request['url']}")
            raise PreprocessingException(message="Scrapping Web Failed")
        
        return r

    def get_content(self,r) -> str:
        soup = BeautifulSoup(r.content, 'html.parser')
        return soup.get_text()
