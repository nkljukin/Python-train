#Деконволюция изображения

from scipy import signal
original = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0]]
impulse_response = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
recorded = signal.convolve(impulse_response, original)
print(recorded)