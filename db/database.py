#-*- coding=utf-8 -*-
#from .redis import AppRedisClient
from utils import Singleton,AppException
from uuid import uuid4
from datetime import datetime,timedelta
from config import config
import redis
import logging
import json

from utils.AppException import MessageException

logger = logging.getLogger(__name__)

#使用redis来存放各类数据
@Singleton
class Database:
    def __init__(self, host=config.DBConfig.HOST, port=6379 , db=0): #'172.16.5.42'
        self.host = host
        self.port = port
        self.db = db

        ####定义redis的相关前缀###########
        self.open_success_list_key = "success:"
        self.open_failure_list_key = "failure:"
        self.max_list_size = config.DBConfig.MAX_RECORD_SIZE

        try:
            logger.debug("Connect to redis ... in Database.__init__()")
            self.connection_pool = redis.ConnectionPool(host=self.host, port=self.port, db=self.db, decode_responses=True) #password
            self.connection = redis.StrictRedis(connection_pool=self.connection_pool)
        except Exception as e:
            msg_str = "Error in conncetion redis ! in Database.__init__()"
            logger.error(msg_str)
            raise MessageException(msg_str)

    #flask 初始化调用该函数
    def init_app(self,app=None):
        logger.debug("Init database in Database.__init__()")

    #将一个开门成功记录存放在数据库中
    def add_success_open_record(self,record):
        list_key = self.open_success_list_key
        self._trim_list_size()
        return self.connection.lpush(list_key,json.dumps(record))

    # 将一个开门失败记录存放在数据库中
    def add_failure_open_record(self, record):
        list_key = self.open_failure_list_key
        self._trim_list_size()
        return self.connection.lpush(list_key, json.dumps(record))

    #控制数据库的长度
    def _trim_list_size(self):
        success_list_key = self.open_success_list_key
        failure_list_key = self.open_failure_list_key
        self.connection.ltrim(success_list_key,0,self.max_list_size)
        self.connection.ltrim(failure_list_key, 0, self.max_list_size)

    def get_all_success_record(self):
        list_key = self.open_success_list_key
        item_list = self.connection.lrange(list_key,0,self.max_list_size)
        dict_list = []
        for item  in item_list:
            dict_item = json.loads(item)
            dict_item = json.loads(dict_item)
            dict_list.append(dict_item)
        return dict_list


    def get_all_failure_record(self):
        list_key = self.open_failure_list_key
        item_list = self.connection.lrange(list_key, 0, self.max_list_size)
        dict_list = []
        for item in item_list:
            dict_item = json.loads(item)
            dict_item = json.loads(dict_item)
            dict_list.append(dict_item)
        return dict_list