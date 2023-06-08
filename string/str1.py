a=input("Enter a string")
if len(a)<2:
  result=''
else:
  result=a[:2]+a[-2:]

print ("Result",result)
