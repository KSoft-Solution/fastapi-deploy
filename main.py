import os

import uvicorn
from fastapi import FastAPI
from loguru import logger
from fastapi.exceptions import RequestValidationError,HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.core.basic_config import DEPLOYMENT_ENV,PROJECT_NAME,DEBUG,VERSION,ALLOWED_HOSTS
from app.core.basic_events import create_start_app_handler,create_stop_app_handler
from app.errors.validation_error import http422_error_handler
from app.errors.http_error import http_error_handler
from app.routes.api import router as main_router

def get_application() -> FastAPI:
    if DEPLOYMENT_ENV == "kube":
        prefix = os.environ.get('PROXY_PREFIX', '/')
        logger.info(f"DEPLOYMENT_ENV is {DEPLOYMENT_ENV} and proxy prefix {prefix}")
        application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION, openapi_prefix=prefix)
    else:
        application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)
    application.include_router(main_router)
    
    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application
    
app = get_application()

if __name__ == '__main__':
    uvicorn.run('main:app', port=5000, reload=True)