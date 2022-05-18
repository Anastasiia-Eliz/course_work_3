import logging

def create_logger():
	logger = logging.getLogger("basic")
	logger.setLevel("DEBUG")

	stream_handler = logging.StreamHandler()
	logger.addHandler(stream_handler)

	file_handler = logging.FileHandler("app/basic.txt")
	logger.addHandler(file_handler)

	formatter = logging.Formatter("%(levelname)s %(actime)s : %(message)s %(pathname)s >> %(funcName)s")
	stream_handler.setFormatter(formatter)

	return logger