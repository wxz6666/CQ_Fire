import pandas as pd
from collections import Counter

data = pd.read_csv(r'D:\wxzi\pythonProject\Fire of CQ\Fire of CQ\可视化\blue合集\filtered_data_blue.csv',
                   encoding='utf_8_sig')
# 提取一列，例如第一列 gb18030 utf_8_sig
column = data['微博用户名']
# 使用 Counter 找到出现次数最多的值
most_common = Counter(column)
# 打印出现次数最多的前位值及其出现次数
for value, count in most_common.most_common(100):
   print("值：", value, "出现次数：", count)

# df = pd.DataFrame({'Value': most_common.most_common(100)[1], 'Count': most_common.most_common(100)[0]})
df = pd.DataFrame(most_common.most_common(10000))
df.to_csv(r'D:\wxzi\pythonProject\Fire of CQ\Fire of CQ\可视化\blue合集\most_common_values_blue.csv', index=False)