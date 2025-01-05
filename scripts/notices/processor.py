import os
from notices.reader import is_valid_namespace, read_config

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

    # 读取 config.json 文件
    config_file = os.path.join(namespace_path, "config.json")
    config = read_config(config_file)

    # 获取配置文件中的标题和日期信息
    if config:
        return [{
            "title": config.get("title", "无标题"),
            "date": config.get("date", "未知日期"),  # 获取日期字段
            "file": f"data/notices/{namespace}/index.html"
        }]
    return []