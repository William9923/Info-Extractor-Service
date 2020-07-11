import time

from apps.utils.model.service import *

class TextService():
    def __init__ (self, algo, preprocessor, outputter):
        self.preprocessor = preprocessor
        self.outputer = outputter
        self.algo = algo

        # base stats service
        self.word_count = 0
        self.keyword_detected = 0
        self.sentences = 0
        self.total_sentences = 0
        self.time = None

    @property
    def data(self):
        return self._data
    
    @data.setter 
    def data(self, value):
        self._data = value

    def do(self):
        t = time.time()

        formatted_data = self.preprocessor.preprocess(self.data)
        self.algo.pattern = formatted_data.get('keyword')
        
        list_of_answer = []
        for row in formatted_data.get('content'):
            self.algo.text = row
            self.word_count += len(row.split(' '))  
            self.total_sentences += 1
            indexes = self.algo.find()

            if (len(indexes) > 0):
                self.sentences += 1
                for index in indexes:
                    self.keyword_detected+=1
                list_of_answer.append(row)

        self.time = time.time() - t

        data = {
            "stats" : self.get_stats(),
            "answer" : list_of_answer,
        }

        return self.outputer.output(data)

    def get_stats(self):
        return {
            "word" : self.word_count,
            "keyword" : self.keyword_detected,
            "sentences" : self.sentences,
            "total_sentences" : self.total_sentences,
            "time" : self.time, 
        }
