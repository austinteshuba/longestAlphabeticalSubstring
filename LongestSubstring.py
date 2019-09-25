# LongestSubstring.py
# Assumptions:
# If an empty or null string is passed, return ''
# May input capital letters, should be compared as lowercase
# Input does not contain spaces
# if there are multiple substrings of the same length, use the first occurence
# Consecutive letters can be included
# Strategy:
# Store current longest substring
# Iterate through the string's letters (O(n)) and check letter's alpha order
# This has a space complexity of O(1).
# Other Considerations:
# Sorting the list is nlogn and will not improve runtime.
# It would also lead to an incorrect solution
# Since the order given matters, we can't load frequency into a hashtable
# Since we don't need to return all alphabetical substrings, we don't need
# a second hashtable.

inputString = input("Enter the string you wish to check")


def longestSubstring(string):
    #Null check
    if (string == None or len(string) == 0):
        return ''

    #Edge case: If the length is one, return the string
    if (len(string) == 1):
        return string

    substring = ""
    longestSubstring = ""
    for i in range(len(string)):
        if substring == "":
            substring = string[i]
        else:
            if (ord(string[i].lower()) >= ord(substring[-1])):
                substring += string[i]
            else:
                substring = string[i]
        if len(substring) > len(longestSubstring):
            longestSubstring = substring
    return longestSubstring

print(longestSubstring(inputString))













        
    
