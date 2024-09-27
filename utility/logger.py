import logging

LOG_FILE = 'llm_log_file.log'
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger('llm_log_file')
