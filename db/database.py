#-*- coding=utf-8 -*-
#from .redis import AppRedisClient
from utils import Singleton,AppException
from uuid import uuid4
from datetime import datetime,timedelta
from config import config
import redis
import logging
import json

logger = logging.getLogger(__name__)

#使用redis来存放各类数据
@Singleton
class Database:
    def __init__(self, host='127.0.0.1', port=6379 , db=0):
        self.host = host
        self.port = port
        self.db = db

    #flask 初始化调用该函数
    def init_app(self,app=None):
        logger.debug("Init database in Database.__init__()")