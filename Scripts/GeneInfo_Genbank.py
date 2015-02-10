# -*- coding: utf-8 -*-


'''
Created on 05/02/2015

@author: Daniel Varzim
'''
import os
from Bio import SeqIO
import shutil


def Get_IDs():
    path = "C:/Users/Daniel Varzim/Documents/GitHub/Trab_Lab_Algoritmos/Resultados/gb records/"
    IDs=[]
    for filename in os.listdir(path):
        result_handle= open(path+filename)
        record = SeqIO.read(result_handle, format="genbank")
        IDs.append(record.id)
        result_handle.close
    return IDs

def Save_IDs():
    IDs=Get_IDs()
    save_file = open("Gene_IDs.txt", "w+")
    for ID in IDs:
        save_file.write(str(ID)+"\n")
    save_file.close
    


def Get_Prtotein_Names():
    path = "C:/Users/Daniel Varzim/Documents/GitHub/Trab_Lab_Algoritmos/Resultados/gb records/"
    Names=[]
    for filename in os.listdir(path):
        result_handle= open(path+filename)
        record = SeqIO.read(result_handle, format="genbank")
        Names.append(record.description)
        result_handle.close
    return Names


def Save_Protein_Names():
    Names=Get_Prtotein_Names()
    save_file = open("Protein_Names.txt", "w+")
    for Name in Names:
        save_file.write(str(Name)+"\n")
    save_file.close    
    
 

def Get_Gene_lenght():
    path = "C:/Users/Daniel Varzim/Documents/GitHub/Trab_Lab_Algoritmos/Resultados/gb records/"
    lenghts=[]
    for filename in os.listdir(path):
        result_handle= open(path+filename)
        record = SeqIO.read(result_handle, format="genbank")
        lenghts.append(len(record.seq))
        result_handle.close
        
    return lenghts

def Save_Gen_Lenght():
    lenghts=Get_Gene_lenght()
    save_file = open("Gene_lenghts.txt", "w+")
    for lenght in lenghts:
        save_file.write(str(lenght)+"\n")
    save_file.close


def Get_Gene_Location():
    path = "C:/Users/Daniel Varzim/Documents/GitHub/Trab_Lab_Algoritmos/Resultados/gb records/"
    Location=[]
    for filename in os.listdir(path):
        result_handle= open(path+filename)
        record = SeqIO.read(result_handle, format="genbank")
        for i in range(len(record.features)):
            mylocation = record.features[i]
            if mylocation.type == "CDS":
                Location.append(mylocation.qualifiers["coded_by"][0])
        result_handle.close
    
    return Location


def Save_Gene_Location():
    Locations= Get_Gene_Location()
    save_file = open("Gene_Location.txt", "w+")
    for location in Locations:
        save_file.write(str(location)+"\n")
    save_file.close

def Get_CDD():
    path = "C:/Users/Daniel Varzim/Documents/GitHub/Trab_Lab_Algoritmos/Resultados/gb records/"
    CDD=[]
    for i in range(225):
        CDD.append([])
    i=0
    for filename in os.listdir(path):

        result_handle= open(path+filename)
        record = SeqIO.read(result_handle, format="genbank")
        CDD.append([])
        for j in range(len(record.features)):
            my_cdd = record.features[j]
            if my_cdd.type == "Region" or my_cdd.type == "Site":
                if "db_xref" in my_cdd.qualifiers:
                    CDD[i].append(my_cdd.qualifiers["db_xref"][0])
        i+=1
        result_handle.close
        
    return CDD    

def Save_CDD():
    CDD= Get_CDD()
    save_file = open("Gene_CDD.txt", "w+")
    for cdd in CDD:
        save_file.write(str(cdd)+"\n")
    save_file.close


if __name__ == '__main__':
    #print(Get_IDs())
    #Save_IDs()
    #for name in Get_Prtotein_Names():
        #print(name)
    #Save_Protein_Names()
    #print(Get_Gene_lenght())
    #Save_Gen_Lenght()
    #print(Get_Gene_Location())
    #Save_Gene_Location()
    #print(Get_CDD())
    Save_CDD()
    pass