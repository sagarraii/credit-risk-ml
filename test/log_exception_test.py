import sys
import os

# Add project root to path to enable imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.exception import CustomException
from src.logger import get_logger

logger = get_logger(__name__)


def divide_numbers():
    try:
        logger.info("Starting division operation")
        result = 10 / 0
        logger.info("Division successful")
        return result

    except Exception as e:
        logger.error("Error occurred during division")
        raise CustomException(e, sys)


if __name__ == "__main__":
    divide_numbers()
