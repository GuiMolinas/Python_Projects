from math import cos, tan, radians, sin
an = float(input('Digite um ângulo: '))
seno = sin(radians(an))
print('O seno de {}° é igual a {:.2f}'.format(an, seno))
cosseno = cos(radians(an))
print('O cosseno de {}° é igual a {:.2f}'.format(an, cosseno))
tg = tan(radians(an))
print('A tagente de {}° é igual a {:.2f}'.format(an, tg))


