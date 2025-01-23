import logging

#Logging
'''1- logging helps to achive observablility of the performance and security.
   2- Errors can be found easily andsecurity and performance monitoring.
'''

# LogginG level--> which will define the level of logging
# There are  6 Logging levels segrigated based on the critical issue
"""
1 CRITICAL
2 ERROR
3 WARNING
4 INFO
5 DEBUG
6 NOTSET
"""
# logging.basicConfig(level=logging.INFO) # To show and  set basic config error msg
logging.basicConfig(level=logging.INFO,format=f"%(asctime)s::%(levelname)s::%(message)s") # To change the format of the msg shown
logging.info('Hello Venky')

