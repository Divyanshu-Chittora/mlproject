import sys

def error_message_detail(error,error_details:sys):
    _,_,exc_tb=error_detail.exc.info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error accured in python script name [{0}] line number[{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )

class CustomException(Exception):
    def __init__(self,error_message,error_dettail:sys):
        super,__init_(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message