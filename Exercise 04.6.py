def computepay(h, r):
 if h<=40:
  pay=h*r
 else:
  pay=(h-40)*r*1.5+40*r
 return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
hrs=float(hrs)
rate=float(rate)
p = computepay(hrs, rate)
print("Pay", p)
