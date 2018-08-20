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

		self._memo_oper = {'add' : "add_memo",
		'modify' : 'modify_memo',
		'show' : 'show_memo',
		'del' : "del_memo",
		'export' : 'export_memo'}

		
	def login(self, user, pwd):
		''' 用户登录 '''
		self.logger.info("User[%s] Login", user)
		ret = self._ua.login(user, pwd)
		if ret['ret']:
			self.datainfo = self._ca.get_data_info(user)
			self._memo = Memo.Memo(self.datainfo['file'], self.datainfo['type'])
			self.help()
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
	