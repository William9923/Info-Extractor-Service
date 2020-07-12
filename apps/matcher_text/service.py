import time

from apps.utils.model.service import *
from apps.utils.config import generate_random_seperator

class TextService(Service):
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

        # metadata
        self.seperator = generate_random_seperator()

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
            self.word_count += len(row)
            self.total_sentences += 1
            contains = False
            
            processed_row = []

            for word in row:
                self.algo.text = word
                indexes = self.algo.find()

                new_word = word

                if len(indexes) > 0:
                    contains = True
                    self.sentences += 1
                    for i in range(len(indexes)):
                        self.keyword_detected += 1
                        new_word = new_word[:i + indexes[i]] + self.seperator + new_word[i+indexes[i]:]

                processed_row.append(new_word)

            if contains:
                list_of_answer.append("".join(processed_row))

        self.time = time.time() - t

        data = {
            "stats" : self.get_stats(),
            "answer" : list_of_answer,
            "metadata" : {
                "seperator" : self.seperator,
            } 
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
