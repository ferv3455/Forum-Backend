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


## 动态列表

### 动态信息

> `forum/posts/`, GET

**无需登录信息**（有信息也可）。返回动态列表，其中`images`中各个对象的`id`对应了一个图片，提供的`thumbnail`为base64缩略图。在详情界面需要使用下面单独的URL重新获取，得到完整图片。

```json
[
  {
    "id": "c2adc042-6080-4cf4-841e-238d990a58a4",
    "title": "hi!",
    "content": "this is me",
    "createdAt": "2023-05-16T06:47:34.052062Z",
    "user": {
      "username": "xxx"
    },
    "images": [
      {
        "id": "07114cbe-6853-4476-94c7-833e3f259986",
        "thumbnail": "data:image/jpeg;base64,/9j/4AAQ..."
      },
      {
        "id": "d95caf8b-c12c-44ef-a3f7-5dcdcf386f3b",
        "thumbnail": "data:image/jpeg;base64,/9j/4AAQ..."
      }
    ],
    "tags": [
      {
        "name": "Activity"
      }
    ],
    "likes": 23,
    "favorites": 432,
    "comments": 12
  }
]
```

### 新建动态

> `forum/posts/`, POST

需要登录，新建帖子。

TODO


### 动态详情

> `forum/posts/<post:id>`, GET

需要登录，获取帖子详情。其中与动态列表中的区别为`images`包含了完整图片。

```json
{
  "id": "c2adc042-6080-4cf4-841e-238d990a58a4",
  "title": "hi!",
  "content": "this is me",
  "createdAt": "2023-05-16T06:47:34.052062Z",
  "user": {
    "username": "xxx"
  },
  "images": [
    {
      "id": "07114cbe-6853-4476-94c7-833e3f259986",
      "content": "data:image/jpeg;base64,/9j/4AAQ..."
    },
    {
      "id": "d95caf8b-c12c-44ef-a3f7-5dcdcf386f3b",
      "content": "data:image/jpeg;base64,/9j/4AAQ..."
    }
  ],
  "tags": [
    {
      "name": "Activity"
    }
  ],
  "likes": 23,
  "favorites": 432,
  "comments": 12
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
