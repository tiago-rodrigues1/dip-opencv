import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# equação de reta
def y(r, p1, p2):
  x1, y1 = p1
  x2, y2 = p2

  if x2 == x1:
    return y1  # evita divisão por zero

  m = (y2 - y1) / (x2 - x1)

  return y1 + m * (r - x1)

img = cv.imread('pollen.jpg', cv.IMREAD_GRAYSCALE).astype(np.uint8)
[height, width] = img.shape

output = np.zeros((height, width), dtype=np.uint8)

# Parâmetros da transformação piecewise linear
r1 = 97
s1 = 30
r2 = 126
s2 = 150

T = np.zeros(256, dtype=np.uint8)

for r in range(256):
  if (r < r1):
    temp = y(r, (0, 0), (r1, s1))
  elif (r < r2):
    temp = y(r, (r1, s1), (r2, s2))
  else:
    temp = y(r, (r2, s2), (255, 255))
  
  T[r] = round(temp)

for i in range(height):
  for j in range(width):
    r = img[i][j]
    output[i][j] = T[r]

cv.imwrite('result.png', output)


# Mostra gráfico da função de transformação
plt.figure(figsize=(12, 10))
plt.title("Função de transformação de intensidade")
plt.xlabel("Intensidade de entrada (r)")
plt.ylabel("Intensidade de saída (s)")

# Define os ticks: de 0 a 250 de 50 em 50 + o extra 255
x_ticks = list(range(0, 251, 50)) + [255]
y_ticks = list(range(0, 251, 50)) + [255]

plt.xticks(x_ticks)
plt.yticks(y_ticks)

plt.grid(True)
plt.plot(T)
plt.show()

