from typing import Dict, Any
import logging
from apps.utils.config import generate_random_seperator
from apps.utils.model.error import ServiceException
import time

LOG = logging.getLogger(__name__)

class Service(object):
    def __init__ (self, algo, preprocessor, outputter):

        LOG.info("Initiate Process Service")

        self.preprocessor = preprocessor
        self.outputer = outputter
        self.algo = algo

        # base stats service
        self.word_count = 0
        self.keyword_detected = 0
        self.sentences = 0
        self.total_sentences = 0
        self.time = None
        self.success = False 

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
        list_of_answer = []

        LOG.info("Starting service process ...")
        try : 
            formatted_data = self.preprocessor.preprocess(self.data)
            self.algo.pattern = formatted_data.get('keyword')

            LOG.debug(formatted_data.get('content'))

            for row in formatted_data.get('content'):
                self.word_count += len(row)
                self.total_sentences += 1
                contains = False
                
                processed_row = []

                for word in row:
                    self.algo.text = word.lower()
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
                    list_of_answer.append(" ".join(processed_row))
        
            self.success = True 

        except Exception as err:    
            raise ServiceException(message="Error occured when processing data")
            LOG.error("Error happended when Creating Process. Please check the system process log!!")
            self.success = False 

        finally:
            self.time = time.time() - t

        data = {
            "stats" : self.get_stats(),
            "answer" : list_of_answer,
            "metadata" : {
                "seperator" : self.seperator,
            } 
        }

        LOG.info("Ready to output process result")
        return self.outputer.output(data)

    def get_stats(self):
        LOG.info("Creating process stats ...")
        return {
            "word" : self.word_count,
            "keyword" : self.keyword_detected,
            "sentences" : self.sentences,
            "total_sentences" : self.total_sentences,
            "time" : self.time, 
            "success" : self.success
        }

