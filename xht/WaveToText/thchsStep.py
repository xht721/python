import tensorflow as tf  # 0.12
import numpy as np
import os
from collections import Counter
import librosa  # https://github.com/librosa/librosa
 
# 训练样本路径
wav_path = 'D:\date' 
label_file = 'D:\date'
 
# 获得训练用的wav文件路径列表
def get_wav_files(wav_path=wav_path):
	wav_files = []
	for (dirpath, dirnames, filenames) in os.walk(wav_path):
		for filename in filenames:
			if filename.endswith('.wav') or filename.endswith('.WAV'):
				filename_path = os.sep.join([dirpath, filename])
				if os.stat(filename_path).st_size < 240000:  # 剔除掉一些小文件
					continue
				wav_files.append(filename_path)
	return wav_files
wav_files = get_wav_files()
def get_wav_lable(files=wav_files, label_file=label_file):
	label_list = []
	for wav_file in wav_files:
		with open(str(wav_file)+".trn",'r',encoding='utf8') as f:
			l = f.readline()
			label_list.append(l)
			# print(l)
	return wav_files,label_list

	
	# with open(label_file, 'r') as f:
	# 	for label in f:
	# 		label = label.strip('\n')
	# 		label_id = label.split(' ', 1)[0]
	# 		label_text = label.split(' ', 1)[1]
	# 		labels_dict[label_id] = label_text
 
	# labels = []
	# new_wav_files = []
	# for wav_file in wav_files:
	# 	wav_id = os.path.basename(wav_file).split('.')[0]
	# 	if wav_id in labels_dict:
	# 		labels.append(labels_dict[wav_id])
	# 		new_wav_files.append(wav_file)
 
	# return new_wav_files, labels

# get_wav_lable()
wav_files, labels = get_wav_lable(wav_files)
print(wav_files[1],labels[1])
