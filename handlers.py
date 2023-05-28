from pathlib import Path

from loguru import logger

from server import get_basedir

name_file_log: Path = get_basedir().joinpath(r'log\message.log')
logger.add(
    sink=name_file_log,
    encoding='utf-8',
    format='{time}-{level}-{line}:{message}',
    filter=lambda x: '[MES]' in x['message'],
    level='DEBUG',
    rotation='10 MB',
    compression='zip'
)


def mes_welcome(message):
    mes = message['from']['first_name']
    logger.debug('[MES]' + mes)
    return 'Privet {}'.format(mes)
