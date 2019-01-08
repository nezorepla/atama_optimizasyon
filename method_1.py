#alper
import numpy as np
import pandas as pd

dataset = pd.read_csv('source.csv',';')
df = pd.DataFrame(dataset)
AgentList=[['A1',0],['A2',0],['A3',0],['A4',0],['A5',0],['A6',0],['A7',0]]
#AgentList
        

Grup1 = df[df['GRUP_KODU'] == 'G1']
Grup2 = df[df['GRUP_KODU'] != 'G1']
