# 动态列表相关API

## 动态信息

### 动态列表（包括各种排序、筛选）

> `forum/posts/`, GET

返回动态列表，其中`images`中各个对象的`id`对应了一个图片，提供的`thumbnail`为base64缩略图。在详情界面需要使用下面单独的URL重新获取，得到完整图片。

该URL可以添加参数，用以筛选动态或指定排序：

- `user`：筛选特定用户的动态（值为用户名）
- `following`：筛选已关注用户的动态（值只能为`'true'`）
- `sortBy`：排序方式，支持`'time'`（发布时间）、`'comment-time'`（最新评论时间）、`'hot'`（最近一天内的评论数，至少为1，**目前还未实现**）

带URL参数的GET请求已通过`HTTPRequest.getWithParams`函数实现，前端可以直接调用。

**获取默认列表时无需登录信息（有信息也可）。如果需要添加参数，如筛选用户名、类别等，则需要登录信息。**

```json
[
  {
    "id": "c2adc042-6080-4cf4-841e-238d990a58a4",
    "title": "hi!",
    "content": "this is me",
    "createdAt": "2023-05-16T06:47:34.052062Z",
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
    "comments": 12,
    "isStarred": true
  }
]
```

### 新建动态

> `forum/posts/`, POST

需要登录，新建帖子。POST提交的JSON格式信息需要包含以下内容：

```json
{
  "title": "xxx",
  "content": "xxx",
  "images": [
    "image_id1",
    "image_id2"
  ],
  "tags": [
    "tag_name1",
    "tag_name2"
  ]
}
```

正常情况下返回ok（状态码200）：

```json
{
  "message": "ok"
}
```


### 动态详情

> `forum/posts/<post:id>`, GET

需要登录，获取帖子详情。其中与动态列表中的区别为`images`包含了完整图片。

```json
{
  "id": "c2adc042-6080-4cf4-841e-238d990a58a4",
  "title": "hi!",
  "content": "this is me",
  "createdAt": "2023-05-16T06:47:34.052062Z",
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
  "comments": 12,
  "isStarred": true
}
```

## 图片资源管理

### 添加图片

> `forum/image/`, POST

在JSON数据中使用图片的base64格式数据作为`data`项。

```json
{
  "data": "xxx"
}
```

正确添加后返回图片的ID信息与缩略图（`thumbnail`）：

```json
{
  "id": "xxx",
  "thumbnail": "xxx"
}
```


### 获取完整图片

> `forum/image/<image:id>`, GET

返回图片的ID信息与完整图（`content`）：

```json
{
  "id": "xxx",
  "content": "xxx"
}
```


### 删除图片

> `forum/image/<image:id>`, DELETE

正常删除后返回ok（状态码200）：

```json
{
  "message": "ok"
}
```

## 点赞与评论

### 点赞

> `forum/like/<post:id>`, POST

### 取消点赞

> `forum/like/<post:id>`, DELETE

### 点赞自己动态的列表

> `forum/likes/`, GET

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
      "id": "c25e99e6-4282-4d52-8856-0e019a816f7c",
      "title": "third post"
    },
    "createdAt": "2023-05-27 23:59:49"
  }
]
```

### 查看动态里的评论列表

> `forum/comment/<post:id>`, GET

返回JSON格式评论列表：

```json
[
  {
    "id": "1f596b74-f05c-42b8-98af-18a75bd5961a",
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
    "content": "haha3",
    "createdAt": "2023-05-27 23:52:43",
    "likes": 6
  }
]
```

### 发表评论

> `forum/comment/<post:id>`, POST

```json
{
  "content": "haha"
}
```

### 点赞评论

> `forum/comment/like/<comment:id>`, POST

仅支持点赞，不能取消点赞。目前可以不断点赞同一条。


### 评论自己动态的列表

> `forum/comments/`, GET

```json
[
  {
    "id": "188defed-b5b7-4e0a-9256-9a2655856ca2",
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
    "createdAt": "2023-05-27 23:30:54",
    "likes": 6
  }
]
```
