# 17_using_(__name__).py
# Updated: cramos 10/oct/2022

# This code snippet show how to use the __name__ attribute
# which helps to local the file where the code is running on

print ('Hello there...\n')

def my_func():
	""" This function just simple prints dummy words """
	print(f'Printing inside my_func: {__name__} \n')

# Step 1. This will produce "main" output
print (f'This is the main section: {__name__} \n')

# Step 2. Calling a function
my_func()


if __name__ == "__main__":
	print("We are running the main python file....")