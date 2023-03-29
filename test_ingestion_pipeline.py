from Visa01.exception import *
from Visa01.logger import logging
from Visa01.pipeline.pipeline import Pipeline

def main() :
    
    try :
        pipeline = Pipeline()
        pipeline.run_pipeline()

    except Exception as e :
        logging.error(f'{e}')
        print(e)

if __name__ == '__main__' :
    main()