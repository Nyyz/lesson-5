#задача1
lst1 = []
lst2 = []
def func(a,b):
    lst1.append(a)
    lst2.append(b)
func(1, 2)
func(3, 4)
func(5, 6)
func(7, 8)
dct={}
for i in range(len(lst1)):
    dct[lst1[i]]=lst2[i]
print(dct)

#задача2
lst3 = []
lst4 = []
def func2(d, c):
    lst3.append(d)
    lst4.append(c)
func2(21, 22)
func2(23, 24)
func2(25, 26)
func2(27, 28)
func2(29, 30)
dct1={}
for i in range(len(lst4)):
    dct1[lst3[i]]=lst4[i]
print(dct1)