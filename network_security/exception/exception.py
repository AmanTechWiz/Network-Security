import sys 
from network_security.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message:Exception, error_detail:sys):
       self.error_message = error_message
       _,_,exc_tb = error_detail.exc_info()
       self.lineno = exc_tb.tb_lineno
       self.file_name=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in file {0} at line number {1} and error message is {2}".format(self.file_name,self.lineno,str(self.error_message))

if __name__ == '__main__':
    try:
        logger.logging.info("Enter the try block !")
        a=1/0
        print("This won't print",a)
    except Exception as e:
        raise NetworkSecurityException(e,sys)        
