#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import os
import time

params = sys.argv

if not len(params) == 3:
    exit('检查参数！')

seq_file = params[1]
seq_file = './' + seq_file
detail_file = params[2]
detail_file = './' + detail_file

result_dir = './RESULTS'
if not os.path.exists(result_dir):
    os.makedirs(result_dir)


def get_seq_details(file):
    details = {}
    with open(file, 'r') as fl:
        temp_code = ''
        temp_detail = ''
        last_code = ''
        last_detail = ''
        for line in fl:
            if line.find('>') == 0:
                if temp_code and temp_detail:
                    details[temp_code] = temp_detail
                temp_code = line.replace('>', '').rstrip('\t\n\r')
                last_code = temp_code
                temp_detail = ''
            else:
                temp_detail += line.rstrip('\t\n\r')
                last_detail = temp_detail
        if last_code and last_detail:
            details[last_code] = last_detail
    return details


def write_result(name, code, detail):
    file = result_dir + '/%s.txt' % name
    with open(file, 'a') as fl:
        fl.write('>' + code + '\n')
        fl.write(detail + '\n')


print('开始处理..............')
start_time = time.time()

seq_details = get_seq_details(detail_file)
print(seq_details)
exit

with open(seq_file) as f:
    for seq_line in f:
        row = seq_line.split()
        example_name = row[0]
        seq_codes = row[1:]

        for seq_code in seq_codes:
            seq_detail = seq_details.get(seq_code, '')
            write_result(example_name, seq_code, seq_detail)

print('处理完毕，耗时%s秒' % (time.time() - start_time))
