# -*- coding: utf-8 -*-

'''
Created on 05/02/2015

@author: Daniel Varzim
'''

from Bio import Entrez

def lineage(Organism):
    Entrez.email = "pg27662@alunos.uminho.pt"     
    handle = Entrez.esearch(db="Taxonomy", term=Organism)
    result = Entrez.read(handle)
    handle.close()
    ID= result["IdList"]
    handle2 = Entrez.efetch(db="Taxonomy", id=ID, retmode="xml")
    result2 = Entrez.read(handle2)
    handle2.close()
    return result2[0]["Lineage"]

if __name__ == '__main__':
    print (lineage("Neisseria gonorrhoeae"))