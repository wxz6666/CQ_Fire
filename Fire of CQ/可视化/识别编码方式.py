import chardet

def detect_csv_encoding(file_path):
    try:
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())
        return result['encoding']
    except Exception as e:
        print(f"无法识别编码方式: {e}")
        return None

# 用法示例
csv_file_path = r'D:\wxzi\pythonProject\Fire of CQ\Fire of CQ\可视化\干净的数据集\8月17日数据.csv'
encoding = detect_csv_encoding(csv_file_path)
if encoding:
    print(f"CSV文件的编码方式为: {encoding}")
else:
    print("无法识别CSV文件的编码方式")

