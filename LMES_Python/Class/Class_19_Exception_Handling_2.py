# Exception Handling 2:
# Multiple except block for same error name is not allowed it ends with error.
# 1 except block have only one else block is allowed multiple else not allowed.
# 1 try block have only 1 finally block is allowed multiple finally block not allowed.

print('Program Starts')
a = 10
b = 0
try:
    print(a/b)
except:                         # This block is execute whether exception happens. # except block only present after try block only.
    print('Provide Integer Values')
else:                           # Else block is followed by except block only. # except is mandatory for else block.
    print('Good Job')
finally:                        # we have to use this finally block whether followed by try block including except block or finally block.
                                # this finally block is executed whether exception happens or not.
    print('Cleaning Statements')
print('Program Ends')

# userdefined exception:

class Too_Old_Exception(Exception):
    def __init__(self,arg):
        self.msg = arg
class Too_Young_Exception(Exception):
    def __init__(self,arg):
        self.msg = arg
age = int(input('Enter Your Age: '))
if age>=60:
    raise Too_Old_Exception('Your Age is Too crossed to Marry')             # "raise" will help to raise the execution.
elif age < 18:
    raise Too_Young_Exception('Your Age is not met the limit to Marry, Please wait to Mature')
else:
    print('You will get the details soon via email.')
print('Have a Nice Day!')