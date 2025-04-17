# Questão numero 1

uso_cpu = [
[20, 25, 40, 50, 45, 60, 55, 35, 70, 65],
[30, 35, 50, 60, 40, 55, 60, 45, 50, 55],
[15, 20, 30, 25, 35, 40, 45, 50, 55, 60],
[10, 15, 25, 35, 45, 50, 55, 60, 65, 70],
]

def mediaLinha(lista):
  for l in range(len(lista)):
    mediaLinha1 = sum(lista[0]) / len(lista[0])
    mediaLinha2 = sum(lista[1]) / len(lista[1])
    mediaLinha3 = sum(lista[2]) / len(lista[2])
    mediaLinha4 = sum(lista[3]) / len(lista[3])

  print(mediaLinha1)
  print(mediaLinha2)
  print(mediaLinha3)
  print(mediaLinha4)