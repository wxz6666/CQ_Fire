import pandas as pd

# 读取包含微博用户名的CSV文件
csv_file_with_usernames = r"D:\wxzi\pythonProject\Fire of CQ\Fire of CQ\数据描述\县级媒体.csv"  # 替换为你的CSV文件名
df_usernames = pd.read_csv(csv_file_with_usernames,encoding='gbk')

# 读取另一个包含数据的CSV文件
csv_file_with_data = (r"D:\wxzi\pythonProject"
                      r"\Fire of CQ\Fire of CQ\data_cleannig\filtered_data_blue.csv")  # 替换为你的CSV文件名
df_data = pd.read_csv(csv_file_with_data)

# 提取微博用户名这一列的值
usernames = df_usernames['微博用户名']

# 使用isin方法过滤包含这些微博用户名的行
filtered_data = df_data[df_data['微博用户名'].isin(usernames)]

# 保存提取出来的数据到新的CSV文件
output_csv_file = "提取的数据_县级媒体.csv"  # 替换为你的输出文件名
filtered_data.to_csv(output_csv_file, index=False)

print(f"已将匹配的数据保存到 {output_csv_file}")
