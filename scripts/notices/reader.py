import os

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