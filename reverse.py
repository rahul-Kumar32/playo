# # reverse a string using string slicing
#
# # def strreve(x):
# #     return x[::-1]
# #
# # nwtxt = strreve("rahul")
# #
# # print(nwtxt)
# #
# # reverse a string in one line
# # text = "hello world" [::-1]
# # print(text)
# #
# # reverse a sentence
# # a = input("enter a string :")
# # print (a[::-1])
#
# # reversing a sentence
#
# def revsent(sentence):
#
#     words = sentence.split(' ')
#
#     rever_sent = ' '.join(reversed(words))
#
#     return rever_sent
# if __name__ == '__main__':
#     inp = input("enter a string:")
#
#     print(revsent(inp))

# removinfg i'th character from string

# oldstr = "geeksforgeeks"
#
# print("the string is :" + oldstr)
#
# nwstr = oldstr[:2] + oldstr[3:]
#
# print(nwstr)

# removinfg i'th character from string naive method

# oldstr = "geeksforgeeks"
#
# print("the string is :" + oldstr)
#
# nwstr = ''
#
# for i in range(len(oldstr)):
#     if i!=2:
#         nwstr = nwstr + oldstr[i]
#
# print(nwstr)
#
# length of a sting without using len function and using for loops

# def findlen(stri):
#
#     counter = 0
#     for i in stri:
#
#         counter += 1
#
#     return counter
#
# stri = "rahulkumar"
#
# print(findlen(stri))





# reverse a string using for loop

my_str ="rahul is a good boy"

list1 = list(''.join(my_str))

rev1 = list1[:]

for i in range(len(rev1)//2):
    rev1[i], rev1[len(rev1)-i-1] = rev1[len(rev1)-i-1], rev1[i]


print(f"My Third reversed list of {my_str} is {rev1}")








