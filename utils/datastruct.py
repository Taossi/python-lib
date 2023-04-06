###########################
# 数据结构相关方法
###########################

# 字典list排序，默认升序
def sort_dict_list(lis, key, desc=False):
    if not isinstance(lis, list):
        return
    reverse = False
    if desc:
        reverse = True
    lis.sort(key=lambda k: (k.get(key, 0)), reverse=reverse)

# 把数组每个元素转成指定类型
def arr_type_change(arr, typ='str'):
    ret_arr = []
    for v in arr:
        if typ == 'str':
            ret_arr.append(str(v))
        elif typ == 'int':
            ret_arr.append(int(v))
        elif typ == 'float':
            ret_arr.append(float(v))
    return ret_arr

# 数组去掉括号，返回以","为间隔的字符串，针对int类型
def get_list_str(lis):
    return str(",".join(str(i) for i in lis))

# 数组去掉括号，返回以","为间隔的字符串，针对字符串类型
def get_list_str_str(lis):
    return str(",".join(("\'" + str(i) + "\'") for i in lis))
