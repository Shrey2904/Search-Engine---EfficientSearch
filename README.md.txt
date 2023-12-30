
In this project I have created a Search Engine based on the racing motor sport - Formula one. I have downloaded multiple pages from wikipedia that are related to formula one. Here are the links to the pages:

1) https://en.wikipedia.org/wiki/Formula_One
2) https://en.wikipedia.org/wiki/Scuderia_Ferrari
3) https://en.wikipedia.org/wiki/Red_Bull_Racing
4) https://en.wikipedia.org/wiki/Mercedes-Benz_in_Formula_One
5) https://en.wikipedia.org/wiki/List_of_Formula_One_World_Drivers%27_Champions
6) https://en.wikipedia.org/wiki/List_of_Formula_One_driver_records
7) https://en.wikipedia.org/wiki/2023_Formula_One_World_Championship
8) https://en.wikipedia.org/wiki/History_of_Formula_One


I have implemented the trie data structure for my search engine which would store all the words and would tell us that if our searched word is present in our data structure or not. To make it work like a real search engine, I have added a feature for auto-complete that would ask the user if they want a suggestion based on the word they have entered. So if the user enters an incomplete word and if that word is a prefix for some words then my program would give the user all the suggestions that have the prefix as the word the user has entered.

Once we get the complete word from the user, the program would show the search result to the user and the pages are ranked based on the count of occurence of that particular word in all the input pages. So if a particular word appears the most in a page then that page will be ranked 1 and would be shown at the top so the pages are sorted in a descending order. The user should enter a single word.

Once the user chooses to exit the program, all the words that the user has searched and which were present in our data structure would be stores in an output file with the word and its corresponding search result which are the pages in which the word was found.

To run the code simply run the .py file. For more reference I have also submitted the .ipynb file of my code. You might have to change the file paths to read the pages that I have downloaded.

If the video format isn't compatible with your system then you can also watch it here: https://drive.google.com/file/d/1OXvML9DgMLdVIzh9HpOfNNzl1goWeI1t/view?usp=sharing

Thank you!