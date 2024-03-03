#task 1
lists = [1, 2, 3, 4, 5]
x = '*'.join(str(list) for list in lists)
print(eval(x))
#task 2
s = "IsMaILApaBeK"
countupper = 0
countlower = 0
for c in s:
    if c.isupper():
        countupper += 1
    elif c.islower():
        countlower += 1
print(countlower,countupper)
#task 3
s = "QazaQ"
if s == s[::-1]:
    print("YES")
# task 4
import time 
num = int(input())
milsec = int(input())
sec = milsec/1000
time.sleep(sec)
sqrt = num ** 0.5
txt = 'Square root of {fnum} after {fsec} is {fsqrt}'.format(fnum = num, fsec = milsec, fsqrt = sqrt)
print(txt)

#task 5
mytup = (True, True, False)
mytup2 = (True, True, True)
print(all(mytup))
print(all(mytup2))