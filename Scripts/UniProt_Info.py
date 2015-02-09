# -*- coding: utf-8 -*-

'''
Created on 05/02/2015

@author: Daniel Varzim utilizando algumas funções do grupo1
'''
import os
from Bio import SeqIO
from Bio import SwissProt
import urllib
from Uniprot_Parser import *
from Bio.SeqIO import UniprotIO

def Get_Gene_IDs():
    path = "C:/Users/Daniel Varzim/Documents/GitHub/Trab_Lab_Algoritmos/Resultados/gb records/"
    IDs=[]
    for filename in os.listdir(path):
        result_handle= open(path+filename)
        record = SeqIO.read(result_handle, format="genbank")
        IDs.append(record.id)
        result_handle.close
    return IDs


def Get_Protein_IDs():
    path="C:/Users/Daniel Varzim/Documents/GitHub/Trab_Lab_Algoritmos/Resultados/Tabela/Protein_IDs.txt"
    IDs=[]
    file=open(path)
    lines=file.readlines()
    for line in lines:
        IDs.append(line.splitlines())
    file.close
    return IDs

def uniprot_ID():
    UniprotIDs=[]
    proteins=Get_Gene_IDs()
    for j in range(len(proteins)):
        data = urllib.request.urlopen("http://www.uniprot.org/uniprot/?query="+proteins[j]+"&sort=score").read()
        if len(data.split())>=3305:
            x=str(data.split()[3305])
            UniprotIDs.append(x[6:12])
        else:
            UniprotIDs.append("Não tem!")
    return UniprotIDs



ID=['Q5F7G5', 'Q5F7G4', 'Q5F7G3', 'Q5F7G2', 'Q5F7G1', 'Q5F7G0', 'Q5F7F9', 'Q5F7F8', 'Q5F7F7', 'Q5F7F6', 'Q5F7F5', 'Q5F7F4', 'Q5F7F3', 'Q5F7F2', 'Q5F7F1', 'Q5F7F0', 'Q5F7E9', 'Q5F7E8', 'Q5F7E7', 'Q5F7E6', 'Q5F7E5', 'Q5F7E4', 'Q5F7E3', 'Q5F7E2', 'Q5F7E1', 'Q5F7E0', 'Q5F7D9', 'Q5F7D8', 'Q5F7D7', 'Q5F7D6', 'Q5F7D5', 'Q5F7D4', 'Q5F7D3', 'Q5F7D2', 'Q5F7D1', 'Q5F7D0', 'Q5F7C9', 'Q5F7C8', 'Q5F7C7', 'Q5F7C6', 'Q5F7C5', 'Q5F7C4', 'Q5F7C3', 'Q5F7C2', 'Q5F7C1', 'Q5F7C0', 'Q5F7B9', 'Q5F7B8', 'Q5F7B7', 'Q5F7B6', 'Q5F6B6', 'Q5F6B5', 'Q5F7B3', 'Q5F7B2', 'Q5F7B1', 'Q5F7B0', 'Q5F7A9', 'Q5F7A8', 'Q5F7A7', 'Q5F7A6', 'Q5F7A5', 'Q5F7A4', 'Q5F7A3', 'Q5F7A2', 'Q5F7A1', 'Q5F7A0', 'Q5F799', 'Q5F798', 'Q5F797', 'Q5F796', 'Q5F795', 'Q5F794', 'Q5F793', 'Q5F792', 'Q5F791', 'Q5F790', 'Q5F789', 'Q5F788', 'Q5F787', 'Q5F786', 'Q5F785', 'Q5F784', 'Q5F783', 'Q5F782', 'Q5F781', 'Q5F5M0', 'Q5F779', 'Q5F778', 'Q5F777', 'Q5F776', 'Q5F775', 'Q5F774', 'Q5F773', 'Q5F772', 'Q5F771', 'Q5F770', 'Q5F769', 'Q5F768', 'Q5F767', 'Q5F766', 'Q5F765', 'Q5F764', 'Q5F763', 'Q5F762', 'Q5F761', 'Q5F760', 'Q5F759', 'Q5F758', 'Q5F757', 'Q5F756', 'Q5F755', 'Q5F754', 'Q5F753', 'Q5F752', 'Q5F751', 'Q5F750', 'Q5F749', 'Q5F748', 'Q5F747', 'Q5F746', 'Q5F745', 'Q5F744', 'Q5F743', 'Q5F742', 'Q5F741', 'Q5F740', 'Q5F739', 'Q5F738', 'Q5F737', 'Q5F736', 'Q5F735', 'Q5F734', 'Q5F733', 'Q5F732', 'Q5F731', 'Q5F730', 'Q5F729', 'Q5F728', 'Q5F727', 'Q5F726', 'Q5F725', 'Q5F724', 'Q5F723', 'Q5F722', 'Q5F721', 'Q5F720', 'Q5F719', 'Q5F718', 'Q5F717', 'Q5F716', 'Q5F715', 'Q5F714', 'Q5F713', 'Q5F712', 'Q5F711', 'Q5F710', 'Q5F709', 'Q5F708', 'Q5F707', 'Q5F706', 'Q5F705', 'Q5F704', 'Q5F703', 'Q5F702', 'Q5F701', 'Q5F700', 'Q5F6Z9', 'Q5F6Z8', 'Q5F6Z7', 'Q5F6H4', 'Q5F6Z5', 'Q5F6Z4', 'Q5F6Z3', 'Q5F6Z2', 'Q5F6Z1', 'Q5F6Z0', 'Q9ZHD6', 'Q5F6Y8', 'Q5F6Y7', 'Q5F6Y6', 'Q5F6Y5', 'Q5F6Y4', 'Q5F6Y3', 'Q5F6Y2', 'Q5F6Y1', 'Q5F6Y0', 'Q5F6X9', 'Q5F6X8', 'Q5F6X7', 'Q5F6X6', 'Q5F6X5', 'Q5F6X4', 'Q5F6X3', 'Q5F6X2', 'Q5F6X1', 'Q5F6X0', 'Q5F6W9', 'Q5F6W8', 'Q5F6W7', 'Q5F6W6', 'Q5F6W5', 'Q5F6W4', 'Q5F6W3', 'Q5F6W2', 'Q5F6W1', 'Q5F6W0', 'Q5F6V9', 'Q5F6V8', 'Q5F6V7', 'Q5F6V6', 'Q5F6V5', 'Q5F6V4', 'Q5F6V3', 'Q5F6V2', 'Q5F6V1', 'Q5F6V0', 'Q5F6U9', 'Q5F6U8', 'Q5F6U7', 'Q5F6U6', 'Q5F6U5', 'Q5F6U4', 'Q5F6U3', 'Q5F6U2', 'Q5F6U1']
    



def info_uniprot():
    identifier=[]
    handle = open("C:/Users/Daniel Varzim/Documents/GitHub/Trab_Lab_Algoritmos/Informação sobre Neisseria gonorrhoeae/uniprot_proteome.txt")
    records = parse(handle) # Uses the function 'parse' from the module. 
    for record in records:
        for i in range(len(ID)):
            identifier.append([])
            if record["AC"]==ID[i]+";":
                #identifier.append([])
                identifier[i].append(ID[i])
                identifier[i].append(record["ID"])
                identifier[i].append(record["DE"])
                identifier[i].append(record["CC"])
    handle.close()
    return identifier


def more_info_uniprot():
    handle = open("C:/Users/Daniel Varzim/Documents/GitHub/Trab_Lab_Algoritmos/Informação sobre Neisseria gonorrhoeae/uniprot-proteome.xml")
    records=UniprotIO.UniprotIterator(handle,return_raw_comments=True)
    refs=[]
    for record in records:
        for i in range(len(ID)):
            if record.id==ID[i]:
                refs.append([ID[i]]+record.dbxrefs)#GO´s
    handle.close()
    return refs   


def Save_UniProt_IDs():
    IDs=ID
    save_file = open("Protein_IDs.txt", "w+")
    for id in IDs:
        save_file.write(str(id)+"\n")
    save_file.close
    


if __name__ == '__main__':
    #print (Get_Protein_IDs())
    #print(Get_Gene_IDs())
    #print(uniprot_ID())
    #Save_UniProt_IDs()
    #print(info_uniprot())
    print(more_info_uniprot())
    
    
    