
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class actividad2:
    def __init__(self):
        self.ruta_raiz=os.path.abspath(os.getcwd())
        self.ruta_act2 = "{}/src/pad20251/actividad_2/".format(self.ruta_raiz)
        print(self.ruta_raiz)
    def punto_11(self,num=100):
        x = np.random.rand(num)
        y = np.random.rand(num)
        plt.scatter(x,y)
        ruta = "{}punto_11.png".format(self.ruta_act2)
        plt.savefig(ruta)
        
act = actividad2()
act.punto_11()