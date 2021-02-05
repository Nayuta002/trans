from zhtools.langconv import *
import sys
import os
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
import threading

root_path = r'G:\轻小说\回復術士のやり直し～即死魔法とスキルコピーの超越ヒール～\繁体'

print(sys.version)
print(sys.version_info)

# 转换繁体到简体
def cht_to_chs(line):
    line = Converter('zh-hans').convert(line)
    line.encode('utf-8')
    return line

# 转换简体到繁体
def chs_to_cht(line):
    line = Converter('zh-hant').convert(line)
    line.encode('utf-8')
    return line


# 遍历文件夹
def walkFile(file):
    file_paths = []
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        for f in files:
            file_path1 = os.path.join(root, f)
            # print(file_path1)
            file_paths.append(file_path1)
        # 遍历所有的文件夹
        # for d in dirs:
        #     print(os.path.join(root, d))
        # print('\n')
    return file_paths

def read_txt(file):
    with open(file,'r',encoding='utf-8') as f:
        data = f.read()
    txtsimple = cht_to_chs(data)
    # print(txtsimple)
    return txtsimple




def write_txt(file):
    if str(file).endswith('.txt'):
        txtsimple = read_txt(file)
        file = str(file).replace('繁体','简体')
        # print(file)
        try:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(txtsimple)
            print(file + 'is ok !!!')
        except Exception as e :
            print(file + 'is error !!! :' + str(e))

    else:
        pass



 # 线程池
def ThreadPool(starts_url):
    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = []
        for url in starts_url:
            future = executor.submit(write_txt, url)
            futures.append(future)
    # 等待所有的线程完成才进行后续的逻辑
    wait(futures, return_when=ALL_COMPLETED)




file_paths = walkFile(root_path)
print(file_paths)
ThreadPool(file_paths)
print('all is ok!!!!')

# path = 'G:\\轻小说\\回復術士のやり直し～即死魔法とスキルコピーの超越ヒール～\\繁体\\回复术士1-9卷第7话.txt'
# read_txt(path)