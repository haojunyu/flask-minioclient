# flask_minioclient帮助文档

## 简介

对 minio 库进行包装，需要在 Flask 配置文件或对象创建时配置以下参数：

* 请求终端： MINIO_ENDPOINT/endpoint
* 访问账号：MINIO_ACCESS_KEY/access_key
* 访问密码：MINIO_SECRET_KEY/secret_key
* 其它信息：secure/region/http_client

## 安装

```python
    pip install flask-minioclient
```

## 使用

```python
    from flask_minioclient import MinioClient

    minio = MinioClient(endpoint='minio:9000',access_key='xxx', secret_key='xxx')

    # 创建 Flask 应用时集成扩展
    def create_app():
        app = Flask(__name__)
        minio.init_app(app)
    
    # app 中使用
    res = minio.connection.make_bucket('bucket_name')
```

## License

[MIT](https://github.com/pythonml/douyin_image/blob/master/LICENSE)