import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 读取CSV文件并加载数据
df = pd.read_csv(r'D:\wxzi\pythonProject\Fire of CQ\Fire of CQ\可视化\干净的数据集\合并后数据.csv',encoding='gb18030')  # 替换为你的CSV文件路径

# 将发布时间列转换为日期时间对象
df['发布时间'] = pd.to_datetime(df['发布时间'], format='%m月%d日 %H:%M')

# 创建一个新的列，表示发布时间的日期
df['发布日期'] = df['发布时间'].dt.date

# 获取不同的认证标志
categories = df['认证标志'].unique()

# 创建一个图形和坐标轴
plt.figure(figsize=(10, 6))

# 遍历每个认证标志并绘制时间序列图
for category in categories:
    subset = df[df['认证标志'] == category]
    subset = subset.groupby('发布日期').size().reset_index(name='Counts')

    if category == 'yellow':
        color = 'yellow'
    elif category == 'blue':
        color = 'blue'
    else:
        color = 'gold'

    plt.plot(subset['发布日期'], subset['Counts'], label=category, color=color)
    # 在折线上标注数量
    for x, y in zip(subset['发布日期'], subset['Counts']):
        plt.text(x, y, str(y), ha='center', va='bottom', fontsize=10, color='black')

# 添加标题和标签
plt.title('Time series diagram of different authentication marks', fontsize=14)
plt.xlabel('Release time', fontsize=12)
plt.ylabel('Daily data volume', fontsize=12)

# 添加图例
plt.legend()

# 设置x轴标签密度，显示更多日期
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))  # 设置日期标签密度
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

# 旋转x轴标签以避免重叠
plt.xticks(rotation=45)
# 格式化x轴标签，去掉年份
ax = plt.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
# 显示图形
plt.tight_layout()
plt.show()
