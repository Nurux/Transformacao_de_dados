'''
Obs: Há um jeito bem mais facil de fazer esse mesmo projeto usando a lib Camelot, porém achei meio inviavel já
que para utiliza-la o usuario deve baixar dois programas a parte e ainda importar a lib aqui no terminal.
Projeto feito com as libs Tabula, Pandas, Numpy, Zipfile e Os
Obs2: se quiser as três tabelas em unico csv, então só sera necessário importar a lib tabula
Ex só com tabula: 
    import tabula
    url_pdf = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-tiss/padrao-tiss/padrao_tiss_componente_organizacional_202108.pdf'
    tabula.io.convert_into(url_pdf, 'tabelas.csv', 'csv', pages='108-114')
Como não queria as 3 tabelas juntas optei por adicionar outras libs.
Abra o terminal e digite:
    pip install tabula
    pip install pandas
    pip install numpy
    pip install zipfile
    pip install os
Se estiver em ambiente Linux:
    pip3 install tabula  
    pip3 install pandas
    pip3 install numpy
    pip3 install zipfile
    pip3 install os  
'''

from typing import List
import tabula 
import pandas as pd
import numpy as np
from zipfile import *
import os

def gera_tabela1(l):
    tabela1 = l[0]
    df = pd.DataFrame(tabela1)
    df.to_csv('tabela1.csv', index=False)

def gera_tabela2(l):
    tabela2 = l[1:7]

    ld = np.array(dtype=list, object=[tabela2])
    df = pd.DataFrame(ld)
    df.to_csv('tabela2.csv')


def gera_tabela3(l):
   
    tabela3 = l[7]

    df = pd.DataFrame(tabela3)
    df.to_csv('tabela3.csv', index=False)

def gera_zip():
   
    with ZipFile('Teste_Intuitive_Care{John_Santos_Felix_de_Santana}.zip', 'w') as myzip:
        myzip.write('tabela1.csv')
        myzip.write('tabela2.csv')
        myzip.write('tabela3.csv')

    os.remove('tabela1.csv')
    os.remove('tabela2.csv')
    os.remove('tabela3.csv')


def main():    
    print('Pesquisando arquivo...\n')

    if os.path.isfile('./Teste_Intuitive_Care{John_Santos_Felix_de_Santana}.zip'):
        print('Arquivo encontrado, verifique a pasta raiz. \nSkipando download...')

    else:
        print('Iniciando download')

        pdf = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-tiss/padrao-tiss/padrao_tiss_componente_organizacional_202108.pdf'

        l = tabula.read_pdf(pdf, pages='108-114', multiple_tables=True , guess=True)
        
        pd.set_option('display.max_colwidth', None)
        gera_tabela1(l)
        gera_tabela2(l)
        gera_tabela3(l)

        gera_zip()
        

if __name__ == '__main__':
    main()
