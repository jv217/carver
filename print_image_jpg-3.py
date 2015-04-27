#!/usr/bin/python

# Import required libraries from Python standard libraries
import sys       # System-specific parameters and functions
import binascii  # Convert between binary and ASCII

# Argument 0 - script path
# Argument 1 - dd file

user_arguments = sys.argv

# Check if number of user arguments is less than two, if true 
# print an error and exit, otherwise continue the program 
# execution.

if len(user_arguments) < 2: 
	print("error: missing arugment (file point)\n\nusage: print_image.py <dd file>")
	exit()

# Take first user argument and assign it to a readable variable name
dd_file = sys.argv[1]

# Set start and end range (in bytes) where to search for media files
start = 0
end = 1 * 1024 * 1024 * 1024 # 1 gb

# Set chunk size (in bytes) to specify how many bytes we want to read
# at a time
chunk_size = 8192

# Set default values
jpg_start = 0

with open(dd_file) as file:
	file.seek(start)
	while file.tell() < end:
		bytes = file.read(chunk_size)
		for index in range(0, chunk_size - 3):

			# Match the beginning of JPG
			if bytes[index] == chr(0xFF) and bytes[index+1] == chr(0xD8):
				address = file.tell() - chunk_size + index
				jpg_start = address

			# Match the end of JPG
			elif bytes[index] == chr(0xFF) and bytes[index+1] == chr(0xE0) and bytes[index+2] == chr(0x00) and bytes[index+3] == chr(0x10):
				if jpg_start == 0
					continue				
				address = file.tell() - chunk_size + index
				jpg_end = address + 7
				jpg_size = jpg_end - jpg_start
				print("found jpg at " + str(address) + ", exporting ...")
				with open(dd_file) as innerFile:
					innerFile.seek(jpg_start)
					jpg_bytes = innerFile.read(jpg_size)
					with open("output/jpg_" + str(index) + ".jpg", "wb") as output:
						output.write(jpg_bytes)
				print("[done]")
				