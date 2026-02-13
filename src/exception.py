import sys
import traceback


class CustomException(Exception):
    """
    Generic custom exception class for ML projects.
    Captures detailed error message including:
    - File name
    - Line number
    - Original error message
    """

    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)

        self.error_message = self.get_detailed_error_message(
            error_message=error_message,
            error_detail=error_detail
        )

    @staticmethod
    def get_detailed_error_message(error_message: str, error_detail: sys) -> str:
        """
        Extracts detailed traceback information.
        """
        _, _, exc_tb = error_detail.exc_info()

        if exc_tb is None:
            return error_message

        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        detailed_message = (
            f"\nError occurred in script: [{file_name}] "
            f"at line number: [{line_number}] "
            f"with message: [{error_message}]"
        )

        return detailed_message

    def __str__(self):
        return self.error_message
