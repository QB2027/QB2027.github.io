import os
import json
from notices.reader import is_valid_namespace

def process_namespace(base_dir, namespace):
    """
    处理命名空间，返回公告信息列表
    :param base_dir: 基础路径
    :param namespace: 命名空间
    :return: 公告信息列表
    """
    namespace_path = os.path.join(base_dir, namespace)

    # 判断是否为有效命名空间
    if not is_valid_namespace(namespace_path):
        return []

    # 生成公告信息
    config_file = os.path.join(namespace_path, "config.json")
    date = "1970-01-01"  # 默认日期
    if os.path.exists(config_file):
        try:
            with open(config_file, "r", encoding="utf-8") as f:
                config = json.load(f)
                date = config.get("date", "未知日期")  # 提取日期字段
        except (json.JSONDecodeError, IOError):
            print(f"Failed to read or parse {config_file}")

    return [{
        "title": namespace,  # 假设标题直接取命名空间名
        "date": date,        # 使用提取的日期信息
        "file": f"data/notices/{namespace}/index.html"
    }]