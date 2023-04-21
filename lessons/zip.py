def zip(str_list: list[str], int_list: list[int]) -> dict[str,int]:
    if len(str_list) != len(int_list) or not str_list or not int_list:
        return {}
    else:
        ret_dict = {}
        for i in range(len(str_list)):
            ret_dict[str_list[i]] = int_list[i]
        return ret_dict
    
    
