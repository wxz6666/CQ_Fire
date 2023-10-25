import pandas as pd
import matplotlib.pyplot as plt

# 请替换 'your_data.csv' 为你的CSV文件路径
df = pd.read_csv(r'D:\wxzi\pythonProject\Fire of CQ\Fire of CQ\可视化\干净的数据集\合并后数据.csv',encoding='gb18030')

# 确保数据包括一个日期/时间列和一个认证标志列
# 假设日期/时间列名为 '发布时间'，认证标志列名为 '认证标志'

# 将日期时间列解析为指定的格式
df['发布时间'] = pd.to_datetime(df['发布时间'], format='%m月%d日 %H:%M')

# 继续执行后续的代码

# 使用groupby分组数据，按照认证标志分组
grouped = df.groupby('认证标志')

# 创建一个图形和坐标轴
plt.figure(figsize=(10, 6))
# # 指定新字体
# plt.rcParams['font.sans-serif'] = 'WenQuanYi Micro Hei'  # 这里使用了文泉驿微米黑字体
# 继续绘制图形
# 对每个认证标志绘制时间序列图
for name, group in grouped:
    if name == 'yellow':
        color = 'yellow'
    elif name == 'blue':
        color = 'blue'
    else:
        color = 'gold'
    plt.plot(group['发布时间'], group.index, label=name, color=color)


# 添加标题和标签
plt.title('Time series diagram of different authentication marks')
plt.xlabel('Release time')
plt.ylabel('Data point index')

# 添加图例
plt.legend()

# 显示图形
plt.tight_layout()
plt.show()
