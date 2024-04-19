import time
def divide(inp,inp2=None): # Baxy Version 1 #
  if '/' not in str(inp) and inp2 is None:return "Something went wrong. Error code NOT_VALID_EQUATION"
  if '/' not in str(inp):x=float(inp);y=float(inp2);z=len(str(x))**2;w=0;v=False;u=0;st=time.time();b=0
  else:g=inp.split('/');x=float(g[0]);y=float(g[1]);z=len(str(x))**2;w=0;v=False;u=0;st=time.time();b=0
  if y==0 or x==0:return 'Something went wrong. Error code DIVIDE_BY_ZERO' 
  if y==1:return float(x)
  while v is False:
    if time.time()-st>=10:return f"Something went wrong. Error code L1TO. Got {w} ."
    w+=int(f'1{"0"*z}')
    if z<=0 and y*w>x>y*(w-1):w-=1;v=True;a=float(w)
    if w*y>x:w-=int(f'1{"0"*z}');z-=1
    if w*y==x:return float(w)
  while a*y!=x:
    if time.time()-st>=10:return f"Something went wrong. Error code L2TO. Got {a} ." 
    if b>10:return 'Something went wrong. Error code GTR10'
    if b==9 and float(f'{str(a)[:len(str(a))-1]}{b}')*y<x:b=1;a=float(f'{str(a)[:len(str(a))]}{b}')
    zer=1;oga=a
    while b==1 and float(f'{str(a)[:len(str(a))-1]}1')*y>x:
      if time.time()-st>=10:return f"Something went wrong. Error code L3TO. Got {a} ."
      a=float(f'{str(oga)[:len(str(oga))-1]}{"0"*zer}1')
      if float(f'{str(a)[:len(str(a))-1]}{"0"*zer}1')*y==x:a=float(f'{str(a)[:len(str(a))-1]}{"0"*zer}1');return a
      zer+=1
    if a*y>x and (float(f'{str(a)[:len(str(a))]}{b-1}'))<x:a=float(f'{str(a)[:len(str(a))-1]}{b-1}');b=1;a=float(f'{str(a)[:len(str(a))]}{b}')
    else:b+=1;a=float(f'{str(a)[:len(str(a))-1]}{b}')
  return float(a)
