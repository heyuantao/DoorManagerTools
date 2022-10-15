#-*- coding=utf-8 -*-
from flask import render_template, request, session, jsonify
from config import config
from views.doormanagertools_view import version_view,dooropen_view

ROUTER_PREFIX = config.App.ROUTE_PREFIX

class Route:

    def init_app(self, app=None, auth=None):
        @app.route(ROUTER_PREFIX + '/api/info/', methods=['GET','POST'])  # 获取文件信息，可以查看文件是否存在
        def api_version_view():
            return version_view(request)

        @app.route(ROUTER_PREFIX + '/api/dooropen/', methods=['GET','POST'])  # 获取文件信息，可以查看文件是否存在
        def api_dooropen_view():
            return dooropen_view(request)

        # ------------------------------------用于文件上传的接口---------------------------------#
        #@app.route(ROUTER_PREFIX+'/api/upload/', methods=['POST'])
        #def api_upload():  # 一个分片上传后被调用
        #    return api_upload_view()

        #@app.route(ROUTER_PREFIX+'/api/upload/success/', methods=['POST'])
        #def api_upload_success():  # 所有分片均上传完后被调用
        #    return api_upload_success_view()
