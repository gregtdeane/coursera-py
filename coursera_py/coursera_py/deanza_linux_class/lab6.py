# Name: Gregory Tuayev-Deane   
# Description: 

import string

# Write a few sentences about how you hope to use what you've learned in this class in the future. You can write
# whatever you'd like, but make sure your response is at least 3 sentences long to have enough text. Store your response
# in a variable and write it out to a file called response.txt

my_response = '''I work as a system integration engineer and frequently use python every day. 
However, I have never taken a formal Python class until now and this class has been a great way to get a formal foundation in Python. 
I plan to take more Python classes so that I can more fluently automate a lot of the tasks I do daily.'''

with open(file='response.txt',mode='w') as my_file:
    my_file.write(my_response)


# Prompt the user to search for a word to see how many times it occurred in the text
search_word = input("Please enter the word you'd like to search for in the file: ").lower()

# Read in the text from the file back into a variable
with open(file='response.txt', mode='r') as file_r:
    # print(file_r)
    file_str = file_r.read().lower()
    

print(file_str)
trans_table = str.maketrans('','',string.punctuation)
file_str_stripped = file_str.translate(trans_table)
words = file_str_stripped.split()
print(words)
word_count_list = [words.count(word) for word in words]
freq_dict = {word: count for word, count in zip(words, word_count_list)}
print(freq_dict)
    


user_word_count = freq_dict[search_word]

# most_common = sorted(freq_dict.values)

with open(file='response.txt', mode='a') as file_a:
    file_a.write(f"\n\nThe word you entered, '{search_word}', occured {user_word_count} times\n")
    # file_a.write(f"The 5 most common words are {most_common}")
    
