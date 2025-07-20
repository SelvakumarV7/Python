# variables are otherwise known as temporary storage.
# Files or Database is the permanent storage.

# Opening a File:
# Before performing any operation (like read or write) on the file,
# first we have to open that file. For this we should use Python's
# inbuilt function open ( ) But at the time of open, we have to specify
# mode, which represents the purpose of opening file.

# f =  open (filename, mode)
# The allowed modes in Python are,

# r = open an existing file for read operation.
# The file pointer is positioned at the beginning of the file.
# If the specified file does not exist then we will FileNotFoundError. This is default mode.

# w = open an existing file for write operation.
# If the file already contains some data then it will be overridden.
# If the specified file is not already available then this mode will create that file.

# a = open an existing file for append operation.
# It won't override existing data. If the specified file is not already available then this mode will create a new file.

#  r+ = To read and write data into the file.
# The previous data in the file will not be deleted. The file pointer is placed at the beginning of the file.

# w+ = To write and read data. It will override existing data.

# a+ = To append and read data from the file it won't override existing data.

# x =  To open a file in exclusive creation mode for write operation.
# If the file already exists then we will get FileExistsError.
