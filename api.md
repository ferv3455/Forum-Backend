# 移动应用大作业后端API

## 登录/注册

### 登录

> `auth/login/`, POST

Header中不能包含token。提交数据：
```json
{
  "username": "xxx",
  "password": "xxx"
}
```
正常情况下返回token（状态码200）：
```json
{
  "token": "xxx"
}
```
返回的token需要添加到其他请求的Header中，格式为：
```text
Authorization: Token xxxxxx
```


### 登出

> `auth/logout/`, GET

Header中需要包含token。正常情况下返回ok（状态码200）：

```json
{
  "message": "ok"
}
```


### 注册

> `auth/register/`, POST

Header中不能包含token。提交数据：
```json
{
  "username": "xxx",
  "password": "xxx"
}
```
正常情况下直接完成登录，返回token（状态码200）：
```json
{
  "token": "xxx"
}
```
返回的token需要添加到其他请求的Header中。


### 检测登录状态token

> `auth/check-valid/`, GET

Header中需要包含token。正常情况下返回ok（状态码200）：

```json
{
  "message": "ok"
}
```


## 测试内容

> `forum/`, GET

在正确登录的情况下（Header中有token），能够正确返回hello信息：

```json
{
  "message": "hello!"
}
```
