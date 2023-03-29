import os, sys, yaml
import Visa01.exception as CustomException

def write_yaml_file(file_path : str, data : dict = None) :

    '''
    Creates .yaml file
    file_path : str
    data in file : dict
    '''
    try :
        os.makedirs(os.path.dirname(file_path), exist_ok = True)
        with open(file_path, 'w') as yaml_file :
            if data is not None :
                yaml.dump(data, yaml_file)
    except Exception as e :
        raise CustomException(e, sys) from e

def read_yaml_file(file_path : str) -> dict :
    
    '''
    Reads .yaml file and returns content of file as dictionary.
    file_path : str
    '''
    try :
        with open(file_path, 'rb') as yaml_file :
            return yaml.safe_load(yaml_file)

    except Exception as e :
        raise CustomException (e, sys) from e 