class stack:
    def __init__(self):
        self.top = -1
        self.arr = []
    def push(self,x):
        self.arr.append(x)
        self.top += 1
    def pop(self,x):
        self.arr.pop(self.top)
        self.top -=1
    def show(self):
        print(self.arr,self.top)


# class la chalu kel
trial = stack()

# element push kele
trial.push(10)

# push kelyavr element check kele
trial.show()
trial.push(20)
trial.show()
trial.push(30)
trial.show()

print()

# element pop kele
trial.pop(30)

# pop kelyavr element check kele
trial.show()
trial.pop(20)
trial.show()
trial.pop(10)
trial.show()



