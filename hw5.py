                                        # -*- coding: utf-8 -*-
import csv
import json
import pickle
import string
from collections import Counter


def main(filename):
    txtfile= open(filename)
    lines = txtfile.readlines()

    all_words = []

   
    for line in lines:
        
        words = line.split()
        line=line.strip
        
        for word in words:
          
            word = word.strip(string.punctuation)
           
            if word!=None and word!="" :
                
                all_words.append(word)

    
    count = Counter(all_words)

    
    with open("wordcount.csv","w",newline="") as csv_file:
        
        writer = csv.writer(csv_file,delimiter=',')
        
        writer.writerow(['word','count'])
        for i in list(all_words):
            writer.writerow([i,count [i]])

            
    with open("wordcount.json","w")as jsonfile:
        json.dump(count,jsonfile)

    with open ("wordcount.pkl","wb") as pklfile:
        pickle.dump(count,pklfile)




if __name__ == '__main__':
    main("i_have_a_dream.txt")
