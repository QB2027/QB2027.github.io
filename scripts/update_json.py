# scripts/update_json.py

import os
import json

def update_notices_json(textbundle_dir, notices_dir, output_file):
    """
    更新 notices.json 文件。
    """
    notices = []
    for dirname in os.listdir(textbundle_dir):
        if dirname.endswith(".textbundle"):
            bundle_path = os.path.join(textbundle_dir, dirname)
            info_path = os.path.join(bundle_path, "info.json")
            with open(info_path, "r", encoding="utf-8") as f:
                info = json.load(f)
            title = info.get("title", "无标题")
            date = info.get("date", "未知日期")
            notice_folder = dirname.replace(".textbundle", "")
            html_file = os.path.join(notices_dir, notice_folder, "index.html").replace("\\", "/")
            notices.append({
                "title": title,
                "date": date,
                "file": html_file
            })

    # 写入 JSON 文件
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({"notices": notices}, f, ensure_ascii=False, indent=4)
    print(f"Updated {output_file}")
