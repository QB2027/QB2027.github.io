from datetime import datetime

def sort_notices(notices):
    """
    对公告列表按照时间升序排序，日期相同的按照标题排序
    :param notices: 公告列表
    :return: 排序后的公告列表
    """
    def sort_key(notice):
        # 提取日期并解析为 datetime 对象，处理无效日期
        date_str = notice.get("date", "0000-00-00")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            date = datetime.min  # 无效日期设置为最小时间
        # 返回排序键：时间升序、标题升序
        return (date.timestamp(), notice.get("title", ""))

    return sorted(notices, key=sort_key)