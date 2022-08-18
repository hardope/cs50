#import collections

contents = []
new_list = []

while True:
    try:
        line = input()
        contents.append(line)

    except:
        break

import collections

contents = []
new_list = []

while True:
    try:
        line = input()
        contents.append(line)

    except:
        break

#counter = collections.Counter(contents)

for i in contents:
    if i not in new_list:
        new_list.append(i)


print("\n")

new_list.sort()
for i in new_list:
    print(i)



for i in contents:
    if i not in new_list:
        new_list.append(i)


print("\n")

new_list.sort()
for i in new_list:
    print(i)

