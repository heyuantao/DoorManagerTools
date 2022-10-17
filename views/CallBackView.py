#-*- coding=utf-8 -*-
from flask import request, jsonify, current_app, stream_with_context, Response
#from flask_api import status
from utils.Parser import DoorManagerRecordParser
import time
from werkzeug.urls import url_quote
import urllib.parse
import base64
import re
from datetime import datetime,timedelta
import traceback
from config import config
import mimetypes
import json
from db import Database
import logging

logger = logging.getLogger(__name__)
db = Database()

def dooropenevent_callback_view(request):
    parse = DoorManagerRecordParser
    data_str = request.data.decode("UTF-8")
    dict_item = json.loads(data_str)

    #print("发生开门事件在{},记录编号为{}".format(parse.time(dict_item), parse.uuid(dict_item)))
    if parse.isUser(dict_item):
        #print("教师 {} 打开了 {}".format(parse.name(dict_item), parse.location(dict_item)))
        item={"id": parse.uuid(dict_item),"name":parse.name(dict_item),"location":parse.location(dict_item),"type":"user",\
              "timestamp":parse.timestamp(dict_item),"time":str(parse.time(dict_item))}
        db.add_success_open_record(json.dumps(item))
    elif parse.isGuest(dict_item):
        #print("{} 设置的访客 {} 打开了 {}".format(parse.visitedName(dict_item),parse.name(dict_item),parse.location(dict_item)))
        item = {"id": parse.uuid(dict_item),"name": parse.name(dict_item), "location": parse.location(dict_item), "type": "guest",\
                "timestamp":parse.timestamp(dict_item),"time":str(parse.time(dict_item)),\
                "visited":parse.visitedName(dict_item)}
        db.add_success_open_record(json.dumps(item))
    else:
        item={"id": parse.uuid(dict_item),"location":parse.location(dict_item),\
              "timestamp":parse.timestamp(dict_item),"time":str(parse.time(dict_item))}
        db.add_failure_open_record(json.dumps(item))

    return jsonify({'status':"ok"})