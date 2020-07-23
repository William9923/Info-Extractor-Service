class ProcessException(Exception):
    status_code = 500

    def __init__(self, message, state, status_code = None, payload=None):
        Exception.__init__(self)
        self.message = message 
        if status_code is not None:
            self.status_code = status_code
        self.state = state
        self.payload = payload 

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message 
        rv['state'] = self.state
        return rv

class PreprocessingException(ProcessException):
    
    def __init__(self, message, status_code=None, payload=None):
        super().__init__(message, "Preprocess", status_code=status_code, payload=payload)

class OutputException(ProcessException):
    def __init__(self, message, status_code=None, payload=None):
        super().__init__(message, "Output", status_code=status_code, payload=payload)

class ServiceException(ProcessException):
    def __init__(self, message, status_code=None, payload=None):
        super().__init__(message, "Service", status_code=status_code, payload=payload)
