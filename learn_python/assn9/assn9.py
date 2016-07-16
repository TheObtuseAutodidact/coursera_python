"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""
import pdb
#  Starter code

# name = raw_input("Enter file: ")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
#
# ############################
# solution_dict = {}
# solution_lst = []
#
# for line in handle:
#     if "From " in line:
#         # pdb.set_trace()
#         time = line.split()[5].split(":")[0]
#         solution_dict[time] = solution_dict.get(time, 0) + 1
#
# for kee, val in sorted(solution_dict.items()):
#     print kee, val
#

def sum_mul(n, m):
    sol_lst = ()
    if (n > m):
        for each in range(m):
            if each % n == 0:
                sol_lst.append(each)
    else:
        return "INVALID"
    return sum(sol_list)

print sum_mul(2, 5)

#
# Desired Output
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
