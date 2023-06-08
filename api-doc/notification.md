# 通知相关API

## 通知整体逻辑

- **消息列表应存储在本地**。
- 收到新消息提醒时，客户端应当调用**获取消息**的API，得到未接收的消息的列表。或者定时循环调用该API，简易实现？
- 确认接收到后，客户端应当调用**确认获取**的API，表示这些信息已被正确接收。
- 调用**发送消息**的API发送私信消息。

## 私信

### 获取未收到的新消息

> `notification/messages/`, GET

```json
[
  {
    "fromUser": {
      "user": {
        "id": 2,
        "username": "tester1"
      },
      "avatar": "aa",
      "description": "dd"
    },
    "toUser": {
      "user": {
        "id": 1,
        "username": "ferv3455"
      },
      "avatar": "aa",
      "description": "dd"
    },
    "content": "haha!",
    "createdAt": "2023-06-08 19:10:19"
  }
]
```

### 发送新消息

> `notification/messages/`, POST

```json
{
    "user": "tester1",
    "content": "haha!"
}
```

### 确认接收新消息

> `/notification/messages-received/`, POST

服务端会确认**该时间之前的所有未接收信息**。时间格式为`"%Y-%m-%d %H:%M:%S"`。

```json
{
    "time": "2023-06-08 19:20:19"
}
```

## 点赞消息

### 获取未收到的新点赞消息

> `notification/likes/`, GET

```json
[
  {
    "user_profile": {
      "user": {
        "id": 1,
        "username": "ferv3455"
      },
      "avatar": "aa",
      "description": "dd"
    },
    "post": {
      "id": "13f6a59b-04d2-448b-8e05-d07ac45f5d7f",
      "title": "fifth post"
    },
    "createdAt": "2023-06-08 23:24:58"
  }
]
```

### 确认接收新点赞消息

> `/notification/likes-received/`, POST

服务端会确认**该时间之前的所有未接收的点赞消息**。时间格式为`"%Y-%m-%d %H:%M:%S"`。

```json
{
    "time": "2023-06-08 19:20:19"
}
```

## 评论消息

### 获取未收到的新评论消息

> `notification/comments/`, GET

```json
[
  {
    "id": "e48e5c3e-424e-49c9-ab5d-46d626110c03",
    "user_profile": {
      "user": {
        "id": 1,
        "username": "ferv3455"
      },
      "avatar": "aa",
      "description": "dd"
    },
    "post": {
      "id": "c25e99e6-4282-4d52-8856-0e019a816f7c",
      "title": "third post"
    },
    "content": "haha",
    "createdAt": "2023-06-08 23:24:32",
    "likes": 0
  }
]
```

### 确认接收新评论消息

> `/notification/comments-received/`, POST

服务端会确认**该时间之前的所有未接收的评论消息**。时间格式为`"%Y-%m-%d %H:%M:%S"`。

```json
{
    "time": "2023-06-08 19:20:19"
}
```
