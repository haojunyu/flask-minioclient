"""
@File    :   flask_minioclient.py
@Time    :   2021/03/14 3:47 下午
@Author  :   hjy
@Version :   1.0
@Contact :   haojunyu2012@gmail.com
@License :   (C)Copyright 2020-
@Desc    :   flask扩展：minio客户端
"""

import minio
from flask import current_app, _app_ctx_stack


class MinioError(Exception):
    ...


class MinioClient(object):
    """This class is used to control the Minio integration to one or more Flask
    applications.
    """

    def __init__(self, app=None,  endpoint=None, access_key=None, secret_key=None, **kwargs):
        self.endpoint = endpoint
        self.access_key = access_key
        self.secret_key = secret_key
        self.other = kwargs

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if self.endpoint is None:
            self.endpoint = app.config['MINIO_ENDPOINT']
        if self.access_key is None:
            self.access_key = app.config['MINIO_ACCESS_KEY']
        if self.secret_key is None:
            self.secret_key = app.config['MINIO_SECRET_KEY']

        self.secure = self.other.get('secure', False)   # bool
        self.region = self.other.get('region', None)    # str
        self.http_client = self.other.get(
            'http_client', None)  # urllib3.poolmanager.PoolManager

        app.teardown_appcontext(self.teardown)

    def connect(self):
        return minio.Minio(self.endpoint,
                           access_key=self.access_key, secret_key=self.secret_key,
                           secure=self.secure, region=self.region, http_client=self.http_client
                           )

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'minio'):
            ctx.minio._http.clear()
            current_app.info('clear minio: {}'.format(self.endpoint))

    @property
    def connection(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'minio'):
                ctx.minio = self.connect()
                current_app.info('connect minio: {}'.format(self.endpoint))
            return ctx.minio
