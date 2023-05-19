# 登录状态验证相关API

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


## 登录状态

### 检测token是否可用

> `auth/check-valid/`, GET

Header中需要包含token。正常情况下返回ok（状态码200）：

```json
{
  "message": "ok"
}
```
