class OddNumberSeries:
    def series(self,n):
        b=[]
        if n<=0:
            print("enter the number above zero")
        else:
            for i in range(1,n+1):
                if i%2!=0:
                    b.append(i)
                    #print(i)
            print(b)


n = int(input("ENTER THE NUMBER\n"))
o=OddNumberSeries()
o.series(n)
