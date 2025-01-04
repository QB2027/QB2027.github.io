import os
import markdown
import json
from pathlib import Path


def load_info_json(bundle_dir):
    """
    加载 info.json 文件并返回内容。
    """
    info_path = bundle_dir / "info.json"
    if not info_path.exists():
        print(f"Warning: Missing info.json in {bundle_dir}")
        return None
    with open(info_path, "r", encoding="utf-8") as f:
        return json.load(f)


def find_markdown_file(bundle_dir):
    """
    查找 Markdown 文件 (.md 或 .markdown) 并返回路径。
    """
    for ext in [".md", ".markdown"]:
        markdown_path = bundle_dir / f"text{ext}"
        if markdown_path.exists():
            return markdown_path
    print(f"Warning: Missing Markdown file (.md or .markdown) in {bundle_dir}")
    return None


def extract_title_and_content(markdown_path):
    """
    提取 Markdown 文件的首行大标题和内容。
    """
    with open(markdown_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    lines = markdown_content.splitlines()
    main_title = lines[0].strip("# ").strip() if lines and lines[0].startswith("#") else "Untitled"
    content = "\n".join(lines[1:])
    return main_title, content


def generate_html(main_title, date, content):
    """
    生成 HTML 页面内容。
    """
    html_content = markdown.markdown(content)
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{main_title}</title>
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
        <a href="/index.html" style="display: block; margin-bottom: 1em;">← 返回首页</a>
        <h1>{main_title}</h1>
        <p><em>{date}</em></p>
        <div>{html_content}</div>
    </body>
    </html>
    """


def save_html(output_path, html):
    """
    将 HTML 内容保存到指定路径。
    """
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated HTML: {output_file}")


def convert_textbundle_to_html(textbundle_path, output_path):
    """
    主逻辑：将单个 TextBundle 文件转换为 HTML 文件。
    """
    try:
        bundle_dir = Path(textbundle_path)

        # 加载 info.json
        info = load_info_json(bundle_dir)
        if not info:
            return
        date = info.get("date", "Unknown Date")

        # 查找 Markdown 文件
        markdown_path = find_markdown_file(bundle_dir)
        if not markdown_path:
            return

        # 提取标题和内容
        main_title, content = extract_title_and_content(markdown_path)

        # 生成 HTML
        html = generate_html(main_title, date, content)

        # 保存 HTML
        save_html(output_path, html)

    except Exception as e:
        print(f"Error processing {textbundle_path}: {e}")
