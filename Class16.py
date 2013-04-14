"""
	Logging modules in python and how to use it
	
	format specifies
	-time
	-level of the error
	-message passed
	-s specifies a string format
	
"""
import logging

logging.basicConfig(level=logging.DEBUG,
	format='%(asctime)s:%(levelname)s:%(message)s',
	filename='myapp.log',
	filemode='w')

logging.log(50,"First Problem. You read this")
	
logging.warning("Watch out !")

logging.info("Try and see me")
