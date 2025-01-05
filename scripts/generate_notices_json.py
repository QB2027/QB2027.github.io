import os
from notices.processor import process_namespace
from notices.writer import write_json_file
from notices.sorter import sort_notices

# 定义基础路径
BASE_DIR = "data/notices"
OUTPUT_FILE = "data/notices.json"

def generate_notices_json():
    """生成公告 JSON 文件"""
    notices = []
    for namespace in os.listdir(BASE_DIR):
        namespace_path = os.path.join(BASE_DIR, namespace)
        # 检查是否为有效目录
        if os.path.isdir(namespace_path):
            notices.extend(process_namespace(BASE_DIR, namespace))
    
    # 按时间倒序、标题排序
    sorted_notices = sort_notices(notices)
    write_json_file(OUTPUT_FILE, sorted_notices)
    print(f"JSON file has been generated at {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_notices_json()