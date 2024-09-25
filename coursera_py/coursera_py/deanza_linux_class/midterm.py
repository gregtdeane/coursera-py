# age = input("Enter an age: ")
# movie_ratings = {"G":0, "PG":7,"PG-13":13,"R":17}
# print(movie_ratings)
# for key,val in movie_ratings:
#     if age >val:
#         atleast_movie_rating = key
#     if age<val:
#         max_movie_rating = atleast_movie_rating

# print("You can watch: ", max_movie_rating)



#########################################################
# vowels = "aeiouAEIOU"
# name1 = input("Enter a first name: ")
# name2 = input("Enter another first name: ")
# name3 = input("Enter another first name: ")

# name1_vowel_count = sum(name1.count(vowel) for vowel in vowels)
# name2_vowel_count = sum(name2.count(vowel) for vowel in vowels)
# name3_vowel_count = sum(name3.count(vowel) for vowel in vowels)

# print("Name with most vowels: ", max([name1_vowel_count,name2_vowel_count,name3_vowel_count]))


#########################################################################
# NY_temp = int(input("Enter high temp for New York: "))
# LA_temp = int(input("Enter high temp for Los Angeles: "))
# Chi_temp = int(input("Enter high temp for Chicago: "))
# Houston_temp = int(input("Enter high temp for Houston: "))
# Pheonix_temp = int(input("Enter high temp for Pheonix: "))

# temp_dict = {"NY":NY_temp, "LA":LA_temp, "CHI":Chi_temp, "HOU":Houston_temp, "PNX":Pheonix_temp}
# Keymax = max(zip(temp_dict.values(), temp_dict.keys()))[1]
# Keymin = min(zip(temp_dict.values(), temp_dict.keys()))[1]
# print("Max temp city: ", Keymax)
# print("Min temp city: ", Keymin)

###########################################################################
# import math
# int_list = []
# entered_int = int(input("Enter first int. Enter n to quit"))
# int_list.append(entered_int)
# while entered_int != "n":
#     next_int = input("Enter some integers. Enter 'n' to stop entering ints:")
#     if next_int == "n":
#         break
#     else:
#         int_list.append(int(next_int))

# old_sum = 0
# el_cntr = 0
# for el in int_list:
#     new_sum = el + old_sum
#     old_sum = new_sum
#     el_cntr = el_cntr+1

# avg = new_sum/el_cntr
# print("Average is ", avg)
    



# int_list_avg = sum(int_list)/len(int_list)
