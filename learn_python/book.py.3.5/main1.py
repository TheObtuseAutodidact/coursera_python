# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print('Line Count:', count)

# fhand = open('mbox.txt')
# inp = fhand.read()
# print(len(inp))
#
# print(inp[:20])

# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)

# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.find('@uct.ac.za') == -1 : continue
#     print(line)

# fname = input('Enter the file name: ')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count + 1
# print('There were', count, 'subject lines in', fname)

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
# I think this could go under and else
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print('There were', count, 'subject lines in', fname)
