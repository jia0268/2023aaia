a = int(input())

if(a<=2000):
	print(100)

else:
	a2 = a-2000
	if((a2%500)!=0):print(f'{100+((a2//500)+1)*5}')
	elif((a%2500)==0):print(f'{100+(a2//500)*5}')
	