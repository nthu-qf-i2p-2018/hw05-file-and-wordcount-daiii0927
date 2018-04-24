                                        # -*- coding: utf-8 -*-
import csv
import json
import string
from collections import Counter


def main(filename):
    txtfile= open(filename)
    lines = txtfile.readlines()

    all_words = []

   
    for line in lines:
        
        words = line.split

        
        for word in words:
          
            word = word.strip(string.punctuation)
           
            if word!=None and word!="" :
                
                all_words.append(word)

    
    counter =Counter(all_words)

    
    with open(...) as csv_file:
        
        writer = csv.writer(csv_file,delimiter=',')
        
        writer.writerow(['word':'count'])
        for i in list(all_words):
            writer.writerows([i,all_words.count(i)])
            
    with open("wordcount.json","w")as jsonfile:
        json.dump(counter,jsonfile)

    with open ("wordcount.pkl","wb") as pklfile:
        pickle.dump(counter,pklfile)



if __name__ == '__main__':
    main("i_have_a_dream.txt")
