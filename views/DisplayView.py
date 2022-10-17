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
import logging

logger = logging.getLogger(__name__)

def version_view(request):
    print("software version request !")
    print("request:")
    print(request.args)
    return jsonify({'version':"1.0.0"})


def sucess_door_open_view(request):
    pass

def failure_door_open_view(request):
    pass