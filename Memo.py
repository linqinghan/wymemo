# /usr/bin/env Python
# -*- coding=utf-8 -*-
# Memo

import pickle
import json
import LogAdmin

'''
Memo内容：id:编号, time:要做的时间, thing:要做的事情, usetime: 大概需要花多少时间
[ {'id' : 1, 'time': '1.1', 'thing':"Hello World', 'usetime':'3'}
{'id' : 2, 'time': '2.2', 'thing':'do homework', 'usetime':'8'}
{'id' : 3, 'time': '3.3', 'thing':'runing', 'usetime':'6'} ]
'''
class Memo():
	''' Memo '''
	def __init__(self, filename, type):
		''' 初始化 '''
		self.filename = filename
		self.type = type
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
		
		self.memo_list = list()
		
		self.logger = LogAdmin.getLogger("Memo")
		
		self.load_memo(filename, type)
		
		
	def load_memo(self, filename, type):
		''' 载入memo '''
		self.logger.info("load_memo")
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
	
	def load_memo_pkl(self, filename):
		self.logger.info("Load Pkl File[%s]", filename)
		try:
			with open(filename, "rb") as f:
				self.memo_list = pickle.load(f)
		except Exception as e:
			self.logger.error("Load Pkl File Error[%s]", e)
		
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
	
	def save_memo_pkl(self, filename, memo_list):
		self.logger.info("Save Pkl File[%s]", filename)
		try:
			with open(filename, "wb") as f:
				pickle.dump(self.memo_list, f)
		except Exception as e:
			self.logger.error("Load Pkl File Error[%s]", e)
		

	def add_memo(self, time, thing, usetime):
		''' add '''
		self.logger.info("add_memo")
		pass
		
	def modify_memo(self, id, time, thing, usetime):
		''' modify '''
		self.logger.info("modify_memo")
		pass
		
	def show_memo(self):
		''' show '''
		self.logger.info("show_memo")
		for memo in self.memo_list:
			print(memo)
		
	def del_memo(self, id):
		''' del '''
		self.logger.info("del_memo")
		pass
	
	def export_memo(self):
		''' 导出pdf '''
		self.logger.info("export_memo")
		pass
		
		
def main():
	pass
	
if __name__ == "__main__":
	main()