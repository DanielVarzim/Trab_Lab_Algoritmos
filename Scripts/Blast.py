# -*- coding: utf-8 -*-

'''
Created on 29/01/2015

@author: Daniel Varzim
'''

from Bio.Blast import NCBIWWW
from Bio import SeqIO

import shutil#moving files
import os.path
#help(NCBIWWW.qblast)


def blast(record,filename):
    result_handle = NCBIWWW.qblast("blastp", "swissprot", record.format("genbank"))
    save_file = open(filename+"_blast.xml", "w")
    save_file.write(result_handle.read())
    save_file.close()
    result_handle.close()
    #Não consegui mover o ficheiro criado para a pasta desejada
    """
    #moving the file to another directory
    path=os.getcwd()
    src = path+"/"+filename #source folder
    dst = "C:/Users/Daniel Varzim/Documents/GitHub/Trab_Lab_Algoritmos/Resultados/Blast"#destination folder
    shutil.move(src, dst)
    """


def teste1():
    
    #C:\Users\Daniel Varzim\Documents\GitHub\Trab_Lab_Algoritmos\Resultados\gb records\NGO1213
    #filename= input("Introduza o nome do ficheiro a efectuar o blast:")
    #record = SeqIO.read(filename+".gb", format="genbank")
    #blast(record, filename)
    

    #tentativa de efectuar o blast de todos os ficheiros genbank gerados
    
    for i in range(1213,1456):
        a=str(i)
        filename= ("C:\\Users\\Daniel Varzim\\Documents\\GitHub\\Trab_Lab_Algoritmos\\Resultados\\gb records\\NGO"+a)
        record = SeqIO.read(filename+".gb", format="genbank")
        blast(record, filename)
    

    
if __name__ == '__main__':
    teste1()
