# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:59:16 2020

@author: CNU074VP
"""

from __future__ import print_function

import pandas as pd
import numpy as np
from scattertext import CorpusFromParsedDocuments
from scattertext import chinese_nlp
from scattertext import produce_scattertext_explorer
import jieba
import re
import os

def get_scattertext_html():
    file_names = os.listdir('C:/Users/CNU074VP/Desktop/Chinese Topic Model/protein review')
    
    # Create Dictionary for File Name and Text
    file_name_and_text = {}
    for file in file_names:
        with open('C:/Users/CNU074VP/Desktop/Chinese Topic Model/protein review/' + file, "r", encoding="UTF-8") as target_file:
             file_name_and_text[file] = target_file.read()
    file_data = (pd.DataFrame.from_dict(file_name_and_text, orient='index')
                 .reset_index().rename(index = str, columns = {'index': 'file_name', 0: 'text'}))
    
    
    df = file_data
    
    for i in np.arange(len(df)):
        df['text'][i] = "\n".join(list(dict.fromkeys(df['text'][i].split("\n"))))   #Remove duplicates
        
    
    
    comment = df.text.values.tolist() 
    
    #load user-defiend dictionary
    jieba.load_userdict('C:/users/CNU074VP/dict_out.csv')
    
    #word segmentation with jieba
    comment_s = []
    # pattern = re.compile(r'[\u4e00-\u9fa5]+')   #Get rid of non-Chinese string, need to keep 换行符\n
    
    pattern = re.compile('\<.*?\>')  #正则去除淘宝评论里<>里边的内容
    for line in comment:
        line.replace(' ','')
        # line = ''.join(re.findall(pattern, line))
        line = ''.join(re.sub(pattern, '', line))
        comment_cut = jieba.lcut(line)
        comment_s.append(comment_cut)  
    
    # load user-defined stop words list
    stopwords = pd.read_excel('C:/users/CNU074VP/PycharmProjects/tmall_spider/stopwords.xlsx')
    stopwords = stopwords.stopword.values.tolist()
    
    # get rid of stop words
    comment_clean = []
    for line in comment_s:
        line_clean = []
        for word in line:        
            if word not in stopwords:
                line_clean.append(word)
        comment_clean.append(line_clean)
    
    comment_doc = []    
    def get_single_doc(num):    
        for i in np.arange(len(comment_clean[num])):
            comment_doc = ' '.join([str(item) for item in comment_clean[num]])
        return comment_doc

        
    l_series = []
    for i in np.arange(len(df)):
        l_series.append(pd.Series(get_single_doc(i)))
        
    
    cleaned_texts = pd.concat(l_series, ignore_index=True).to_frame().rename(columns = {0 : "parsed_text"}).reset_index(drop=True)
    
    original_data = df.reset_index(drop=True)
    
    df = pd.concat([original_data, cleaned_texts],  axis=1)
    
    df['parsed_text'] = df['parsed_text'].apply(chinese_nlp)
    
    for i in np.arange(len(df['text'])):
        df['text'][i] = re.sub(pattern, '', df['text'][i])
        
    
    df['text'] = df['text'].apply(chinese_nlp)
    
    corpus = CorpusFromParsedDocuments(df,
                                       category_col='file_name',
                                       parsed_col='parsed_text').build()
    
    html = produce_scattertext_explorer(corpus,
                                        category='安利蛋白粉评论.txt',
                                        category_name='安利蛋白粉评论.txt',
    	                                not_category_name='汤臣倍健蛋白粉评论.txt',
    	                                width_in_pixels=1000,
    	                                metadata=df['file_name'],                                 
    	                                asian_mode=True,
                                        alternative_text_field = "text")
    result = open('D:/scattertext/protein_review_compare.html', 'w', encoding='utf-8').write(html)
    
    return result