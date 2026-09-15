import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio
from scipy.io import wavfile

RATE = 44_100
LA = 440
DO = 523.25


def display_signal(freq):
    t=np.linspace(0,1,int(freq))
    tab=np.sin(2*np.pi*freq*t)
    plt.plot(t,tab)
    plt.show()






