import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()
lista = []
podzielone = []
for file in os.listdir(file_path):
    if file.endswith(".pdf"):
        file = file[:-4]
        lista.append(file)
print(lista)
for i in range(len(lista)):
    podzielone.append(lista[i].split(" "))
print(podzielone)

df = pd.DataFrame(podzielone, columns=['NUMER RYSUNKU', 'NAZWA DETALU'])
df['TYPE'] = ''
df.insert(loc=0, column='NUMER PROJEKTU', value=['' for i in range(df.shape[0])])
df.insert(loc=0, column = 'Lp.', value=[i+1 for i in range(df.shape[0])])
df = df.set_index('Lp.')
print(df)

writer = pd.ExcelWriter('ewidencja_simple.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
