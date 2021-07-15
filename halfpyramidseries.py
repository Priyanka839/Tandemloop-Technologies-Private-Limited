class HalfPyramid:
    def halfpyramid(self,n):
        for row in range(1,n+1):
            if row % 2 != 0:
                for col in range(1, row+1):
                    print(col,end=" ")
                print()
            else:
                for col in range( row ,0,-1):
                    print(col, end=" ")
                print()
        for row in range(n-1,0,-1):
            if row % 2 != 0:
                for col in range(1, row + 1):
                    print(col, end=" ")
                print()
            else:
                for col in range(row, 0, -1):
                    print(col, end=" ")
                print()
n = int(input("ENTER THE NUMBER\n"))
h=HalfPyramid()
h.halfpyramid(n)