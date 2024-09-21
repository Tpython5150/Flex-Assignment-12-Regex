'''
Python Regular Expression Deep Dive

Objective:
The aim of this assignment is to deepen your practical skills in Python's regular expressions, enhancing your ability toprocess and manipulate text data. You will tackle a variety of real-world scenarios, applying regex toextract, validate, and transform text efficiently.

Task 1: Email Enhancement
Problem Statement:
You have a script that extracts email addresses from a text but needs to be refined to exclude certain domains (e.g., '[exlcude.com](http://exclude.com/)') Modify the scripts to extract all email addresses except those from the specified domain.

code example:
'''
import re
# (?!exclude\.com|http://exclude\.com) had to look up solution not in my notes from chapter. 
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com, user4@http://exclude.com, tmccormick1510@gmail.com"
emails = re.findall(r"\b[A-Za-z0-9.%+-]+@(?!exclude\.com|http://exclude\.com\b)[A-Za-z0-9.-]+.[A-Za-z]{2,}\b", text)
print(emails)


