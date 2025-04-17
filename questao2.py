# Questão numero 2

def alerta_uso(lista):
  for l in lista:
    if l > 85:
      return True
  return False

for i in range(4):
  resultado = alerta_uso(uso_cpu[i])
  print(f'Região {i + 1} tem mais de 85%: {resultado}')