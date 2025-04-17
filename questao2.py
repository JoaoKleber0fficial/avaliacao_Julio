# Questão numero 2

uso_cpu = [
[20, 25, 40, 50, 45, 60, 55, 35, 70, 65],
[30, 35, 50, 60, 40, 55, 60, 45, 50, 55],
[15, 20, 30, 25, 35, 40, 45, 50, 55, 60],
[10, 15, 25, 35, 45, 50, 55, 60, 65, 70],
]

def alerta_uso(lista):
  for l in lista:
    if l > 85:
      return True
  return False

for i in range(4):
  resultado = alerta_uso(uso_cpu[i])
  print(f'Região {i + 1} tem mais de 85%: {resultado}')