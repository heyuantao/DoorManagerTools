#-*- coding=utf-8 -*-
from flask import render_template, request, session, jsonify
from config import config
from views.CallBackView import dooropenevent_callback_view
from views.DisplayView import version_view, sucess_door_open_view, failure_door_open_view

ROUTER_PREFIX = config.AppConfig.ROUTE_PREFIX

class Route:

    def init_app(self, app=None, auth=None):
        @app.route(ROUTER_PREFIX + '/', methods=['GET'])  # 获取文件信息，可以查看文件是否存在
        def main_api():
            return version_view(request)

        @app.route(ROUTER_PREFIX + '/api/info/', methods=['GET'])  # 获取文件信息，可以查看文件是否存在
        def version_api():
            return version_view(request)

        @app.route(ROUTER_PREFIX + '/api/success/', methods=['GET'])  #
        def success_open_api():
            return sucess_door_open_view(request)

        @app.route(ROUTER_PREFIX + '/api/failure/', methods=['GET'])  #
        def failure_open_api():
            return failure_door_open_view(request)

        #该接口仅仅被智能网关调用
        @app.route(ROUTER_PREFIX + '/api/callback/dooropenevent/', methods=['POST'])  # 获取文件信息，可以查看文件是否存在
        def door_open_event_callback_api():
            return dooropenevent_callback_view(request)






        # ------------------------------------用于文件上传的接口---------------------------------#
        #@app.route(ROUTER_PREFIX+'/api/upload/', methods=['POST'])
        #def api_upload():  # 一个分片上传后被调用
        #    return api_upload_view()

        #@app.route(ROUTER_PREFIX+'/api/upload/success/', methods=['POST'])
        #def api_upload_success():  # 所有分片均上传完后被调用
        #    return api_upload_success_view()
