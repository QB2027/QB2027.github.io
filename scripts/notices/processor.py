import os
from notices.reader import is_valid_namespace

def process_namespace(base_dir, namespace):
    """
    处理命名空间，返回公告信息列表
    :param base_dir: 基础路径
    :param namespace: 命名空间
    :return: 公告信息列表
    """
    namespace_path = os.path.join(base_dir, namespace)

    # 检查是否为有效命名空间
    if not is_valid_namespace(namespace_path):
        return []

    # 模拟读取 config.json 文件或直接生成默认公告信息
    config_file = os.path.join(namespace_path, "config.json")
    return [{
        "title": namespace,  # 假设标题直接取命名空间名
        "date": "2024-01-03",  # 模拟日期
        "file": f"data/notices/{namespace}/index.html"
    }]