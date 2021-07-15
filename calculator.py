class Calculator:
    def add(self, x, y):
        x = self.x
        y = self.y
        print("the result is",x+y)

    def sub(self, x, y):
        x = self.x
        y = self.y
        print("the result is",x-y)

    def mul(self, x, y):
        x = self.x
        y = self.y
        print("the result is",x * y)

    def div(self, x, y):
        x = self.x
        y = self.y
        print("the result is",x/y)

c = Calculator()
#The float() and int() operators will be sufficient, as Python floats are usually the equivalent of C doubles, and if the integer is too large, int() will cast it to a long int
c.x = float(input("ENTER THE VALUE OF A\n"))
c.y = float(input("ENTER THE VALUE OF B\n"))
print("Enter the operation")
print("1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")
select = int(input("Select any one operations  between 1 to 4:"))
if select == 1:
    c.add(c.x, c.y)

elif select == 2:
    c.sub(c.x, c.y)
elif select == 3:
    c.mul(c.x, c.y)
elif select == 4:
    if c.y <= 0:
        print("You cannot divide by zero")
    else:
        c.div(c.x, c.y)
else:
    print("Invalid")



