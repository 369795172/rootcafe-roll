# Root Cafe Roll a Die
[![GitHub license](https://img.shields.io/github/license/WeixinCloud/wxcloudrun-express)](https://github.com/WeixinCloud/wxcloudrun-express)
![GitHub package.json dependency version (prod)](https://img.shields.io/badge/python-3.7.3-green)

微信云托管 python Django 框架模版，实现简单的抽奖读写接口，使用云托管 MySQL 读写、记录数值。






## 目录结构说明
~~~
.
├── Dockerfile                  dockerfile
├── README.md                   README.md文件
├── container.config.json       模板部署「服务设置」初始化配置（二开请忽略）
├── manage.py                   django项目管理文件 与项目进行交互的命令行工具集的入口
├── requirements.txt            依赖包文件
└── wxcloudrun                  app目录
    ├── __init__.py             python项目必带  模块化思想
    ├── apps.py                 自动生成文件apps.py
    ├── asgi.py                 自动生成文件asgi.py, 异步服务网关接口
    ├── migrations              数据移植（迁移）模块
    ├── models.py               数据模块
    ├── settings.py             项目的总配置文件  里面包含数据库 web应用 日志等各种配置
    ├── templates               模版目录,包含主页index.html文件
    ├── urls.py                 URL配置文件  Django项目中所有地址中（页面）都需要我们自己去配置其URL
    ├── views.py                执行响应的代码所在模块  代码逻辑处理主要地点  项目大部分代码在此编写
    └── wsgi.py                 自动生成文件wsgi.py, Web服务网关接口
~~~


## 服务 API 文档

### `GET /api/roll`

获取当前抽奖折扣

#### 请求参数

无

#### 响应结果

- `code`：错误码
- `data`：当前折扣数

##### 响应结果示例

```json
{
  "code": 0,
  "data": 10 
}
```

#### 调用示例

```
curl https://<云托管服务域名>/api/roll
```




## 使用注意
如果不是通过微信云托管控制台部署模板代码，而是自行复制/下载模板代码后，手动新建一个服务并部署，需要在「服务设置」中补全以下环境变量，才可正常使用，否则会引发无法连接数据库，进而导致部署失败。
- MYSQL_ADDRESS
- MYSQL_PASSWORD
- MYSQL_USERNAME
以上三个变量的值请按实际情况填写。如果使用云托管内MySQL，可以在控制台MySQL页面获取相关信息。


## License

[MIT](./LICENSE)
