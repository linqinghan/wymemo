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
		self._id = 0
		self._filename = filename
		self._type = type
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
		self.logger.info("load_memo[filename = %s, type = %s]", filename, type)
		for t in self._memo_type:
			if t['type'] == type and hasattr(self, t['load_func']):
				# self.logger.error("Find Type [%s]", type)
				getattr(self, t['load_func'])(filename)
				self._id = self.get_max_id(self.memo_list)
				self.logger.info(f"max_id = {self._id}")
				return True
		
		self.logger.error("Error File Type[%s]", type)
		return False
	
	def load_memo_json(self, filename):
		self.logger.info("Load Json File[%s]", filename)
		try:
			with open(filename, "r") as f:
				self.memo_list = json.load(f)
				# return self.get_max_id(self.memo_list)
		except Exception as e:
			self.logger.error("Load Json File Error[%s]", e)			


	def load_memo_pkl(self, filename):
		self.logger.info("Load Pkl File[%s]", filename)
		try:
			with open(filename, "rb") as f:
				self.memo_list = pickle.load(f)
		except Exception as e:
			self.logger.error("Load Pkl File Error[%s]", e)
		
	def save_memo(self, filename, type, memo_list):
		''' save memo '''
		for t in self._memo_type:
			if t['type'] == type and hasattr(self, t["save_func"]):
				getattr(self, t["save_func"])(filename, memo_list)
				return True
		
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
	
	def get_max_id(self, memo_list):
		''' '''
		max_id = 0
		for memo in memo_list:
			if int(memo['id']) > max_id:
				max_id = int(memo['id'])

		return max_id

	def add_memo(self, time, thing, usetime):
		''' add '''
		self.logger.info(f"add_memo [id = {self._id}]")
		self._id += 1
		self.logger.info(f"id = {self._id}")
		item = {}
		item['id'] = self._id
		item['time'] = time
		item['thing'] = thing
		item['usetime'] = usetime

		self.memo_list.append(item)
		self.show_memo()
		self.save_memo(self._filename, self._type, self.memo_list)


	def modify_memo(self, id, time, thing, usetime):
		''' modify '''
		self.logger.info("modify_memo")
		index = 0
		for memo in self.memo_list:
			if memo['id'] == id:
				self.logger.info(memo)
				index = self.memo_list.index(memo)
				self.memo_list[index]['time'] = time
				self.memo_list[index]['thing'] = thing
				self.memo_list[index]['usetime'] = usetime
				self.show_memo()
				self.save_memo(self._filename, self._type, self.memo_list)
		pass
		
	def show_memo(self):
		''' show '''
		self.logger.info("show_memo")
		print(" Memo List ".center(80, "*"))
		for memo in self.memo_list:
			print(memo)
		print("*" * 80, "\n")
		
	def del_memo(self, id):
		''' del '''
		self.logger.info("del_memo")
		for memo in self.memo_list:
			if memo['id'] == id:
				self.logger.info(memo)
				self.memo_list.remove(memo)
				self.save_memo(self._filename, self._type, self.memo_list)
		self.show_memo()
	
	def export_memo(self):
		''' 导出pdf '''
		self.logger.info("export_memo")
		pass
		
		
def main():
	m = Memo("zdy.pkl", "pkl")
	m.add_memo("1.1", "Hello Word", 1)
	m.add_memo("2.2", "Running", 2)
	m.add_memo("3.3", "GoHome", 3)
	
	m.modify_memo(1, "5.5", "Hello world", 2)

	m.show_memo()

	m.del_memo(1)

if __name__ == "__main__":
	main()