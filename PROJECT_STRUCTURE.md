# 项目目录结构

```plaintext
project/
├── .github/
│   └── workflows/
│       └── generate-html.yml         # GitHub Actions 配置
├── scripts/                          # Python 脚本模块
│   ├── __init__.py                   # 标记为模块
│   ├── convert.py                    # textbundle 转 HTML 模块
│   ├── update_json.py                # 生成 JSON 文件模块
│   ├── main.py                       # 主入口文件
├── static/                           # 静态文件
│   ├── css/
│   │   └── style.css                 # CSS 样式文件
│   ├── js/
│   │   ├── main.js                   # 主入口 JS
│   │   ├── fileManager.js            # 文件管理模块
│   │   ├── noticeManager.js          # 公告管理模块
│   │   ├── utils.js                  # 通用工具模块
│   ├── html/
│   │   ├── header.html               # Header 模块
│   │   ├── footer.html               # Footer 模块
│   │   ├── fileList.html             # 文件列表容器
│   │   ├── noticeList.html           # 公告列表容器
│   ├── img/
│   │   └── logo.png                  # LOGO 文件
├── data/                             # 数据存储
│   ├── textbundle/                   # 原始 textbundle 文件
│   │   ├── project_meeting.textbundle/ # 公告“项目会议”
│   │   │   ├── info.json             # 公告元数据
│   │   │   ├── text.md               # 公告内容
│   │   │   ├── assets/               # 公告资源文件
│   │   │       ├── image1.png
│   │   ├── release_notes.textbundle/ # 公告“版本说明”
│   │       ├── info.json
│   │       ├── text.md
│   │       ├── assets/
│   │           ├── image1.png
│   │           ├── diagram.svg
│   ├── notices/                      # 转换后的 HTML 文件，每个公告一个文件夹
│   │   ├── project_meeting/          # 公告“项目会议”文件夹
│   │   │   ├── index.html            # 公告 HTML 文件
│   │   │   ├── image1.png            # 公告资源文件
│   │   ├── release_notes/            # 公告“版本说明”文件夹
│   │       ├── index.html
│   │       ├── image1.png
│   │       ├── diagram.svg
│   ├── notices.json                  # 自动生成的公告 JSON 文件
│   ├── files.json                    # 文件下载 JSON 文件
├── index.html                        # 主 HTML 文件
├── LICENSE                           # 项目 License 文件
├── README.md                         # 项目说明文件
├── .gitignore                        # Git 忽略文件
