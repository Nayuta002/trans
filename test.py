import os
import re

path = r'G:\轻小说\回復術士のやり直し～即死魔法とスキルコピーの超越ヒール～\简体\00080_第九章：回復術士は新たな道を示す'


# 遍历文件夹
def walkFile(file):
    file_paths = []
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # print(f'root:{root}')
        # print(f'dirs:{dirs}')
        # print(f'files:{files}')

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


def del_file(file_paths):
    for file in file_paths:
        if str(file).endswith('(1).txt'):
            # 删除
            print(file)
            os.remove(file)

    print('ok')


def rename_txt(file_paths):
    for file in file_paths:
        if str(file).endswith('.txt'):
            temp = str(file).rsplit('\\', 1)
            root = temp[0]
            file_txt = temp[1]
            # print(file_txt)
        else:
            continue

        data = re.search('^[0-9]{5}_', file_txt)
        if not data:
            new_name = split_name(file_txt)
            print(new_name)
            os.rename(os.path.join(root, file_txt),os.path.join(root, new_name))
        else:
            # print(data.group())
            pass

def split_name(name):
    name_dict = {
        '序幕': '00000_',
        '第一話': '00010_',
        '第二話': '00020_',
        '第三話': '00030_',
        '第四話': '00040_',
        '第五話': '00050_',
        '第六話': '00060_',
        '第七話': '00070_',
        '第八話': '00080_',
        '第九話': '00090_',
        '第十話': '00100_',
        '第十一話': '00110_',
        '第十二話': '00120_',
        '第十三話': '00130_',
        '第十四話': '00140_',
        '第十五話': '00150_',
        '第十六話': '00160_',
        '第十七話': '00170_',
        '第十八話': '00180_',
        '第十九話': '00190_',
        '第二十話': '00200_',
        '第二十一話': '00210_',
        '第二十二話': '00220_',
        '第二十三話': '00230_',
        '第二十四話': '00240_',
        '第二十五話': '00250_',
        '第二十六話': '00260_',
        '第二十七話': '00270_',
        '第二十八話': '00280_',
        '第二十九話': '00290_',
        '第三十話': '00300_'
    }
    try:
        temp = str(name).split('：')
        number = temp[0]
        print(number)
        name = name_dict[number] + name
    except:
        pass
    return name


file_paths = walkFile(path)
for i in file_paths:
    data = i.rsplit('\\',1)[1]
    print(data)
# rename_txt(file_paths)
