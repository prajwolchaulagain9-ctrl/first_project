# def extract_firstwords(new_file):
#     first_words= []
#     opened= open(new_file,'r')
#     for line in opened:
#         first_word= line.split()[0]
#         first_words.append(first_word)
#     opened.close()
#     return first_words
# print(extract_firstwords('sample.txt'))

# with open('sample.txt','r') as f ,open('dest.txt','w') as d:
#     for line in f.readlines():
#         d.writelines(line)     


# with open("story.txt",'r') as f:
#     line_num=1
#     total_words=0
#     for line in f.readlines():
#         no_words= len(line.split())
#         print(f"line{line_num} has {no_words} words")
#         line_num=line_num+1
#         total_words= total_words+no_words
#     print("There are ",str(total_words),"words in the file")
    

    

# with open("numbers.txt","r") as f, open("squared.txt","w") as s:
#     for line in f.readlines():
#         int_num= int(line)
#         s.writelines(f'{str(int_num**2)}\n')
#     print("done")


# message=input("Enter a message: ")
# f= open("numbers.txt","a")
# f.writelines(f"{message}\n")


with open("sample.txt","r") as i , open("dest.txt","w") as d:
    for lines in i:
        new_line=lines.upper()
        d.writelines(f"{new_line}\n")


