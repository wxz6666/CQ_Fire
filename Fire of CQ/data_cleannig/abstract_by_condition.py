import pandas as pd
# 读取 CSV 文件
df = pd.read_csv(r'D:\wxzi\pythonProject\Fire of CQ\Fire of CQ\可视化\干净的数据集\合并后数据.csv',
                 encoding='gb18030')
# 找到包含 "blue" 的行 gb18030 utf_8_sig
column_name = '认证标志'
rows_with_blue = df[df[column_name].str.contains('blue', na=False)]
# 抽取出包含 "blue" 的行
filtered_df = rows_with_blue.drop(columns=['认证标志'])
# 保存抽取出的行到一个新的 CSV 文件
filtered_df.to_csv(r'D:\wxzi\pythonProject\Fire of CQ\Fire of CQ\可视化\blue合集\filtered_data_blue.csv', index=False)