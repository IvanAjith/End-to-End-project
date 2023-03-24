
## Step 1 : Import sys
import sys

## Step2 : Define error_message_detail function
def error_message_details(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()                       #This gives 3 parameters and the 3rd one is important
    file_name = exc_tb.tb_frame.f_code.co_filename             #Use this format to fetch the filename from the error
    error_message = "Error occured in [{0}], line number [{1}] with error message [{2}]".format(
    file_name, exc_tb.tb_lineno, str(error))
    return error_message


## Step3 : Define CustomException class and inherit the error_message_detail function using super() function
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message


