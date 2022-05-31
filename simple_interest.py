principle=int(input("enter principle"))
rate=int(input("enter rate "))
time=int(input("enter time"))
SI = principle*(1+(rate*time))
print("simple interest =",SI)
total_amount = principle+SI
print("total amount=",total_amount)    