# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 21:26:29 2022

@author: kevin
"""
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from sklearn.base import BaseEstimator, TransformerMixin, ClassifierMixin
import pandas as pd
import inflect
from sklearn.feature_extraction.text import CountVectorizer

#Pasamos a minuscula
def minuscula(text):
  texto =[]
  for word in text:
    textos= word.lower()
    texto.append(textos)
  listToStr = ''.join([str(elem) for elem in texto]) 
  return listToStr  

#Eliminamos los números
def numeros(text):
  x=inflect.engine()
  texto = []
  for word in text :
      word.replace(" ","")
      if word.isdigit():
         textos=x.number_to_words(word)
         texto.append(textos)
      else:
         texto.append(word)    
  return texto   

def preprocesamiento(text):
  texto = minuscula(text)
  #texto = numeros(texto)
  return texto

def limpieza_tokens(df):
  tokenizer = RegexpTokenizer(r'\w+')
  lemmatizer = WordNetLemmatizer()
  list_token = []
  for text in df['text']:
      # tokenize it 
      result = []
      results = tokenizer.tokenize(text)
      for word in results:
          # lemmatize it 
          words = lemmatizer.lemmatize(word)
          result.append(words)
      list_token.append(result)

  #Lista de stopwords
  count_vec = CountVectorizer(input='content', stop_words='english')
  stopw = set(count_vec.get_stop_words())

  #Eliminamos artículos, conjunciones, preposiciones, etc

  for a in range(0,len(list_token)-1):
    borrables = []
    for b in range(0,len(list_token[a])-1):
      if list_token[a][b] == 'm' or list_token[a][b] == 's' or list_token[a][b] == 've' or list_token[a][b] == 'don' or list_token[a][b] == 't' or list_token[a][b] == 'd' or list_token[a][b] == 'll' or list_token[a][b] in stopw:
        borrables.append(list_token[a][b])
    for c in borrables:
      list_token[a].remove(c)

  lst = []
  for i in list_token:
      listToStr = ' '.join([str(elem) for elem in i]) 
      lst.append(listToStr)
  return lst

#Clase de la transformación del texto
class Texto_Basico(BaseEstimator,TransformerMixin):
    def __init__(self):
        pass

    def fit(self,X,y=None):
        return self
    
    def transform(self,X,y=None):
        X = pd.DataFrame(X).copy()
        X['text'] = X['text'].apply(preprocesamiento)
        return X
    
#Clase de la tokenización y retoques finales
class Texto_Definitivo(BaseEstimator,TransformerMixin):
    def __init__(self):
        pass

    def fit(self,X,y=None):
        return self
    
    def transform(self,X,y=None):
        print(X.head(10))
        X = pd.DataFrame(X).copy()
        X['text'] = limpieza_tokens(X)
        print(X.info())
        return X