#-*- coding=utf-8 -*-
from flask import Flask
from flask_cors import CORS
from werkzeug.serving import WSGIRequestHandler
from config import config
import logging

#from task import init_db_by_upload_files

logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__,static_folder=config.AppConfig.STATIC_FOLDER, template_folder=config.AppConfig.TEMPLATE_FOLDER)
    app.config.from_object(config)
    print(app.config)
    CORS(app)
    #app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RR'

    from routers import DoorManagerRouter
    route_instance = DoorManagerRouter()
    route_instance.init_app(app)

    # 从gunicorn获得loglevel等级，并将其设置到app中
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    return app

#WSGIRequestHandler.protocol_version = "HTTP/1.1"
application = create_app()

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)
    application.run(port=5001,host="0.0.0.0")