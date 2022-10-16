#-*- coding=utf-8 -*-
from flask import request, jsonify, current_app, stream_with_context, Response
#from flask_api import status
from utils.Parser import DoorManagerRecordParser
import time
#from werkzeug.urls import url_quote
import urllib.parse
import base64
import re
from datetime import datetime,timedelta
import traceback
from config import config
import mimetypes
import json
import logging

logger = logging.getLogger(__name__)

def version_view(request):
    print("software version request !")
    print("request:")
    print(request.args)
    return jsonify({'version':"1.0.0"})

def dooropen_view(request):
    data_str = request.data.decode("UTF-8")
    dict_item = json.loads(data_str)
    # print(dict_item)
    print("发生开门事件在{},记录编号为{}".format(DoorManagerRecordParser.time(dict_item), DoorManagerRecordParser.uuid(dict_item)))
    if DoorManagerRecordParser.isUser(dict_item):
        print("教师 {} 打开了 {}".format(DoorManagerRecordParser.name(dict_item), DoorManagerRecordParser.location(dict_item)))
    if DoorManagerRecordParser.isGuest(dict_item):
        print("{} 设置的访客 {} 打开了 {}".format(DoorManagerRecordParser.visitedName(dict_item),
                                          DoorManagerRecordParser.name(dict_item),
                                          DoorManagerRecordParser.location(dict_item)))

    return jsonify({'status':"ok"})