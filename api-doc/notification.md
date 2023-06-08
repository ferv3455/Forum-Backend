# 私信相关API

## 整体逻辑

- **消息列表应存储在本地**。
- 收到新消息提醒时，客户端应当调用**获取消息**的API，得到未接收的消息的列表。或者定时循环调用该API，简易实现？
- 确认接收到后，客户端应当调用**确认获取**的API，表示这些信息已被正确接收。
- 调用**发送消息**的API发送私信消息。

## API

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
