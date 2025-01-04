import os
import json
from markdown import markdown

def convert_textbundle_to_html(textbundle_path, output_path):
    """
    将单个 textbundle 文件转换为 HTML 并保存到指定位置。
    """
    # 加载 info.json
    info_path = os.path.join(textbundle_path, "info.json")
    text_md_path = os.path.join(textbundle_path, "text.md")
    text_markdown_path = os.path.join(textbundle_path, "text.markdown")

    # 检查 text.md 或 text.markdown 是否存在
    if os.path.exists(text_md_path):
        text_path = text_md_path
    elif os.path.exists(text_markdown_path):
        text_path = text_markdown_path
    else:
        print(f"Warning: Missing text.md or text.markdown in {textbundle_path}. Skipping...")
        return

    with open(info_path, "r", encoding="utf-8") as f:
        info = json.load(f)
    title = info.get("title", "无标题")
    date = info.get("date", "未知日期")

    # 加载公告内容
    with open(text_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Markdown 转 HTML
    html_body = markdown(content, extensions=["extra", "nl2br", "toc", "fenced_code"])

    # 添加 MathJax 支持和页面结构
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script>
      MathJax = {{
        tex: {{
          inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
          displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
        }},
        svg: {{
          fontCache: 'global'
        }}
      }};
    </script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }}
        h1, h2, h3 {{ color: #0078d7; }}
        pre, code {{ background: #f4f4f4; padding: 5px; border-radius: 5px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        table, th, td {{ border: 1px solid #ddd; padding: 8px; }}
        th {{ background-color: #f2f2f2; }}
        a {{ color: #0078d7; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
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
