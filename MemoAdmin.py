# /usr/bin/env Python
# -*- coding=utf-8 -*-
# Memo管理
# 

import json
import pickle
import UserAdmin
import LogAdmin
import ConfAdmin



class MemoAdmin():
	''' 备忘录管理 '''
	def __init__(self):
		''' 初始化 '''
		self._ca = ConfAdmin()
		user_file = self._ca.get_user_file()
		self._ua = UserAdmin(user_file)
		self.logger = LogAdmin.getLogger("MemoAdmin")
		self._memo_type = [{'type' : 'json', 
			'load_func' : 'load_memo_json',
			'save_func' : 'save_memo_json'},
			{'type' : 'pkl',
			'load_func' : 'load_memo_pkl',
			'save_func' : 'save_memo_pkl'}]
		self._memo_oper = {'add' : "add_memo",
		'modify' : 'modify_memo',
		'show' : 'show_memo',
		'del' : "del_memo",
		'export' : 'export_memo'}
		
	def login(self, user, pwd):
		''' 用户登录 '''
		ret = self._ua.login(user, pwd)
		if ret['ret']:
			self.datainfo = self._ca.get_data_info()
			self.load_memo(self.datainfo['file'], self.datainfo['type'])
		return ret
		
	def load_memo(self, filename, type):
		''' 载入memo '''
		for t in self._memo_type:
			if t['type'] == type and hasattr(self, "load_func"):
				getattr(self, "load_func")(self, filename)
		
		self.logger.error("Error File Type[%s]", type)
		return False
	
	def load_memo_json(self, filename):
		self.logger.info("Load Json File[%s]", filename)
		try:
			with open(filename, "r") as f:
				self.memo_list = json.load(f)
		except Exception as e:
			self.logger.error("Load Json File Error[%s]", e)
		pass
	
	def load_memo_pkl(self, filename):
		self.logger.info("Load Pkl File[%s]", filename)
		try:
			with open(filename, "rb") as f:
				self.memo_list = pickle.load(f)
		except Exception as e:
			self.logger.error("Load Pkl File Error[%s]", e)
		pass
		
	def save_memo(self, filename, memo_list):
		''' save memo '''
		for t in self._memo_type:
			if t['type'] == type and hasattr(self, "save_func"):
				getattr(self, "save_func")(self, filename, memo_list)
		
		self.logger.error("Error File Type[%s]", type)
		return False
	
	def save_memo_json(self, filename, memo_list):
		self.logger.info("Save Json File[%s]", filename)
		try:
			with open(filename, "r") as f:
				json.dump(self.memo_list, f)
		except Exception as e:
			self.logger.error("Load Pkl File Error[%s]", e)
		pass
	
	def save_memo_pkl(self, filename, memo_list):
		self.logger.info("Save Pkl File[%s]", filename)
		try:
			with open(filename, "wb") as f:
				pickle.dump(self.memo_list, f)
		except Exception as e:
			self.logger.error("Load Pkl File Error[%s]", e)
		pass
		
	def quit(self):
		''' 用户退出 '''
		pass
		
		
	def register(self, user, pwd):
		''' 注册新用户 '''
		return self._ua.register(user, pwd)
		
	def add_memo(self):
		''' add '''
		pass
		
	def modify_memo(self):
		''' modify '''
		pass
		
	def show_memo(self):
		''' show '''
		pass
		
	def del_memo(self):
		''' del '''
		pass
	
	def export_memo(self):
		''' 导出pdf '''
		pass
		
	
		
def main():
	pass
	
if __name__ == "__main__":
	main()
	