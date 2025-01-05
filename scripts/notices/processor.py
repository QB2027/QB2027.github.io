import os
from notices.reader import is_valid_namespace, get_html_files

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
    return [{
        "title": namespace,  # 假设标题直接取命名空间名
        "date": "未知日期",   # 假设没有日期信息
        "file": f"data/notices/{namespace}/index.html"
    }]