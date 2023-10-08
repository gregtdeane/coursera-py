import re 
# ( - beginning of extraction 
# ) - end of extraction
# . match any char
# [aef83] - matches any character in set
# ^ - beginning of line
# [^XYZ] - matches a single character not in listed set
# square bracket is compared to single character

#re.search(pattern, searchable_text)  to see if a string matches reg ex - returns boolean - similar to find
#re.findall(pattern, searchable_text)  extract portions of a string that match the reg ex - returns list of string

#greedy matching
#unless you specify otherwise, regex library tries to give largest possible version of string 
#that you are matching
# e.g. .+ want to be as big as possible and still match - wildcards are very pushy outwards
# asterisk or plus - are greedy
# prevent greedy behavior with '?' - question mark

  # \ exit character

  




