# Equation
tim=float(input("Enter the number a: "))
print(str(tim)+"*x")
ope=input("+.   -.   *.   /.: ")
nb=float(input("Enter the number b: "))
equal=float(input("Enter the result of equation: "))
if ope=='+':
	print(str(tim)+"*x"+str(ope)+str(nb)+"="+str(equal))
	print("<=> "+str(tim)+"*x"+" = "+str(equal)+"-"+str(nb))
	print("<=> x = "+str(equal-nb)+"/"+str(tim))
	print("<=> x = "+str((equal-nb)/tim))
elif ope=='-':
	print(str(tim)+"*x"+str(ope)+str(nb)+"="+str(equal))
	print("<=> "+str(tim)+"*x"+" = "+str(equal)+"+"+str(nb))
	print("<=> x = "+str(equal+nb)+"/"+str(tim))
	print("<=> x = "+str((equal+nb)/tim))
elif ope=='*':
	print(str(tim)+"*x"+str(ope)+str(nb)+"="+str(equal))
	print("<=> "+str(tim)+"*x"+" = "+str(equal)+"/"+str(nb))
	print("<=> x = "+str(equal*nb)+"/"+str(tim))
	print("<=> x = "+str((equal/nb)/tim))
else:
	print(str(tim)+"*x"+str(ope)+str(nb)+"="+str(equal))
	print("<=> "+str(tim)+"*x"+" = "+str(equal)+"*"+str(nb))
	print("<=> x = "+str(equal/nb)+"/"+str(tim))
	print("<=> x = "+str((equal*nb)/tim))

