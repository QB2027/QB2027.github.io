import os
from notices.processor import process_namespace
from notices.writer import write_json_file

# 定义基础路径
BASE_DIR = "data/notices"
OUTPUT_FILE = "data/notice.json"

def generate_notice_json():
    """生成公告 JSON 文件"""
    notices = []
    for namespace in os.listdir(BASE_DIR):
        namespace_path = os.path.join(BASE_DIR, namespace)
        # 检查是否为目录并处理命名空间
        if os.path.isdir(namespace_path):
            notices.extend(process_namespace(BASE_DIR, namespace))
    
    # 写入 JSON 文件
    write_json_file(OUTPUT_FILE, notices)
    print(f"JSON file has been generated at {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_notice_json()