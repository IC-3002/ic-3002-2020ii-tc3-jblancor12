def sumatoria_cubica(n):
	res=0
	for i in range(n):	
		
		for j in range(i+1):
			
			for k in range(i+1):
				res=res+1	
	print (res)
	return res


def sumatoria_constante(n):
	print ((n*(n+1)*(2*n+1))/6)
	return (n*(n+1)*(2*n+1))/6



sumatoria_constante(10)
sumatoria_cubica(10)