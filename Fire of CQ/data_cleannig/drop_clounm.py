import pandas as pd

# 读取CSV文件
df = pd.read_csv(r'D:\wxzi\pythonProject\Fire of CQ\Fire of CQ\data'
                 r'_cleannig\new_file_34.csv',encoding='utf_8_sig')

# 用空字符串替换NaN值（可以根据需要选择其他替代值）
df['微博内容'] = df['微博内容'].fillna('')

# 删除包含特定文本的行
df = df[~df['微博内容'].str.contains('')]

# 保存修改后的数据到新的CSV文件
df.to_csv(r'D:\wxzi\pythonProject\Fire of CQ\Fire of CQ\data_cleannig\new_file_35.csv', index=False)
