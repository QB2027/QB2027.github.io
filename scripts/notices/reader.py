import os
import json

def get_html_files(namespace_path):
    """
    获取指定文件夹中的所有 HTML 文件
    :param namespace_path: 命名空间路径
    :return: HTML 文件名列表
    """
    if not os.path.isdir(namespace_path):
        raise NotADirectoryError(f"Not a valid directory: {namespace_path}")
    
    return [
        file for file in os.listdir(namespace_path)
        if file.endswith(".html")
    ]

def is_valid_namespace(namespace_path, ignored_dirs=None):
    """
    判断是否为有效的命名空间
    :param namespace_path: 命名空间路径
    :param ignored_dirs: 忽略的目录列表
    :return: 布尔值，是否为有效目录
    """
    if ignored_dirs is None:
        ignored_dirs = [".", "css"]

    # 检查是否为隐藏目录或指定忽略目录
    namespace_name = os.path.basename(namespace_path)
    return os.path.isdir(namespace_path) and not namespace_name.startswith(".") and namespace_name not in ignored_dirs

def read_config(config_path):
    """
    读取并解析配置文件 config.json
    :param config_path: 配置文件路径
    :return: 配置内容字典或 None（如果读取失败）
    """
    if not os.path.exists(config_path):
        return None
    
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Error parsing JSON file: {config_path}")
        return None