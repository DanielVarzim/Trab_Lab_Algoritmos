# -*- coding: utf-8 -*-

'''
Created on 30/01/2015

@author: Grupo6, utilizando exemplos do tutorial de biopython
'''


from Bio import Entrez
from Bio import Medline
import shutil#moving files
import os.path


def ProcurarArtigos(nome):
    # Função que faz procura no PubMed de todos os artigos que contêm informações acerca da Neisseria gonorrhoeae
    Entrez.email = "joaosilva1993@live.com.pt"     
    handle = Entrez.egquery(term = nome)
    record = Entrez.read(handle)
    for row in record["eGQueryResult"]:
        if row["DbName"] == "pubmed":
            print ("Numero de artigos no PubMed: ", (row["Count"]))
      


def DownloadArtigosIDs(nome, numArtigos):
    handle = Entrez.esearch(db = "pubmed", term = nome, retmax = numArtigos) # 11146 artigos existentes
    record = Entrez.read(handle)
    idlist = record["IdList"]
    
    return idlist

def ObterRegistos(idlist):
    # para obter registos Medline e extrair informação
    handle = Entrez.efetch(db = "pubmed", id = idlist, rettype = "medline", retmode = "text")
    records = Medline.parse(handle)
    
    # guarda os registo e estes sÃo convertidos numa lista
    records = list(records)
    return records

def GuardarRegistos(nome, records):
    save_file = open(nome+"_pubmed.txt", "w+")
    for record in records:
        save_file.write("Title: "+ record.get("TI", "?")+"\n")
        save_file.write("Authors: "+ str(record.get("AU", "?"))+"\n")
        save_file.write("Source: "+ record.get("SO", "?")+"\n"+"\n")
    save_file.close()
    
    #moving the file to another directory
    path=os.getcwd()
    src = path+"/"+nome+"_pubmed.txt" #source folder
    dst = "C:/Users/Daniel Varzim/Documents/GitHub/Trab_Lab_Algoritmos/Resultados"#destination folder
    shutil.move(src, dst)

    
    
   
def VerRegistos(records):
    # Dá-nos algumas informações sobre os records
    for record in records:
        print ("Title: ", record.get("TI", "?"))
        print ("Authors: ", record.get("AU", "?"))
        print ("Source: ", record.get("SO", "?"))
        print ("")

def ProcuraTitulo(records):
    search_title = input("Qual o artigo que procura: ") #Introduzir titulo que pretendemos procurar
        
    for record in records:
        if not "TI" in record: #TI-Title
            continue
        if search_title in record["TI"]:
            print ("%s encontrado: %s" % (search_title, record["SO"]))
            
def ProcuraAutor(records):
    search_author = input("Qual o autor que procura: ") #Introduzir o nome do autor que procuramos
        
    for record in records:
        if not "AU" in record:  #AU-Authors
            continue
        if search_author in record["AU"]:
            print ("Autor %s encontrado: %s" % (search_author, record["SO"]))
            
            
def teste():
    ProcurarArtigos("Neisseria gonorrhoeae")                    #diz-nos quantos artigos existem com o nome "neisseria gonorrhaeae"
    lista = DownloadArtigosIDs("Neisseria gonorrhoeae", 11146)  #faz download dos ids de todos os artigos com o nome "neissseria gonorrhaeae"
    registos = ObterRegistos(lista)
    GuardarRegistos("Neisseria gonorrhoeae", registos)          #Guarda alguma info(Titulo, Autor e Source) de todos os artigos encontrados num ficheiro
    #VerRegistos(registos)
    #ProcuraTitulo(registos)
    #ProcuraAutor(registos)

        

if __name__ == '__main__':
    teste()
            
        
        
