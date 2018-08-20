# /usr/bin/env Python
# -*- coding=utf-8 -*-
# logging


import logging
import sys


def getLogger(modules_name="debug", filename="memo.log"):
	logger = logging.getLogger(modules_name)
		
	formatter = logging.Formatter('[%(asctime)s %(filename)s:%(lineno)d]: %(message)s')
	
	# 文件Handler
	file_handler = logging.FileHandler(filename)
	file_handler.setFormatter(formatter)
	
	# modules_filename = modules_name + ".log"
	# print(modules_filename)
	# file_handler2 = logging.FileHandler(modules_filename)
	# file_handler2.setFormatter(formatter)
	
	console_handler = logging.StreamHandler()
	console_handler.setFormatter(formatter);
	
	logger.addHandler(file_handler)
	logger.addHandler(console_handler);
	# logger.addHandler(file_handler2);
	
	logger.setLevel(logging.INFO)
	
	return logger
	


def main():
	log = getLogger()
	log.debug("Hello World")
	a = 3
	b = 4
	log.info("{} + {} = {}".format(a, b, a + b))
	
	log.warning("Exit")
	
	log2 = getLogger("hello")
	log2.info("QQ")
	log2.info(f"{a} * {b} = {a * b}")
	
if __name__ == "__main__":
	main()
