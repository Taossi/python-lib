# 获取今天0点时间戳
import datetime
import time

###########################
# 时间戳相关方法
###########################

# 时间字符串转时间戳
def get_ts_by_str(ts_str='2021-01-01 00:00:00', fmt='%Y-%m-%d %H:%M:%S'):
    return int(time.mktime(time.strptime(ts_str, fmt)))

# 时间戳转时间字符串
def get_time_str_by_ts(ts, fmt="%Y-%m-%d %H:%M:%S"):
    return time.strftime(fmt, time.localtime(ts))

# 获取今天0点时间戳
def get_today_zero_time():
    return int(time.mktime(datetime.date.today().timetuple()))

# 获取时间戳对应的0点时间戳
def get_time_zero_time(t):
    ymd = get_time_str_by_ts(t, "%Y-%m-%d")
    ymd_hms = ymd + " 00:00:00"
    return get_ts_by_str(ymd_hms)

# 秒数转时间
intervals = (
    ('Y', 31536000),  # 60 * 60 * 24 * 365
    ('D', 86400),  # 60 * 60 * 24
    ('H', 3600),  # 60 * 60
    ('M', 60),
    ('S', 1),
)

def display_time(seconds, max_unit='D', granularity=2):
    unit_idx = 0
    if max_unit == 'Y':  # 年
        unit_idx = 0
    elif max_unit == 'D':  # 日
        unit_idx = 1
    elif max_unit == 'H':  # 小时
        unit_idx = 2
    elif max_unit == 'M':  # 分钟
        unit_idx = 3
    elif max_unit == 'S':  # 秒
        unit_idx = 4

    result = []
    for name, count in tuple(list(intervals)[unit_idx:]):
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('S')
            result.append("{}{}".format(value, name))
    return ', '.join(result[:granularity])