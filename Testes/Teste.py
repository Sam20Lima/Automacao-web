import logging
from termcolor import colored

# Define um formato de log com cores e outros parâmetros de formatação
class ColoredFormatter(logging.Formatter):
    def format(self, record):
        log_colors = {
            'DEBUG': ['blue'],
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

# Configura o logger
logger = logging.getLogger('colored_logger')
handler = logging.StreamHandler()
formatter = ColoredFormatter('%(levelname)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# Exemplos de logs coloridos
logger.debug('Esta é uma mensagem de debug.')
logger.info('Esta é uma mensagem de informação.')
logger.warning('Este é um aviso!')
logger.error('Este é um erro.')
logger.critical('Mensagem crítica!')
