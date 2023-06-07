if __name__=="__main__":
    from scipy.io.wavfile import read
    import matplotlib.pyplot as plt
    from ejercicio_2 import indicesmaximos, indicesminimos
    import numpy as np


def carga(direccion):
    fs, data = read(direccion) 
    return fs, data

def promedio(data):
    
    promedio=sum(data)/len(data)
    
    return(promedio)
if __name__=="__main__":
    
    
    fs, data=carga("audio.wav")
    print(data)

    indicesminimos(data)
    indicesmaximos(data)
    duracion=10
    promedioprint=np.ones(duracion*fs)*promedio
    plt.plot(np.arange(0,duracion,1/fs),data[0:duracion*fs])
    plt.plot(np.arange(0,duracion,1/fs),promedioprint)
    plt.show()
