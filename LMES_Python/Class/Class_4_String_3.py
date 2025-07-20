a = '       Selva      '
print(a.strip())     # removes extra spaces both side
print(a.lstrip())    # remove extra spaces left side
print(a.rstrip())    # remove extra space in right side

b = 'Selva137'
print(b.isalpha())   # check variable is only alpha
print(b.isalnum())   # check variable is alpha & number
print(b.isdigit())   # check variable is only number