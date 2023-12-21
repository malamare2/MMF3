import math

# Definirajte funkciju koja opisuje ponašanje tijela
def funkcija(t):
    return math.sin(2*t) - 2*math.cos(t)

# Postavite granice pretrage na temelju vašeg problema
donja_granica = 0
gornja_granica = 10

# Koristite bisekciju za pronalaženje trenutka zaustavljanja tijela
trenutak_zaustavljanja = bisect(funkcija, donja_granica, gornja_granica)

print(f"Tijelo se zaustavilo u trenutku {trenutak_zaustavljanja}.")