# /usr/bin/env Python
# -*- coding=utf-8 -*-
# User Admin
#
import pickle
import LogAdmin

class UserAdmin():
	'''用户管理模块，包括用户登录和注册'''
	def __init__(self, filename="user.pkl"):
		'''初始化'''
		self.logger = LogAdmin.getLogger("UserAdmin")
		self._filename = filename
		self.load(filename)
		
	def login(self, user, pwd):
		'''
		用户登录
		'''
		result = {'ret' : True, "msg": "Login Ok"}
		
		ret = self.check_password(user, pwd)
		if ret == -1:
			result['ret'] = False
			result['msg'] = "Password is Wrong"
			self.logger.error("Password Is Wrong")
			return result
		elif ret == -2:
			result['ret'] = False
			result['msg'] = "User Not Found"
			self.logger.error("User Not Found")
			return result
			
		self.logger.info("Login Ok")
		return result
		
	def register(self, user, pwd):
		'''
		注册新用户
		'''
		if self.check_user(user):
			self.logger.error("User Has Register")
			return False
		if not self.check_password_strength(pwd):
			return False

		u = {}
		u['user'] = user
		u['pwd'] = pwd
		self._userlist.append(u)
		
		self.save(self._filename)
		return True
		
	def check_user(self, user):
		'''检查用户名'''
		for u in self._userlist:
			if u['user'] == user:
				return True
		
		return False
		
	def check_password(self, user, pwd):
		'''检查密码'''
		for u in self._userlist:
			if u['user'] == user and u['pwd'] == pwd:
				return 0
			elif u['user'] == user and u['pwd'] != pwd:
				# self.logger.error("Password Error")
				return -1
				
		# self.logger.error("User Not Found")
		return -2
	
	def check_password_strength(self, pwd):
		'''
		检查密码强度
		TODO: 使用正则表达式，保证密码强度。有大小字母有数字，长度8-16之间
		'''
		# re_pwd = "" #
		return True

	def load(self, filename):
		'''载入用户信息'''
		try:
			with open(filename, "rb") as f:
				# self._userlist = f.read()
				self._userlist = pickle.load(f)
			return self._userlist
		except Exception as e:
			# print(e)
			self.logger.error(e)
			
		self._userlist = []
		return self._userlist
		
	def save(self, filename):
		'''保存用户信息'''
		self.logger.info(self._userlist)
		try:
			with open(filename, 'wb') as f:
				pickle.dump(self._userlist, f)
		except Exception as e:
			# print(e)
			self.logger.error(e)
		
def main():
	us = UserAdmin()
	ret = us.login("hb", "hb123")
	# print(ret['msg'])
	ret = us.register("hb", "hb456")
	# print(ret['msg'])
		
	
	
if __name__ == "__main__":
	main()
