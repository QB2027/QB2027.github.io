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

### TextBundle 管理

#### TextBundle 文件结构与内容

- 每个公告内容可以用 TextBundle 格式定义，包含 `info.json` 和 `text.markdown` 文件。
- 公告标题需写在 Markdown 文件的首行大标题中，同时保留 `info.json` 中的标题用于超链接表示。

**文件结构：**
```
textbundle
├── info.json
└── text.markdown
```

**`info.json` 模板：**
```json
{
  "title": "<公告标题>",
  "date": "<公告日期>"
}
```

**`text.markdown` 模板：**
```markdown
# <公告标题>

<公告内容>
```

**注意：**
- Markdown 文件首行的 `#` 大标题会显示为 HTML 中的大字体标题，同时作为页面 `<title>` 内容。
- `info.json` 的 `title` 用作外部链接的显示文字。
- 公告内容紧跟标题，支持普通文本和 Markdown 格式。
- 生成的 HTML 文件将包含一个返回按钮，便于用户返回上一页面。

---

## 自动化脚本与部署

无需本地运行，自动化脚本会在推送到主分支后自动运行以下功能：

1. 转换 `textbundle` 为 HTML 文件。
   - 将 Markdown 文件的首行大标题作为 HTML 主标题和页面 `<title>`。
   - 在 HTML 文件中添加返回按钮。
2. 更新公告 JSON 文件（`notices.json`）。

---

## 贡献指南

1. Fork 本仓库并创建分支。
2. 提交代码并确保通过自动化测试。
3. 提交 Pull Request 并描述修改内容。

---

## 许可证

本项目采用 [知识共享署名-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-sa/4.0/) 进行许可。

