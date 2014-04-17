from path import path
d = path(DIRECTORY)
files = d.walkfiles("*.pyc")
for file in files:
	file.remove()
	print "Removed {} file".format(file)
