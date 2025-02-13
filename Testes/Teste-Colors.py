import logging
from termcolor import colored
from time import time

# Defina a variável ENV_FILE (substitua pelo valor apropriado)
ENV_FILE = "config.env"

# Define um formato de log com cores e outros parâmetros de formatação
class ColoredFormatter(logging.Formatter):
    def format(self, record):
        log_colors = {
            'DEBUG': ['blue', 'dark'],
            'INFO': ['green'],
            'WARNING': ['yellow'],
            'ERROR': ['red'],
            'CRITICAL': ['red', 'on_white']
        }
        log_attrs = {
            'CRITICAL': ['bold']
        }
        log_color = log_colors.get(record.levelname, ['white'])
        attrs = log_attrs.get(record.levelname, [])
        record.msg = colored(record.msg, *log_color, attrs=attrs)
        return super().format(record)

# Configuração do logger para main.py
main_logger = logging.getLogger("MainLogger")
main_logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setFormatter(ColoredFormatter(
    '%(asctime)s - %(levelname)s - %(message)s'))
main_logger.addHandler(console_handler)

starting_time = time()
main_logger.info(f'{ENV_FILE}')
main_logger.info('\n*************** INITIATING ROUTINE(s) ***************\n')

# Exemplos de logs coloridos
main_logger.debug('Esta é uma mensagem de debug.')
main_logger.info('Esta é uma mensagem de informação.')
main_logger.warning('Este é um aviso!')
main_logger.error('Este é um erro.')
main_logger.critical('Mensagem crítica!')
