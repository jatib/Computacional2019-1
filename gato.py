import random

gato = ["vivo","muerto"]

i = 0
j = 0
n = int(input("elige cuantas veces hacer el experimento:\t"))

while i < n:
	x=random.choice(gato)
	if "vivo" in x:
		j+=1
	i+=1

print "De ",n," veces que se realizo el experimento ",j," veces estuvo vivo"
