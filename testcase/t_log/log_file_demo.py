import logging

#输出控制台
#1、设置logger名称
logger = logging.getLogger("log_file_demo")
#2、设置log级别
logger.setLevel(logging.INFO)
#3、创建handler
fh_stream = logging.StreamHandler()
#写入文件
fh_file = logging.FileHandler("./test.log")
#4、设置日志级别
fh_stream.setLevel(logging.DEBUG)
fh_file.setLevel(logging.WARNING)
#5、定义输出格式
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s ')
fh_stream.setFormatter(formatter)
fh_file.setFormatter(formatter)
#6、添加handler
logger.addHandler(fh_stream)
logger.addHandler(fh_file)
#7、运行输出

logger.info("this is a info")
logger.debug("this is a debug")
logger.warning("this is a warning")