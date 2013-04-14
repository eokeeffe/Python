import os
import time
import tempfile

temp = tempfile.NamedTemporaryFile()
try:
	print 'temp:', temp
	print 'temp.name:', temp.name
finally:
	# Automatically cleans up the file
	time.sleep(15)
	temp.close()

print 'Exists after close:', os.path.exists(temp.name)