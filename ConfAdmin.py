# /usr/bin/env Python
# -*- coding=utf-8 -*-
# 配置管理
#
''' 
配置文件：
[DEFAULT]
user_file=user.pkl
save_user=yes # 是否保存用户名
last_user=zhangshan # 最后登录的用户
last_login_time=xxxx # 最后登录的时间
[zhangshan]
file=zhangshan.pkl
type=pkl
[lisi]
file=lisi.pkl
type=json

'''
import os
import configparser
import LogAdmin

# TODO: 
# 	1.文件不存在的处理
# 	2.增加自动登录管理，如：保存用户名，最后登录的用户，最后登录的时间[用户一段时间不登录的话，就自动退出]
class ConfAdmin():
	def __init__(self, conf_file="memo.conf"):
		self.logger = LogAdmin.getLogger("ConfAdmin")
		self._conf_file = conf_file
		self.load(conf_file)
		
	def get_user_file(self):
		return self.conf.get("DEFAULT", "user_file")
	
	def get_data_info(self, user):
		data = {}
		try:
			data['file'] = self.conf.get(user, "file")
			data['type'] = self.conf.get(user, 'type')
			self.logger.info(data)
		except Exception as e:
			self.logger.error("Get [%s] Failed[%s]", user, e)
			
		return data
	
	def add_new_user(self, user, filename, type):
		''' 添加一条新记录 '''
		self.logger.info("user = %s, filename = %s, type = %s", user, filename, type);
		try:
			self.conf.add_section(user)
			self.conf.set(user, "file", filename)
			self.conf.set(user, 'type', type)
			self.save(self._conf_file)
		except Exception as e:
			self.logger.error("Add Failed[%s]", e)
		
	def load(self, conf_file):
		'''载入配置文件'''
		self.logger.info("Load File %s", conf_file)
		if not os.path.exists(conf_file):
			with open(conf_file, "w") as f:
				f.write("[DEFAULT]\nuser_file=user.pkl\n")
		try:			
			self.conf = configparser.ConfigParser()
			self.conf.read(conf_file)
			return self.conf
		except Exception as e:
			self.logger.error("Load File Failed[%s]", e)

	def save(self, conf_file):
		'''保存配置文件'''
		try:
			self.conf.write(open(conf_file, "w"))
		except Exception as e:
			self.logger.error("Save File Failed[%s]", e)


def main():
	ca = ConfAdmin()
	f = ca.get_user_file()
	print(f)
	data = ca.get_data_info("zdy")
	print(data)
	data = ca.get_data_info("hb")
	
	ca.add_new_user("wangwu", "wangwu.pkl", "pkl")
	ca.add_new_user("xiaoliu", "xiaoliu.json", "json")
	
	
if __name__ == "__main__":
	main()
		
	
	