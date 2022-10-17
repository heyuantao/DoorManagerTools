#-*- coding=utf-8 -*-
from flask import request, jsonify, current_app, stream_with_context, Response, make_response
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
from db import Database
import mimetypes
import json
import logging

logger = logging.getLogger(__name__)
db = Database()

def version_view(request):
    #print(request.args)
    return jsonify({'version':"1.0.0"})


def sucess_door_open_view(request):
    record_list = db.get_all_success_record()
    print(record_list)
    #return jsonify(record_list)
    response = make_response(jsonify(record_list))
    response.headers['Content-Type'] = 'application/json;charset=UTF-8'
    return response

def failure_door_open_view(request):
    record_list = db.get_all_failure_record()
    return jsonify(record_list)