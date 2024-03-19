                    # WARNING #
        # THIS VERSION OF BAXY IS HEAVILY IN BETA #
  # THIS VERSION CAN ONLY DO FLOAT NUMBER / SINGLE DIGIT INTIGER #
      # IT IS NOT RECCOMENDED TO USE THIS VERSION ! #




 # Baxy Version 1.1 (BETA) (READABLE) (EXPECT BREAKS) #
import time

def multiply(m, l):
  m = float(m)
  l = float(l)
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
    if i == '.':
        e.append('.')
    else:
        d = (int(l[len(l) - c::len(l)]) * int(i)) + con
        con = 0
        if len(str(d)) >= 2:
            e.append(str(str(d)[len(str(d))-1::len(str(d))]))
            con = int(str(d)[:-1])
        else:
            e.append(str(d))
  if con != 0:
    e.append(str(con))
  return float(''.join(e)[::-1])



def divide(inp, inp2=None):
  if '/' not in str(inp):
    if inp2 is None:
      return "Something went wrong. Error code NOT_VALID_EQUATION"


  if '/' not in str(inp):
    x = float(inp)
    y = float(inp2)
    z = len(str(x))**2
    w = 0
    v = False
    u = 0
    st = time.time()
    b = 0


  else:
    g = inp.split('/')
    x = float(g[0])
    y = float(g[1])
    z = len(str(x))**2
    w = 0
    v = False
    u = 0
    st = time.time()
    b = 0


  if y == 0 or x == 0:
    return 'Something went wrong. Error code DIVIDE_BY_ZERO' 
  if y == 1:
    return float(x)



  while v is False:
    if time.time() - st >= 10:
      return f"Something went wrong. Error code L1TO. Got {w} ."


    w += float(f'1{"0"*z}')
    if z <= 0 and y * w > x > y * (w-1):
      w -= 1
      v = True
      a = float(w)


    if w * y > x:
      w -= float(f'1{"0"*z}')
      z -= 1


    if w * y == x:
      return float(w)


  while multiply(a, y) != x:
    if len(str(multiply(a, y))) > len(str(a))*1.5:
      print(f'Possible Multiplication Error Detected: {a} * {y} = {multiply(a, y)}')
    if time.time()-st >= 10:
      return f"Something went wrong. Error code L2TO. Got {a} ." 

    if b > 10:
      return 'Something went wrong. Error code GTR10'

    if b==9:
      if multiply(float(f'{str(a)[:len(str(a))-1]}{b}'), y) < x:
        b=1
        a=float(f'{str(a)[:len(str(a))]}{b}')


    zer=1
    oga=a
    while b == 1 and multiply(float(f'{str(a)[:len(str(a))-1]}1'), y) > x:

      if time.time() - st >= 10:
        return f"Something went wrong. Error code L3TO. Got {a} ."


      a = float(f'{str(oga)[:len(str(oga))-1]}{"0"*zer}1')

      if b==1:
        if multiply(float(f'{str(a)}1'), y) > x:
          if multiply(float(f'{str(a)[:len(str(a))-1]}{"0"*(zer-1)}1'), y) > x:
            if multiply(float(f'{str(a)[:len(str(a))-1]}{"0"*zer}1'), y) == x:
              return float(f'{str(a)[:len(str(a))-1]}{"0"*zer}1')

      zer+=1

    if multiply(a, y) > x:
      if (float(f'{str(a)[:len(str(a))]}{b-1}')) < x:
        a = float(f'{str(a)[:len(str(a))-1]}{b-1}')
        b = 1
        a = float(f'{str(a)[:len(str(a))]}{b}')


    else:
      b+=1
      a=float(f'{str(a)[:len(str(a))-1]}{b}')


  return float(a)
