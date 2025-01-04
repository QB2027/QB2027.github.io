import os
import shutil
from textbundle_converter import convert_textbundle_to_html
from update_json import update_notices_json


# 定义目录
TEXTBUNDLE_DIR = "data/textbundle"
NOTICES_DIR = "data/notices"
NOTICES_JSON = "data/notices.json"

def clear_notices_directory():
    """
    清空 notices 文件夹和 notices.json。
    """
    if os.path.exists(NOTICES_DIR):
        shutil.rmtree(NOTICES_DIR)
    os.makedirs(NOTICES_DIR, exist_ok=True)

    if os.path.exists(NOTICES_JSON):
        os.remove(NOTICES_JSON)

def process_textbundle_files():
    """
    遍历 TEXTBUNDLE_DIR 下的所有 textbundle 文件并转换为 HTML。
    """
    for dirname in os.listdir(TEXTBUNDLE_DIR):
        if dirname.endswith(".textbundle"):
            textbundle_path = os.path.join(TEXTBUNDLE_DIR, dirname)
            notice_name = dirname.replace(".textbundle", "")
            output_folder = os.path.join(NOTICES_DIR, notice_name)
            output_path = os.path.join(output_folder, "index.html")
            convert_textbundle_to_html(textbundle_path, output_path)

    # 更新 Notices JSON
    update_notices_json(TEXTBUNDLE_DIR, NOTICES_DIR, NOTICES_JSON)

if __name__ == "__main__":
    # 清空 notices 文件夹和 JSON 文件
    clear_notices_directory()
    # 处理 textbundle 文件
    process_textbundle_files()
