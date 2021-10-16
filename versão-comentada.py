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

#Define opção maxima de display como nula, para evitar truncamento de dados 
pd.set_option('display.max_colwidth', None)

def tab1(l):
    #Pega a variavel l como parametro e busca o primeiro elemento da lista, depois transforma a lista em um DataFrame e converte para um arquivo csv e retira a indexação
    tabela1 = l[0]
    df = pd.DataFrame(tabela1)
    df.to_csv('tabela1.csv', index=False)

def tab2(l):
    #Pega a variavel l como parametro e busca do 2° até o 8° elemento da lista, (lembrando que o inicio da lista tem indicie 0 portanto o numero 1 e referente ao 2° elemento)
    tabela2 = l[1:7]

    #Por fim junta a variavel de alocação em um array, transforma esse array em um Dataframe e depois converte para um arquivo csv
    ld = np.array(dtype=list, object=[tabela2])
    df = pd.DataFrame(ld)
    df.to_csv('tabela2.csv')


def tab3(l):
    #Pega a variavel l como parametro e adiciona a variavel tabela o conteudo do indicie 7 da lista ou o 8° elemento (nesse caso ele só vai pegar a ultima tabela da pagina no caso a do quadro 32)
    tabela3 = l[7]

    #Transforma o dados recebido em um Dataframe e converte ele para um arquivo csv sem indexação
    df = pd.DataFrame(tabela3)
    df.to_csv('tabela3.csv', index=False)

def zip():
    #Por fim pega todos os arquivos csv na pasta raiz e compacta eles em zip, logo em seguida apaga os 3 arquivos csv da pasta 
    with ZipFile('Teste_Intuitive_Care{John_Santos_Felix_de_Santana}.zip', 'w') as myzip:
        myzip.write('tabela1.csv')
        myzip.write('tabela2.csv')
        myzip.write('tabela3.csv')

    os.remove('tabela1.csv')
    os.remove('tabela2.csv')
    os.remove('tabela3.csv')


#Inicio do programa
print('Pesquisando arquivo...\n')

if os.path.isfile('./Teste_Intuitive_Care{John_Santos_Felix_de_Santana}.zip'):
    #Caso o arquivo exista o programa informa ao usuário e fecha
    print('Arquivo encontrado, verifique a pasta raiz. \nSkipando download...')

else:
    #Defini o a variavel pdf com a url do arquivo 
    pdf = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-tiss/padrao-tiss/padrao_tiss_componente_organizacional_202108.pdf'

    #Usei o tabula para ler somente as paginas que continham os quadros 30, 31 e 32 e atribui o resultado a variavel l que ficou como um tipo lista, já que o tabula retorna este tipo.
    l = tabula.read_pdf(pdf, pages='108-114', multiple_tables=True , guess=True)

    #Chamei as funções em sequencia
    tb1 = tab1(l)
    tb2 = tab2(l)
    tb3 = tab3(l)

    #Chamei função de geral zip 
    zp = zip()
