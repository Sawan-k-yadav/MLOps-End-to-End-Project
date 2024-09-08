import sys

class customException(Exception):
                                     # Defining type variable as sys   
    def __init__(self, error_message, error_details:sys):
        self.error_message=error_message

    #from sys exc_info only third value is important here to get the details of error in execution trace back
        _,_,exc_tb=error_details.exc_info()   # --> Execution info

        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in the python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message)
        )
    


if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        # print(e)
        raise customException(e, sys)  # Instead of just sending error message 
                                        # we can check files and details of error.
