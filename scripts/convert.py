# scripts/convert.py

import os
import json
from markdown import markdown

def convert_textbundle_to_html(textbundle_path, output_path):
    """
    将单个 textbundle 文件转换为 HTML 并保存到指定位置。
    """
    # 加载 info.json
    info_path = os.path.join(textbundle_path, "info.json")
    with open(info_path, "r", encoding="utf-8") as f:
        info = json.load(f)
    title = info.get("title", "无标题")
    date = info.get("date", "未知日期")

    # 加载 text.md
    text_path = os.path.join(textbundle_path, "text.md")
    with open(text_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Markdown 转 HTML
    html_body = markdown(content, extensions=["extra", "toc", "tables", "fenced_code"])

    # 处理资源路径
    assets_path = os.path.join(textbundle_path, "assets")
    if os.path.exists(assets_path):
        html_body = html_body.replace("](assets/", f"]({assets_path}/")

    # 添加 HTML 页面结构
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{date} - {title}</title>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
    <h1>{title}</h1>
    <p><em>{date}</em></p>
    {html_body}
</body>
</html>
"""

    # 写入 HTML 文件
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Converted {textbundle_path} to {output_path}")
