# Tic Tac Toe Game Develop:

list = ["_","_","_",
        "_","_","_",
        "_","_","_",]

def display():
    print(list[0] + "|" + list[1] + "|" + list[2])
    print(list[3] + "|" + list[4] + "|" + list[5])
    print(list[6] + "|" + list[7] + "|" + list[8])

list[0] = "X"

def update():
    pos = int(input("Enter you index for marking 'X': "))
    list[pos] = "X"

while True:
    display()
    update()