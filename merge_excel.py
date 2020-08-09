#!/usr/bin/env python3
#coding:utf-8
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#作者：lzjgf
#博客：
#文件：
#日期：
#备注：
#功能：
#版本：
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import pandas as pd
import os,sys

def merge_csv(file_list,new_file_name):
	if len(file_list)==0:
		print("文件夹内没有csv文件。")
	else:
		print("正在读取第1个文件。")
		df = pd.read_csv(file_list[0], header=0, encoding="gbk", low_memory=False )
		# df.to_csv(os.path.join(filepath, new_file_name) , index=False, encoding="gbk" )
		for i in range(1,len(file_list)):
			print(f"正在读取第{i+1}个文件。")
			df1 = pd.read_csv(file_list[i], header=0,encoding="gbk",low_memory=False )
			# header=None表示原始文件数据没有列索引，这样的话read_csv会自动加上列索引
			df = df.append(df1)
		print("开始输出合并后的文件。")
		df.to_csv(new_file_name, index=False,encoding="gbk")
			# header=0表示不保留列名，index=False表示不保留行索引，
			# mode='a'表示附加方式写入，文件原有内容不会被清除
		print("合并完成，文件名为：",new_file_name)

def merge_excel(file_list,new_file_name):

	if len(file_list)==0:
		print("文件夹内没有xls文件。")
	else:
		df = pd.DataFrame()
		for i,file in enumerate(file_list):
			print(f"正在读取第{i+1}个文件。")
			df1 = pd.read_excel(file, header=0,encoding="gbk" )
			# header=None表示原始文件数据没有列索引，这样的话read_csv会自动加上列索引
			df = df.append(df1)
		print("开始输出合并后的文件。")
		print(df)
		df.to_excel(new_file_name, index=False,encoding="gbk")
			# header=0表示不保留列名，index=False表示不保留行索引，
		print("合并完成，文件名为：",new_file_name)



def main():
	os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))
	print("功能：合并文件夹下csv，xls或xlsx文件。")
	print("注意：这些文件的格式(列名)须相同。")
	ext = input("请输入需要合并文件的后缀csv ， xls 还是 xlsx，\n默认为 xlsx：").strip()
	if ext not in ["csv", 'xls']:
		ext = "xlsx"
	print(f'开始合并{ext}文件。')
	outfile_name = "merge_file."+ext
	try :
		os.remove(outfile_name)
	except Exception as _:
		pass
	file_list = os.listdir()
	csv_list = list()
	xls_list = list()
	xlsx_list = list()
	for file in file_list:
		if file.endswith('.csv'):
			csv_list.append(file)
		elif file.endswith('.xls'):
			xls_list.append(file)
		elif file.endswith('.xlsx'):
			xlsx_list.append(file)

	if ext == "csv":
		merge_csv(csv_list,outfile_name)
	elif ext == 'xls':
		merge_excel(xls_list,outfile_name)
	else:
		merge_excel(xlsx_list,outfile_name)
	input("按任意键退出！")
if __name__ == '__main__':
    main()



