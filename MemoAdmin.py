# /usr/bin/env Python
# -*- coding=utf-8 -*-
# Memo管理
# 

import random
import json
import pickle
import UserAdmin
import LogAdmin
import ConfAdmin
import Memo


class MemoAdmin():
	''' 备忘录管理 '''
	def __init__(self):
		''' 初始化 '''
		self._ca = ConfAdmin.ConfAdmin()
		user_file = self._ca.get_user_file()
		self._ua = UserAdmin.UserAdmin(user_file)
		self.logger = LogAdmin.getLogger("MemoAdmin")

		self._memo_oper = {'a' : "add_memo",
		'm' : 'modify_memo',
		's' : 'show_memo',
		'd' : "del_memo",
		'p' : 'export_memo',
		'q' : 'quit'}

		
	def login(self, user, pwd):
		''' 用户登录 '''
		self.logger.info("User[%s] Login", user)
		ret = self._ua.login(user, pwd)
		if ret['ret']:
			self.datainfo = self._ca.get_data_info(user)
			self._memo = Memo.Memo(self.datainfo['file'], self.datainfo['type'])
			# self.help()
		return ret


	def quit(self):
		''' 用户退出 '''
		pass
		
		
	def register(self, user, pwd):
		''' 注册新用户 '''
		if self._ua.register(user, pwd):
			type = ['json', "pkl"]
			random_value = random.randint(0, 1)
			file = user + "." + type[random_value]
			self._ca.add_new_user(user, file, type[random_value])
			return True

		return False

	def help(self):
		''' help function '''
		print("请输入要执行的操作: ")
		print("\t a: 添加一条记录")
		print("\t m: 修改一条记录")
		print("\t d: 删除一条记录")
		print("\t s: 显示所有记录")
		print("\t q: 退出")

	def run(self, oper_type):
		if oper_type not in self._memo_oper.keys():
			self.logger.error("Error Input")
			return
		if hasattr(self, self._memo_oper[oper_type]):
			getattr(self, self._memo_oper[oper_type])()
		
	def add_memo(self):
		''' add '''
		time = input("Please Input Time: ");
		thing = input("Please Input Thing: ");
		usetime = input("Please Input Usetime: ");
		self._memo.add_memo(time, thing, usetime)

		
	def modify_memo(self):
		''' modify '''
		self._memo.show_memo()
		
		id = input("Please Input Id: ")
		while True:
			if self._memo.check_memo_id(id):
				break
			self.logger.error("Id Not Exist!")
			id = input("Please Input Id[q:exit]: ")
			id = id.strip().lower()
			if id == 'q':
				return
		time = input("Please Input Time: ");
		thing = input("Please Input Thing: ");
		usetime = input("Please Input Usetime: ");
		self._memo.modify_memo(id, time, thing, usetime)

		
	def show_memo(self):
		''' show '''
		self._memo.show_memo()

		
	def del_memo(self):
		''' del '''
		id = input("Please Input Id: ")
		while True:
			if self._memo.check_memo_id(id):
				break
			self.logger.error("Id Not Exist!")
			id = input("Please Input ID[q: exit]: ")
			id = id.strip().lower()
			if id == 'q':
				return
		self._memo.del_memo(id)
	
	def export_memo(self):
		''' 导出pdf '''
		self._memo.export_memo()
		pass
		
	
		
def main():
	ma = MemoAdmin()
	user = input("Please Input UserName: ")
	pwd = input("Please Input Password: ")
	
	ret = ma.login(user, pwd)
	if not ret['ret']:
		print("Login Failed.")
		v = input("Do You Want Register[y/n]: ")
		v = v.strip().lower()
		if v == 'y':
			user = input("Please Input UserName: ")
			pwd = input("Please Input Password: ")
			pwd2 = input("Please Input Password Again: ")
			if pwd != pwd2:
				print("Password No Same")
				return
			ma.register(user, pwd)
		else:
			return
	while True:
		ma.help()
		type = input()
		type = type.strip().lower()
		if type == 'q':
			return
		ma.run(type)
	
if __name__ == "__main__":
	main()
	