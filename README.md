## 项目简介
本项目是一个用于管理文件下载和公告系统的网站，支持嵌套文件结构、公告展示和镜像加速功能。

---

## 维护指南

### 文件下载管理

#### 文件结构与 `files.json` 模板

- `files.json` 用于定义文件的嵌套结构。
- 支持文件夹嵌套、GitHub 仓库的分支信息以及直接外部链接。

**`files.json` 模板：**
```json
{
  "files": [
    {
      "repo": "<仓库名称>", "branch": "<分支名称>", "children": [
        { "name": "<文件名称>", "path": "<文件路径>" },
        { "name": "<文件名称>", "path": "<文件路径>" }
      ]
    },
    {
      "repo": "<仓库名称>", "branch": "<分支名称>", "children": [
        { "name": "<文件名称>", "path": "<文件路径>" }
      ]
    },
    { "name": "<外部链接文件名称>", "url": "<外部链接URL>" }
  ]
}
```

**字段说明：**
- `repo`：GitHub 仓库名称（如 `Qianban2027/Study`）。
- `branch`：GitHub 分支名称（如 `main`）。
- `children`：子文件夹或文件列表。
- `name`：文件或文件夹名称。
- `path`：文件在仓库中的路径。
- `url`：直接链接的文件 URL。

---

### 公告展示管理

#### 文件结构与内容

- 每个公告内容可以用 HTML 格式书写。
- 注意统一样式。

**文件结构：**
```
命名空间
├── config.json
└── index.html
```

##### **`config.json` 模板：**
```json
{
  "title": "<公告标题>",
  "date": "<公告日期>"
}
```
##### **`index.html` 模版：**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>页面标题</title>
    
    <!-- 基础样式文件，提供全局的布局和基础功能样式 -->
    <link rel="stylesheet" href="../css/base.css">
    
    <!-- 排版样式文件，提供标题和段落等文字的样式 -->
    <link rel="stylesheet" href="../css/typography.css">
</head>
<body>
    <!-- 返回首页链接 -->
    <nav>
        <a href="/index.html" class="back-link">← 返回首页</a>
    </nav>

    <!-- 页面标题 -->
    <header>
        <h1 class="title">页面标题</h1>
    </header>

    <!-- 页面正文 -->
    <main class="content">
        <p>这是正文内容。</p>
    </main>
</body>
</html>
```

##### **`CSS` 使用说明：**
见[CSS使用说明](docs/css-guidelines.md)

**注意：**
- `HTML` 文件将包含一个返回按钮，便于用户返回上一页面。
- 使用 `CSS` 统一样式
---

## 自动化脚本与部署

无需本地运行，自动化脚本会在推送到主分支后自动运行以下功能：
- 更新公告 JSON 文件（`notices.json`）。

---

## 贡献指南

1. Fork 本仓库并创建分支。
2. 提交代码并确保通过自动化测试。
3. 提交 Pull Request 并描述修改内容。

---

## 许可证

本项目采用 [知识共享署名-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-sa/4.0/) 进行许可。

