a = float(input("Ström (A)"))
u = float(input("Spänning (V)"))
r = float(input("radie (meter)"))

m = ((((r**2)*(1.602)*(10**(-19)))/(2*u))*((((541)/(781250))*a)**2))


mprefix = m*(10**(-31))

mprefixshort = round(mprefix, 5)

print("Massan av elektronen är estimerad till ",mprefixshort,"!")
