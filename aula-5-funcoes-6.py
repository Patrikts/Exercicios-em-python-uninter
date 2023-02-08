def comida():
    ovos = 'variável local de comida'
    print(ovos)

def bacon():
    ovos = 'variável local de bacon'
    print(ovos)
    comida()
    print(ovos)

#Programa principal
ovos = 'variável global'
bacon()
print(ovos)