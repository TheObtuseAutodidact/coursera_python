"""
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
Check Code
"""
import pdb
#  Starter code

name = raw_input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

##########################

solution_dict = {}

for line in handle:
    if "From " in line:
        name = line.split()[1]
        solution_dict[name] = solution_dict.get(name, 0) + 1

max_sender = None
max_sent = None

for key, val in solution_dict.items():
    if val > max_sent:
        max_sender = key
        max_sent = val

print max_sender, max_sent
