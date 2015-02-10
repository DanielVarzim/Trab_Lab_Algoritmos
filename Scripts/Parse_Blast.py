# -*- coding: utf-8 -*-

'''
Created on 29/01/2015

@author: Daniel Varzim
'''
from Bio.Blast import NCBIXML

def parsing_blast(filename):
    result_handle= open(filename+".xml")
    blast_record = NCBIXML.read(result_handle)
    E_VALUE_THRESH = 0.05
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                print('****Alignment****')
                print('sequence:', alignment.title)
                print('length:', alignment.length)
                print('e value:', hsp.expect)
                print(hsp.query[0:75] + '...')
                print(hsp.match[0:75] + '...')
                print(hsp.sbjct[0:75] + '...')
                print("")
    result_handle.close()
    

if __name__ == '__main__':
    #C:\Users\Daniel Varzim\Documents\GitHub\Trab_Lab_Algoritmos\Resultados\Blast\NGO1213_blast
    filename= input("Introduza o nome do ficheiro a efectuar o parsing blast:")
    parsing_blast(filename)