import os
import sys
from pathlib import Path

from aiogram import Bot, Dispatcher, executor, types
from loguru import logger

import handlers
from settings import load as load_settings


def get_basedir() -> Path:
    return Path(os.path.abspath(__file__)).parent


def set_logger():
    name_file_log: Path = get_basedir().joinpath(r'log\debug.log')
    logger.add(
        sink=name_file_log,
        encoding='utf-8',
        format='{time}-{level}-{line}:{message}',
        filter=lambda x: '[MES]' not in x['message'],
        level='DEBUG',
        rotation='1 day',
        compression='zip'
    )


def create_bot(settings: dict) -> Dispatcher:
    bot = Bot(token=settings['API_TOKEN'])
    return Dispatcher(bot)


def polling_bot(dp: Dispatcher) -> None:
    executor.start_polling(dp, skip_updates=True)


def get_settings() -> dict:
    settings = load_settings(handler='c')
    if not settings:
        logger.error('Settings empty')
        sys.exit()
    return settings
