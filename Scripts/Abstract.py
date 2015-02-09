# -*- coding: utf-8 -*-

'''
Created on 05/02/2015

@author: Daniel Varzim
'''
from Bio import Entrez
Entrez.email = "pg27662@alunos.uminho.pt"    

# invoke ESearch, using history
search_handle = Entrez.esearch(db="pubmed", term="Neisseria gonorrhoeae",
                               reldate=365, datetype="pdat",
                               usehistory="y")
search_result = Entrez.read(search_handle)
search_handle.close()

# save the count and webenv & query_key referencing the ESearch history
count = int(search_result["Count"])
webenv = search_result["WebEnv"]
query_key = search_result["QueryKey"] 
print("Fetching %i records using webenv=%s, query_key=%s" % (count, webenv, query_key))

# invoke EFetch to retrieve count records, batch_size at a time, using the webenv & query_key values rather than the UIDs
batch_size = 10
out_handle = open("recent_Neisseria_papers.txt", "w")
for start in range(0, count, batch_size):
    end = min(count, start + batch_size)
    print("Fetching records %i thru %i" % (start + 1, end))
    fetch_handle = Entrez.efetch(db="pubmed",
                                 rettype="medline", retmode="text",
                                 retstart=start, retmax=batch_size,
                                 webenv=webenv,
                                 query_key=query_key)
    data = fetch_handle.read()
    fetch_handle.close()
    out_handle.write(data)
out_handle.close()