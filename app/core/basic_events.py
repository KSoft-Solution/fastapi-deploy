from typing import Callable

from fastapi import FastAPI
from loguru import logger

from app.core.db_events import (
    close_mongo_connection, connect_to_mongo
)

def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def start_app() -> None:
        await connect_to_mongo(app)
    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    @logger.catch
    def stop_app() -> None:
        close_mongo_connection(app)
    return stop_app
