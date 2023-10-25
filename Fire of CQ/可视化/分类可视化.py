import pandas as pd
import matplotlib.pyplot as plt

# 读取包含"发布时间"列的CSV文件
csv_file = r"D:\wxzi\pythonProject\Fire of CQ\Fire of CQ\数据描述\提取的数据_县级媒体.csv"  # 替换为你的CSV文件名
df = pd.read_csv(csv_file,encoding='utf-8') #utf-8 gbk

# 解析自定义时间格式为日期时间对象
df['发布时间'] = pd.to_datetime("2022年" + df['发布时间'], format='%Y年%m月%d日 %H:%M')

# 提取日期和小时
df['日期'] = df['发布时间'].dt.date
df['小时'] = df['发布时间'].dt.hour

# 以日期和小时为间隔对数据进行分组
hourly_data = df.groupby(['日期', '小时' ]).size()

# 创建折线图
plt.figure(figsize=(14, 6))
hourly_data.plot(kind='line', marker='o')
plt.title('Daily 24-hour time distribution line chart')
plt.xlabel('Date and hour')
plt.ylabel('Number')
plt.grid(True)


# 显示图表
plt.show()
