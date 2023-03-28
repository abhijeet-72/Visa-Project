import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

while True:
    project_name = input("Please enter the Project Name : ")

    if project_name != '' :
        break

logging.info(f'Created project as : {project_name}')

file_path_list = [
    f'.github/workflows/.gitkeep',
    f'.github/workflows/main.yaml',
    f'{project_name}/__init__.py',
    f'{project_name}/components/__init__.py',
    f'{project_name}/configuration/__init__.py',
    f'{project_name}/constant/__init__.py',
    f'{project_name}/entity/__init__.py',
    f'{project_name}/exception/__init__.py',
    f'{project_name}/logger/__init__.py',
    f'{project_name}/pipeline/__init__.py',
    f'{project_name}/utils/__init__.py',
    f'config/config.yaml',
    'main.py',
    'README.md',
    'requirements.txt',
    'schema.yaml',
    'setup.py'
]

for file_path in file_path_list :
    paths = Path(file_path)
    filedir, filename = os.path.split(paths)

    if filedir != '' :
        os.makedirs(filedir, exist_ok = True)
        logging.info(f'Creating the file directory {filedir} at {paths}')

    if (not os.path.exists(paths)) or (os.path.getsize(paths) == 0) :
        with open(paths, 'w') as f :
            pass
            logging.info(f'Creating the file {filename} for path {paths}')

    else :
        logging.info(f'The file {filename} already exist at {paths}...')
