#Given a string s, reverse only all the vowels in the string and return it.
#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 
def reverseVowels(s):
    vovels = {'a', 'e', 'i' ,'o','u', 'A', 'E', 'I' , 'O', 'U'}
    s = list(s)
    # print(s)
    vpos=[]
    vword=[]

 for index, char in enumerate(s):
        if char in vovels:
            vpos.append(index)
            vword.append(char)
    print(vword, vpos)
    for i in vpos:
        print(i)
        s[i]=vword.pop()
        
    return "".join(s)

reverseVowels("hello")


#Example 1:
#Input: s = "hello"
#Output: "holle" 
