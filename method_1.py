import numpy as np
import pandas as pd

dataset = pd.read_csv('source.csv',';')
df = pd.DataFrame(dataset)
AgentList=[['A1',0.0],['A2',0.0],['A3',0.0],['A4',0.0],['A5',0.0],['A6',0.0],['A7',0.0]]
#AgentList
Agent_df=pd.DataFrame(AgentList,columns=['Agent','Bakiye'])



Grup1 = df[df['GRUP_KODU'] == 'G1']
Grup1[['SORUMLU']] = Grup1[['SORUMLU']].astype('str')

Grup2 = df[df['GRUP_KODU'] != 'G1']
Grup2[['SORUMLU']] = Grup2[['SORUMLU']].astype('str')

max_bal_ix=np.argmax(Grup1.iloc[:, 1].values)
min_agent_ix=np.argmin(Agent_df.iloc[:, 1].values)
Grup1[max_bal_ix,4]=Agent_df[min_agent_ix,0]

for i in range(0, len(Grup1)):
    max_bal_ix=np.argmax(Grup1.iloc[:, 1].values)
    min_agent_ix=np.argmin(Agent_df.iloc[:, 1].values)
    Agent_df.at[min_agent_ix,'Bakiye'] += Grup1.at[max_bal_ix,'BAL']
    Grup1.at[max_bal_ix,'SORUMLU']=Agent_df.at[min_agent_ix,'Agent']
