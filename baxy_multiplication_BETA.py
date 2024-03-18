#This is not fit for a public release
#This is meant to be incorporated into Baxy
#The idea for this is to go to the last decimal number, multiply it by whatever, and carry the decimals over, yk like how you do multiplication but just add it to a table
print('enter number to multiply')
m = float(input())
print('enter number to multiply by')
l = float(input())
t = len(str(m).split(".")[1]) + len(str(l).split(".")[1])
if m == int(m):
    t -= 1
if l == int(l):
    t-=1
m = str(m)[::-1]
l = str(l)[::-1]
e = []
c = 1
con = 0
for i in m:
    print(e)
    if i == '.':
        e.append('.')
    else:
        d = (int(l[len(l) - c::len(l)]) * int(i)) + con
        con = 0
        print(d, i)
        if len(str(d)) >= 2:
            e.append(str(str(d)[len(str(d))-1::len(str(d))]))
            con = int(str(d)[:-1])
        else:
            e.append(str(d))
if con != 0:
    e.append(str(con))
print(''.join(e)[::-1])


#incase i need this later
#'what'[len('what')-chartofind::len('what')] gets whatever letter you want (e.g. chartofind=1 will give t and chartofind = 2 will give a)

#For github people:
#This version can multiply <float number> * <single digit intiger>
