# 用户账号相关API

> **所有API的调用均需要在header中添加token。**

## 基本信息

### 获取用户（个人与其他用户）信息

> `account/profile` GET （获取自己）
> 
> `account/profile/<username>` GET

获取用户的个人信息，包括头像`avatar`（base64格式）与自我介绍`description`：

```json
{
  "user": {
    "id": 1,
    "username": "tester1"
  },
  "avatar": "avatar1",
  "description": "desc1"
}
```

### 修改个人账号信息（头像、自我介绍）

> `account/profile` PUT

提交JSON数据来表示要修改的新头像与新自我介绍（**两项均为可选，即可以只修改其中一项**）：

```json
{
  "avatar": "new_avatar",
  "description": "new_description"
}
```
```json
{
  "avatar": "new_avatar"
}
```
```json
{
  "description": "new_description"
}
```

修改成功后返回ok（状态码200）：

```json
{
  "message": "ok"
}
```

### 修改个人账号用户名

> `account/username` PUT

提交JSON数据表示新用户名：

```json
{
  "old_password": "old_passwordxxxxxx",
  "password": "new_passwordxxxxxx"
}
```

修改成功后返回ok（状态码200）：

```json
{
  "message": "ok"
}
```

### 修改个人账号密码

> `account/password` PUT

提交JSON数据表示旧密码与新密码：

```json
{
  "old_password": "old_passwordxxxxxx",
  "password": "new_passwordxxxxxx"
}
```

修改成功后返回ok（状态码200）：

```json
{
  "message": "ok"
}
```


## 关注列表

### 获取用户（个人与其他用户）关注列表

> `account/following` GET （获取自己）
> 
> `account/following/<username>` GET

获取用户的关注列表，格式如下：

```json
{
  "user": {
    "id": 1,
    "username": "ferv3455"
  },
  "following": [
    {
      "user": {
        "id": 2,
        "username": "tester1"
      },
      "avatar": "aa",
      "description": "dd"
    },
    {
      "user": {
        "id": 3,
        "username": "tester2"
      },
      "avatar": "aa",
      "description": "dd"
    }
  ]
}
```

### 关注其他用户

> `account/following` PUT

以JSON格式提交新关注对象的用户名列表：

```json
{
  "username": ["tester1", "tester2"]
}
```

修改成功后返回ok（状态码200）：

```json
{
  "message": "ok"
}
```

### 取消关注其他用户

> `account/following` DELETE

以JSON格式提交取消关注对象的用户名列表：

```json
{
  "username": ["tester1", "tester2"]
}
```

修改成功后返回ok（状态码200）：

```json
{
  "message": "ok"
}
```

### 获取关注该用户（个人与其他用户）的用户列表

> `account/followed` GET （获取自己）
> 
> `account/followed/<username>` GET

获取用户的受到关注列表，格式如下：

```json
{
  "user": {
    "id": 1,
    "username": "ferv3455"
  },
  "followed": [
    {
      "user": {
        "id": 2,
        "username": "tester1"
      },
      "avatar": "aa",
      "description": "dd"
    },
    {
      "user": {
        "id": 3,
        "username": "tester2"
      },
      "avatar": "aa",
      "description": "dd"
    }
  ]
}
```

## 收藏夹列表

### 获取用户（个人与其他用户）收藏夹列表

> `account/favorites` GET （获取自己）
> 
> `account/favorites/<username>` GET

获取用户的收藏列表，**同样支持`sortBy`参数**，格式类似动态列表，：

```json
[
  {
    "id": "c25e99e6-4282-4d52-8856-0e019a816f7c",
    "title": "third post",
    "content": "hello there!",
    "createdAt": "2023-05-19T15:18:59.605920Z",
    "user_profile": {
        "user": {
          "id": 1,
          "username": "ferv3455"
        },
        "avatar": "aa",
        "description": "dd"
      },
    "images": [
      {
        "id": "07c6fb95-0747-414d-b6bd-7e4a9087f848",
        "thumbnail": "xxx"
      },
      {
        "id": "e16817ac-9692-4a5b-857e-730d145851ba",
        "thumbnail": "xxx"
      }
    ],
    "tags": [
      {
        "name": "Activity"
      }
    ],
    "likes": 0,
    "favorites": 0,
    "comments": 0,
    "isStarred": true
  }
]
```

### 收藏动态

> `account/favorites` PUT

以JSON格式提交新收藏帖子的id列表：

```json
{
    "id": [
        "c25e99e6-4282-4d52-8856-0e019a816f7c", 
        "c30d36ea-100d-4654-b83a-2e143b4897c5"
    ]
}
```

修改成功后返回ok（状态码200）：

```json
{
  "message": "ok"
}
```

### 取消收藏

> `account/favorites` DELETE

以JSON格式提交取消收藏帖子的id列表：

```json
{
    "id": [
        "c25e99e6-4282-4d52-8856-0e019a816f7c", 
        "c30d36ea-100d-4654-b83a-2e143b4897c5"
    ]
}
```

修改成功后返回ok（状态码200）：

```json
{
  "message": "ok"
}
```
