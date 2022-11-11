import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import time
from IPython import display
import soundfile as sf
#plt.style.use(['dark_background'])

#DEFINIENDO LA SEÑAL
new_signal = np.empty(0)

signal, samplerate = sf.read('violin_05.wav')
time = np.arange(0, len(signal) * 1/samplerate, 1/samplerate)

# GERENADO UNA NUEVA SEÑAL A PARTIR DEL AUDIO
# DEBIDO A QUE ESTA TIENE 2 VALORES (RIGHT AND LEFT
# LOS ARCHIVOS DE AUDIO TIENEN 2 VALORES PARA SER ESCUCHADOS
# EN DISPOSITIVOS CON SALIDAS QUE LOS DIFERENCIAS (COMO AUDÍFONOS)

for i in range (len(signal)):
    new_signal = np.append(new_signal, signal[i][0])
else:
    pass

#CREACIÓN DE KERNEL
kernel = np.exp(-np.linspace(-2,2,31)**2) #FUNCIÓN GAUSSIANAS
kernel = kernel/sum(kernel)
N = len(new_signal) #LONGITUD DE LA SEÑAL

#TAMAÑO DE LA CONVOLUCIÓN
nnew_signal = len(new_signal)
nkernel = len(kernel)
nconvolucion = nnew_signal + nkernel - 1

#APLICACIÓN DE LA CONVOLUCIÓN
resultado = np.convolve(new_signal, kernel, 'full')

plt.figure(figsize=(15,9))

#GRÁFICA DE LA SEÑAL
plt.subplot(311)
plt.plot(new_signal, 'ro-', linewidth=2)
plt.xlim([0, nnew_signal-1])
plt.title('SEÑAL')
plt.axis([20900, 21500, -0.30, 0.60]) #LIMITACIÓN PARA LA VISUALIZACIÓN DE UN TRAMO DE LA SEÑAL
plt.grid()

#GRÁFICA DEL KERNEL
plt.subplot(312)
plt.plot(kernel, 'bo-', linewidth=2)
plt.xlim([0, nnew_signal-1])
plt.title('KERNEL')
plt.axis([-1,70, 0, 0.08]) #LIMITACIÓN PARA VISUIZACIÓN DEL KERNEL
plt.grid()

#GRÁFICA DE LOS RESULTADOS
plt.subplot(313)
plt.plot(resultado, 'yo-', linewidth=2)
plt.xlim([0, nconvolucion])
plt.title('RESULTADO DE CONVOLUCIÓN')
plt.axis([20900, 21500, -0.30, 0.60]) #LIMITACIÓN PARA LA VISUALIZACIÓN DE UN TRAMO DE LA SEÑAL
plt.grid()

plt.show()


# GENERACIÓN DE AUDIO A
# PARTIR DE LA SEÑAL FILTRADA


def create_audio():

    sf.write('audio_convol.flac', resultado, samplerate)

create_audio()
