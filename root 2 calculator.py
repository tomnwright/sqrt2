target = 1.4142135623730950488
import time
start = time.time()
class sfrac:
	#standard_frac = sfrac()
	def __init__(self, numerator=1, denominator=1):
		self.numerator = numerator
		self.denominator = denominator
	def get_decimal(self):
		pass
	def get_reciprical(self):
		return sfrac(self.denominator,self.numerator)
	def __str__(self):
		return "{}/{}".format(self.numerator,self.denominator)
class tools:
	def add_frac(frac_1, frac_2):
		numerator_1 = (frac_1.denominator*frac_2.numerator)+(frac_2.denominator*frac_1.numerator)
		denominator_1 = frac_1.denominator*frac_2.denominator
		return sfrac(numerator_1,denominator_1)
	def indftN_str(n):
		if "." in n:
			return n.split(".")
		else:
			return [n,"0"]
	def lstripNUM_0(n):
		n = n.lstrip("0")
		return ["","0"][n[0]=="."]+n
	def ratio2dec(n,d,dp):
		d = int(d)
		n = tools.indftN_str(str(n))
		if dp<1: #decimal place validation
			raise Exception("dp cannot be less than 1")

		carry = ""
		answer=[]
		for i in n[0]:
			temp = int(carry+i)
			answer.append(str(temp//d))
			carry = str(temp%d)
		answer.append(".")
		i = 0
		while i<(dp):
			if (i+1)>len(n[1]):
				temp = int(carry+"0")
			else:
				temp = int(carry+n[1][i])
			answer.append(str(temp//d))
			carry = str(temp%d)
			i+=1
		return tools.lstripNUM_0("".join(answer))
def get_sqrt2(i,dp):
	rat2 = sfrac(2)
	def a_next(b):
		return tools.add_frac(b.get_reciprical(),rat2)
	a = sfrac(1,2)
	print("starting ratio iterations...",end="")
	for k in range(i):
		a = a_next(a)
		if k%25000==0:
			print(".",end="")
	c=tools.add_frac(a,sfrac(-1))
	print("DONE\nstarting decimal conversion...",end="")
	rat = tools.ratio2dec(c.numerator,c.denominator,dp)
	print("DONE\nstarting file writing...",end="")
	with open("decimal.txt",mode="w") as file:
		file.write(rat)
	print("DONE")

#get_sqrt2(60000,30000)
