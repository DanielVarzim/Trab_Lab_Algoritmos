# -*- coding: utf-8 -*-

'''
Created on 29/01/2015

@author: Utilizando parte do script do grupo 5 e exemplos do tutorial de biopython
'''

from Bio.Blast import NCBIWWW
from Bio import SeqIO

import shutil#moving files
import os.path
#help(NCBIWWW.qblast)


def blast(filename):
    record = SeqIO.read(filename+".gb", format="genbank")
    result_handle = NCBIWWW.qblast("blastp", "swissprot", record.format("genbank"))
    save_file = open(filename+"_blast.xml", "w")
    save_file.write(result_handle.read())
    save_file.close()
    result_handle.close()
    


def get_locustag(record):
    gis = []
    
    #Codigo do grupo 5
    # selects our relevant locus tags, between NGO1213 and NGO1455, and adds them to 'gis'
    for feature in record.features:
        if feature.type == 'CDS':
            locus_tag = feature.qualifiers['locus_tag'][0]
            if locus_tag >= 'NGO1213' and locus_tag <= 'NGO1455':
                gis.append(feature.qualifiers['db_xref'][0][3:])
                
    return gis

def blastp(genes):
    for gix in genes:
        result_handle = NCBIWWW.qblast("blastp", "swissprot", gix)
        save_file = open(gix+"_blast.xml", "w")
        save_file.write(result_handle.read())
        save_file.close()
        result_handle.close()
        
        #moving the file to another directory
        path=os.getcwd()
        src = path+"/"+gix+"_blast.xml" #source folder
        dst = "C:/Users/Daniel Varzim/Documents/GitHub/Trab_Lab_Algoritmos/Resultados/Blast"#destination folder
        shutil.move(src, dst)
        

def teste1():
    #Efectua o blast de um único ficheiro gb gerado, por exemplo:
    #C:\Users\Daniel Varzim\Documents\GitHub\Trab_Lab_Algoritmos\Resultados\gb records\NGO1213
    #filename= input("Introduza o nome do ficheiro a efectuar o blast:")
    #blast(record, filename)
    

    #tentativa de efectuar o blast de todos os genes
    
    filename= ("C:\\Users\\Daniel Varzim\\Documents\\GitHub\\Trab_Lab_Algoritmos\\Resultados\\Regiao")
    record = SeqIO.read(filename+".gb", format="genbank")
    genes=get_locustag(record)
    blastp(genes)
    

    
if __name__ == '__main__':
    teste1()
