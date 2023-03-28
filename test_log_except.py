from Visa01.exception import CustomException
from Visa01.logger import logging
from flask import Flask
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def test_page():
    try:
        raise Exception('This is to test the Custom Exception.')
    
    except Exception as e:
        Visa01 = CustomException(e, sys)
        logging.info(Visa01.error_message)
        logging.info('This is to test the Logging.')

if __name__ == '__main__':
    app.run(debug = True)
