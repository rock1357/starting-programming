#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 17:31:17 2022

@author: riccardosciarra
"""



dati = [1, 2, 3, 4]

def my_function():
    for dato in dati:
        
        print(dati[dato])
           
    
        
my_function()

#%%

"the error is fixed: dato comincia da dato=1 mentre l'array ha dati[0] che non verrà visualizzato"
" perciò l'ultimo numero che visualizziamo: dati(dato=4) non esiste."
"Per trovare l'errore è risultato utile usare l'ipython debugger che viene invocato tramite il comando '%run -d nomefile.py' "



dati = [1, 2, 3, 4]

def my_function():
    for dato in dati:
        
        print(dati[dato-1])
           
    
        
my_function()