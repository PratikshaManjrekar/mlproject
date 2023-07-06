'Creating own custom exception'
import sys
import logging

def error_message_details(error, error_detail:sys):
    'error_detail will be present inside sys module'
    _,_,exc_tb=error_detail.exc_info()
    'exc_tb - Will give all info about the exception like in which file, on which line exception occured'
    
    file_name=exc_tb.tb_frame.f_code.co_filename   #To get a file name
    error_message="Error occured in pyhton script name [{0}] line number [{1}] error message [{2}]".format(
         file_name,exc_tb.tb_lineno,str(error))
    return error_message  

'Whenever error raises we need to call the error function so for that create a class'
class CustomException(Exception):        #Inheriting a parent 'Exception'
    def __init__(self, error_message, error_detail:sys):   #Constructor
        super().__init__(error_message)     # Inheriting __init__ function from exception
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):     # For printing error message
        return self.error_message
     