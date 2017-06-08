#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import re
import sys
import os
import time

params = sys.argv

if not len(params) == 3:
    exit('检查参数！')

seqFile = params[1]
seqFile = './' + seqFile
detailFile = params[2]
detailFile = './' + detailFile

result_dir = './RESULTS'
if not os.path.exists(result_dir):
    os.makedirs(result_dir)

def getSeqDetails(file):
    seq_details = {}
    with open(file, 'r') as f:
        for line in f:
            if line.find('>') == 0:
                seq_code = line.replace('>', '').rstrip(' \t\n\r')
                seq_detail = next(f)
                seq_details[seq_code] = seq_detail
    return seq_details


def writeResult(exampleName, seqCode, seqDetail):
    file = result_dir + '/%s.txt' % exampleName
    with open(file, 'a') as f:
        f.write('>' + seqCode + '\n')
        f.write(seqDetail)


print('开始处理..............')
start_time = time.time()

seq_details = getSeqDetails(detailFile)
with open(seqFile) as f:
    for line in f:
        row = re.split(r'\t+', line.rstrip(' \t\n\r'))
        example_name = row[0]
        seq_codes = row[1:]

        for seq_code in seq_codes:
            seq_detail = seq_details.get(seq_code, '')
            writeResult(example_name, seq_code, seq_detail)

print('处理完毕，耗时%s秒' % (time.time() - start_time))