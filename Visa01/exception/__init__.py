import sys 

class CustomException(Exception) :

    def __init__(self, error_message: Exception, error_details: sys) :
        super().__init__(error_message)
        self.error_message = CustomException.get_detailed_error_message(error_message = error_message, 
                                                                        error_details = error_details)

    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_details: sys) -> str :

        _, _, exc_tb = error_details.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        try_block_line_number = exc_tb.tb_lineno
        except_block_line_number = exc_tb.tb_frame.f_lineno

        error_message = f'''
        Error occured in script : [{file_name}] 
        in try block line number : [{try_block_line_number}] & 
        in exception block line number : [{except_block_line_number}] 
        Error Message : [{error_message}]
        '''

        return error_message
    
    def __str__(self) :
        return self.error_message
    
    def __repr__(self) -> str:
        return CustomException.__name__.str()