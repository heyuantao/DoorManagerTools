#-*- coding=utf-8 -*-
import os
from utils import Singleton
import logging

logger = logging.getLogger(__name__)

class RedisConfigSettings:
    #HOST = "172.16.5.42"
    HOST = "127.0.0.1"
    MAX_RECORD_SIZE = 1000 #保存在redis中的最大记录长度

class AppConfigSettings:
    ROUTE_PREFIX = "" # 为路由的前缀，如果与其他网站共享一个ip且通过nginx反向代理转发时使用，默认为空。样式为 "/site_url_prefix" or ""
    SITE_URL = "http://127.0.0.1:5000"
    STATIC_FOLDER = "./templates"  # not end with slash
    STATIC_URL = "/api/static/"                              # /api/static this is use for css and js file
    TEMPLATE_FOLDER = "./templates"  # not end with slash
    AUTH_TOKEN = [os.getenv('TOKEN',default="123456"),]  #可以设置多个token,可以设置并修改
    #CELERY_BACKEND = "redis://127.0.0.1:6379/1"
    #接口中文字符的设置
    JSON_AS_ASCII = False
    JSONIFY_MIMETYPE= "application/json;charset=utf-8"
    #调试模式
    DEBUG = False

@Singleton
class Config:
    AppConfig = AppConfigSettings()
    DBConfig = RedisConfigSettings()
    def __init__(self):
        pass
        #self.AppConfig.config['JSON_AS_ASCII'] = False
        #self.AppConfig.config['DEBUG'] = False

config = Config()
