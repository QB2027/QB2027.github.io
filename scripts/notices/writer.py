import json

def write_json_file(output_file, notices):
    """
    将公告列表写入 JSON 文件
    :param output_file: 输出文件路径
    :param notices: 公告列表
    """
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({"notices": notices}, f, ensure_ascii=False, indent=4)