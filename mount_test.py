import imagemounter
files = ["/home/jade/Documents/Recover.E01", "/home/jade/Documents/Recover.E02"]
parser = imagemounter.ImageParser(files, None, True)
for volume in parser.init():
	print("test")