#!/usr/bin/env python
# coding: utf-8

# ### CS600 PROJECT  - SHREY TANNA

# ### ---------------------------------------------------------------------------------------

# ### FINAL VERSION

# ### Function to process the html pages to extract words

# In[1]:


from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from collections import Counter
# nltk.download('stopwords')
import re
import os


def extract_words_from_html(path):
    with open(path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Now we have the data from our HTML file that we have stored locally and we need to parse HTML content for our processing
    res = BeautifulSoup(html_content, 'html.parser')
    
    # Using beautiful soup we have extracted the text from our HTML file
    text = res.get_text()
    
    # We only need words that have alphabets from A-Z and a-z and in our data and ignore all the other symbols hence we tokenize the text into words
    words = re.findall(r'\b[A-Za-z]+\b', text)
    
    # We remove all the stop words from our data using NLTK's list of stop words
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
    
    # We can see the difference in number of words before and after removing the stop words 
    print("Number of words before removing the stop words:", len(words))
    print("Number of words after removing the stop words:", len(filtered_words))
    
    #To count the occurences of all the words, we create a Counter object and then convert it to a dictionary
    word_occurrences = Counter(filtered_words)
    word_occurrences = dict(word_occurrences)
    # word_occurrences
    return word_occurrences


# ### Reading all the pages from local storage

# In[2]:


files = [r"C:\Users\SHREY\OneDrive\Desktop\STEVENS SUBJECTS\CS 600 ADV ALGO\PROJECT\Formula One - Wikipedia.html", r"C:\Users\SHREY\OneDrive\Desktop\STEVENS SUBJECTS\CS 600 ADV ALGO\PROJECT\History of Formula One - Wikipedia.html",
        r"C:\Users\SHREY\OneDrive\Desktop\STEVENS SUBJECTS\CS 600 ADV ALGO\PROJECT\Mercedes-Benz in Formula One - Wikipedia.html", r"C:\Users\SHREY\OneDrive\Desktop\STEVENS SUBJECTS\CS 600 ADV ALGO\PROJECT\Red Bull Racing - Wikipedia.html",
        r"C:\Users\SHREY\OneDrive\Desktop\STEVENS SUBJECTS\CS 600 ADV ALGO\PROJECT\2023 Formula One World Championship - Wikipedia.html", r"C:\Users\SHREY\OneDrive\Desktop\STEVENS SUBJECTS\CS 600 ADV ALGO\PROJECT\Scuderia Ferrari - Wikipedia.html",
        r"C:\Users\SHREY\OneDrive\Desktop\STEVENS SUBJECTS\CS 600 ADV ALGO\PROJECT\List of Formula One driver records - Wikipedia.html", r"C:\Users\SHREY\OneDrive\Desktop\STEVENS SUBJECTS\CS 600 ADV ALGO\PROJECT\List of Formula One World Drivers' Champions - Wikipedia.html"]

words_in_pages = {}

for path in files:
    print(f"PROCESSING FILE: {os.path.basename(path)}")
    word_occurrences = extract_words_from_html(path)
    words_in_pages[os.path.basename(path)] = word_occurrences
    print('\n')


# In[3]:


class TNode:

    def __init__(self):
        self.children = {}
        self.flag = False
        self.DataFound = []
        
class Trie:
    def __init__(self):
        self.root = TNode()
    
    def insert(self, word, pages):
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TNode()
                
            curr = curr.children[c]
        curr.flag = True
        curr.DataFound.append(pages)
    
    def search(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
#                 return 'Not Found 1'
                return """
                                    Not Found"""
            curr = curr.children[c]
        if curr.flag:
            return curr.DataFound, word
#         else:
#             return "Not Found 2"
        while True:
            try:
                option = int(input("Would you like the available suggestions: \n\n1: yes \n0: no\n\nChoice: "))
                if option == 1:
                    output = self.suggest(word)
                    #return(output)
                    print("\nPlease type in the word from the below suggestion list:\n\n",output)
                    print('\nSuggested successfully!!')
                    suggest_accepted = input("\nIf you want to search for any above sugestions please enter from the above given: \n\nNew Word: ").lower()
                    return (self.search(suggest_accepted))
                
                elif option == 0:
                    return 'Not Found 3'
                
                else:
                    print("\nPLEASE ENTER 0 OR 1\n")
            except ValueError:
                print("\nPLEASE ENTER 0 OR 1\n")


        
                    #THIS WOULD SORT OF BE LIKE AUTCOMPLETE WHERE IT WOULD ASK THE USER IF IT MEANT ANY OF THE FOLLOWING SUGGESTIONS OR NOT
        
    def suggest(self,prefix):
        suggestions = []
        curr = self.root
        
        for c in prefix:
            if c not in curr.children:
                return suggestions
            curr = curr.children[c]
        
        self.dfs(curr,prefix,suggestions)
        return suggestions
    
    def dfs(self,node, prefix, suggestions):
        if node.flag:
            suggestions.append(prefix)
        
        for c, ref_node in node.children.items():
            self.dfs(ref_node, prefix + c, suggestions)


# In[4]:


t = Trie()
l = 0
for k in words_in_pages:
    for word in words_in_pages[k].keys():
        t.insert(word,k)


# In[5]:


import pandas as pd
from tabulate import tabulate
# import warnings
# warnings.filterwarnings('ignore')



#Creating a txt file to store our output
txt_path = r"C:\Users\SHREY\OneDrive\Desktop\STEVENS SUBJECTS\CS 600 ADV ALGO\PROJECT\output.txt"



#Before adding new data to our txt file we need to clear it by opening the file in 'write' format
with open(txt_path,'w') as file:
    file.write("")
    
  
research = 1
while research:
    word_to_search = input('\nEnter the word you want to search: \nWord: ').lower()
    search_result = t.search(word_to_search)
    df = pd.DataFrame(columns=['PAGES', 'OCCURENCES'])
    # search_result
    # print(len(search_result))
    if len(search_result) == 2:
        pages , word = search_result
        for page in pages:
            occurences = words_in_pages[page][word]
            res_df = pd.DataFrame({'PAGES': [page], 'OCCURENCES': [occurences]})
            #df = df.append({'PAGES' : page, 'OCCURENCES' : occurences}, ignore_index = True)
            df = pd.concat([df,res_df], ignore_index=True)
        df = df.sort_values(by=['OCCURENCES'], ascending=False)
#         print(df)
        
        
        #Converting the dataframe to a table
        data_table = tabulate(df, headers='keys', tablefmt='grid', showindex=False)
        print('\nResult:\n', data_table)
        
        #Saving the dataframe to txt file
#         txt_path = r"C:\Users\SHREY\OneDrive\Desktop\STEVENS SUBJECTS\CS 600 ADV ALGO\output.txt"
        with open(txt_path, 'a') as file:
            file.write(f"Search Results for: {word}\n\n")
            file.write(data_table + '\n\n' + '-'*100 + '\n\n')
        
        print("Data Saved")

        
        while True:  
            research = input("\n\n\t\t\tDo you want to keep searching?: \n\n\t\t\t1: yes\n\t\t\t0: no\n\n\t\t\tChoice: ")
            if research == '1' or research == '0':
                research = int(research)
                break
            else:
                print("\n\t\t\tInvalid input. Please enter 1 or 0. Retry.")
    else:
        print(search_result)
#         research = 0
        while True:  
            research = input("\n\n\t\t\tDo you want to keep searching?: \n\n\t\t\t1: yes\n\t\t\t0: no\n\n\t\t\tChoice: ")
            if research == '1' or research == '0':
                research = int(research)
                break
            else:
                print("\n\t\t\tInvalid input. Please enter 1 or 0. Retry.")

else:
    with open(txt_path, 'a') as file:
        file.write("\n\n\t\t\t\t\t\tThank you for using my search engine :)")
    print("\n\n\t\t\tThank you for using my search engine :)")
    print("\n\n\t\t\tSearch Results downloaded at defined location :)")


# In[ ]:




