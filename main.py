import tabula 
import pandas as pd
import numpy as np
from zipfile import *
import os

def tab1(l):
    tabela1 = l[0]
    df = pd.DataFrame(tabela1)
    df.to_csv('tabela1.csv', index=False)

def tab2(l):
    tabela2 = l[1:7]
    cont = 0
    lista1 = ''

    for lista in tabela2:
        cont = cont + 1
        if(cont < 1):
            lista1 = lista
        elif(cont < 2):
            lista2 = lista
        elif(cont < 3):
            lista3 = lista
        elif(cont < 4):
           lista4 = lista
        elif(cont < 5):
           lista5 = lista
        elif(cont < 6):
           lista6 = lista
        elif(cont < 7):
            lista7 = lista

    ld = np.array(dtype=object,object=[lista1,lista2,lista3,lista4,lista5,lista6,lista7])     
    df = pd.DataFrame(ld)
    df.to_csv('tabela2.csv')

def tab3(l):
    tabela3 = l[7]

    df = pd.DataFrame(tabela3)
    df.to_csv('tabela3.csv', index=False)

def zip():
    with ZipFile('Teste_Intuitive_Care{John_Santos_Felix_de_Santana}.zip', 'w') as myzip:
        myzip.write('tabela1.csv')
        myzip.write('tabela2.csv')
        myzip.write('tabela3.csv')

    os.remove('tabela1.csv')
    os.remove('tabela2.csv')
    os.remove('tabela3.csv')


pdf = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-tiss/padrao-tiss/padrao_tiss_componente_organizacional_202108.pdf'

l = tabula.read_pdf(pdf, pages='108-114',multiple_tables=True ,guess=True)

tb1 = tab1(l)
tb2 = tab2(l)
tb3 = tab3(l)

zp = zip()