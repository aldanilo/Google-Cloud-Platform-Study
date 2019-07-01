# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:31:33 2019

@author: danilosouza
"""
import pandas as pd
import time
start = time.time()

size =1
reader = pd.read_csv('empresas.csv', chunksize = size,dtype = str)
cnpjs = pd.read_csv('cnpjs_list.csv',dtype = str)
user_log_chunk = next(reader)
cnpjs_achados =  pd.DataFrame(data=None, columns=user_log_chunk.columns)


j=1
size =100000 
reader = pd.read_csv('empresas.csv', chunksize = size,dtype = str)
for chunk in pd.read_csv('empresas.csv', chunksize = size,dtype = str):
    user_log_chunk = next(reader)
    user_log_chunk['found'] = user_log_chunk['cnpj'].isin(cnpjs['Cnpj 14 Digitos'])
    achados = user_log_chunk.loc[user_log_chunk['found'] == True]
    del user_log_chunk['found']
    del achados['found']
    cnpjs_achados = pd.concat([cnpjs_achados,achados],sort = False)
    del(user_log_chunk)  
    print(str(size*j))
    j += 1
    if(len(cnpjs_achados) == len(cnpjs)):
        break

lista_cnpjs_achados = cnpjs_achados['cnpj']

cnpjs['achado?'] = cnpjs['Cnpj 14 Digitos'].isin(lista_cnpjs_achados)
cnpjs_achados_ = cnpjs.loc[cnpjs['achado?'] == True]
cnpjs_NAO_achados = cnpjs.loc[cnpjs['achado?'] == False]

if(len(cnpjs_NAO_achados) == 0):
    print('todos os cnpjs foram achados!')
    cnpjs_achados.to_csv('cnpjs_achados.csv', encoding = 'utf-8', index = False)   
else:
    print(str(len(cnpjs_NAO_achados)) + ' cnpjs não foram achados.')
    print(str(len(cnpjs_achados)) + ' cnpjs foram achados.')
    cnpjs_achados.to_csv('cnpjs_achados.csv', encoding = 'utf-8', index = False) 
    cnpjs_NAO_achados.to_csv('cnpjs_NAO_achados.csv', encoding = 'utf-8', index = False)
    
end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))    


