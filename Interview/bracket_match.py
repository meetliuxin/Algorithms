#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: "liuxin"
# Date: 2018-7-12


def bracket_match(one_str):
    '''''
    括号匹配
    '''
    tmp_list = []
    open_bracket_list = ['(', '[', '{', '<', '《']
    close_bracket_list = [')', ']', '}', '>', '》']
    one_str_list = list(one_str)
    length = len(one_str_list)
    set_list = list(set(one_str_list))
    num_list = [one_str_list.count(one) for one in set_list]
    if one_str[0] in close_bracket_list:
        return False
    elif length % 2 != 0:
        return False
    elif len(set_list) % 2 != 0:
        return False
    else:
        for i in range(length):
            if one_str[i] in open_bracket_list:
                tmp_list.append(one_str[i])
            elif one_str[i] in close_bracket_list:
                if close_bracket_list.index(one_str[i]) == open_bracket_list.index(tmp_list[-1]):
                    tmp_list.pop()
                else:
                    return False
                    break
    return True


if __name__ == '__main__':
    one_str_list = ['({})', '({[<《》>]})', '[(]){}', '{{{{{{', '([{}])', '}{[()]']
    for one_str in one_str_list:
        if bracket_match(one_str):
            print(one_str, '正确')
        else:
            print(one_str, '错误')

    tmp = '{}[{()()[]<{{[[[[(())()()(){}[]{}[]()<>]]]]}}>}]'
    print(bracket_match(tmp))