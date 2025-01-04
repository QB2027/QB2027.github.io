import os
import json
from datetime import datetime

def update_notices_json(textbundle_dir, notices_dir, output_file):
    """
    更新 notices.json 文件，生成相对于项目根目录的路径，并按照时间降序排序。
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
            # 转换日期字符串为 datetime 对象
            try:
                date_obj = datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                date_obj = None
            notice_folder = dirname.replace(".textbundle", "")
            html_file = f"data/notices/{notice_folder}/index.html"
            notices.append({
                "title": title,
                "date": date,
                "date_obj": date_obj,  # 用于排序
                "file": html_file
            })

    # 按日期降序排序
    notices = sorted(notices, key=lambda x: x["date_obj"], reverse=True)

    # 移除临时字段 date_obj
    for notice in notices:
        del notice["date_obj"]

    # 写入 JSON 文件
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({"notices": notices}, f, ensure_ascii=False, indent=4)
    print(f"Updated {output_file}")

