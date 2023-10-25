import csv

# 打开txt文档并读取内容
with open(r'D:\wxzi\pythonProject\Fire of CQ\Fire of CQ\数据描述\县级媒体.txt', 'r', encoding='utf-8') as txt_file:
    content = txt_file.read()

# 将文本内容按逗号分割成名词列表
nouns = content.split('、')

# 创建CSV文件并写入名词列表
with open('县级媒体.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    for noun in nouns:
        writer.writerow([noun.strip()])

print('CSV文件创建完成')
