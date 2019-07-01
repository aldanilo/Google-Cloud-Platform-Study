# -*- coding: utf-8 -*-

f = open('Page3.txt','r',encoding="utf-8")
message = f.read()

message = message.strip()


import nltk.data
from nltk import tokenize
from nltk.corpus import stopwords
import pandas as pd


#tokenizer = nltk.data.load('tokenizers/punkt/portuguese.pickle')

frases = tokenize.sent_tokenize(message,language='portuguese')

words = nltk.word_tokenize(message,language='portuguese')

sent_pos = nltk.pos_tag(message.split())

#grammar = 'NumericalPhrase: {<NN|NNS>?<RB>?<JJR><IN><CD><NN|NNS>?}'
#parser = nltk.RegexpParser(grammar)

x = list()
for elem in sent_pos:
    if(elem[1] == "CD"):
        x.append(elem)
import re   
money = list()
date = list()  

for elem in x:   
    if re.match("[0-9]+(\.[0-9][0-9][0-9])+(\,)+([0-9][0-9])?",elem[0]):   #for money
        money.append(elem[0])   
    elif re.match("([0-9])+(\,)+([0-9][0-9])",elem[0]):
        money.append(elem[0])  
    if re.match("[0-9][0-9]+(\/)+[0-9][0-9]+(\/)+([0-9][0-9]?)",elem[0]):   #for date
        date.append(elem[0])    
        
frase_com_money = list()   
frase_com_data = list()    
for frase in frases:
    for elem in money:
        if elem in frase:
            frase_com_money.append(frase)
        
    for elem2 in date:
        if elem2 in frase:
            frase_com_data.append(frase)


sr = stopwords.words('portuguese')
frase_com_money_resumida = list()
for frase in frase_com_money:
    frase_tokens = nltk.word_tokenize(frase,language='portuguese')
    
    for token in frase_tokens:
        if token in stopwords.words('portuguese'):
            frase_tokens.remove(token)
    
    
    frase_tokens = nltk.pos_tag(frase_tokens)
    frase_meaning = list()
    for word in frase_tokens:
        if (word[1] == 'NNP' or word[1] == 'VBZ' or word[1] == 'NNS' or word[1]== 'NN' or word[1]== 'CD'):
            frase_meaning.append(word[0])
    sentence = ' '.join(frase_meaning)
    frase_com_money_resumida.append(sentence)


final_table = pd.DataFrame()

final_table['Valor'] = money
final_table['Frase'] = frase_com_money_resumida

final_table2 = pd.DataFrame()
final_table2['Valor'] = money
final_table2['Frase'] = frase_com_money_resumida

final_table3 = pd.DataFrame()
final_table3['Valor'] = money
final_table3['Frase'] = frase_com_money_resumida

final_table = pd.concat([final_table, final_table2], ignore_index=True)
final_table = pd.concat([final_table, final_table3], ignore_index=True)



final_table.to_csv("pdf_analise.csv",encoding='utf-8', index=False)
