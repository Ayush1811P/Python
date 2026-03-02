        #🔎 Level 1 – Python Core Check
        #✅ Question 1: Basic Logic + Loop + Condition
        
# def analyze_numbers(numbers):
#     total=0
#     average=0.00
#     maximum=numbers[0]
#     count_even=0
#     for x in numbers:
#         if maximum < x:
#             maximum=x
#         if x %2==0:
#             count_even+=1
#         total=total+x
#     average=total/len(numbers)

#     return{
#         "sum": total,
#         "average": average,
#         "max": maximum,
#         "even_count": count_even
#     }
    

# print(analyze_numbers([10, 5, 8, 3])    )




    #Level 2 – Now Let’s Increase Difficulty
    #Question 2: String + Logic + Dictionary

# def words_count(sentence):
#     sentence=sentence.lower()
#     sentence=sentence.replace(",","")      
#     sentence=sentence.replace("!","")      
#     sentence=sentence.replace(".","")      
#     sentence=sentence.replace("?","")   

#     words = sentence.split()   
    
#     freq={}
#     for word in words:
#         if word in freq:
#             freq[word]+=1
#         else:
#             freq[word]=1
#     return freq

# print(words_count("Hello hello world, world!"))        

        #🚀 Question 3 – Intermediate Logic
        #Return the second largest unique number
        #If not possible, return None

# def smax(numbers):
#     maximum=numbers[0]
#     smaximum=0
#     for x in numbers:
#         if maximum<x:
#             smaximum = maximum
#             maximum = x
#         if x < maximum and x > smaximum:
#             smaximum=x
#         elif smaximum==maximum:
#             smaximum=None
#     return smaximum
# print(smax([5, 5, 5]))      



        #🔥Now I want you to attempt it. 😄
        #Convert to lowercase
        #Remove spaces
        #Count characters in dictionary
        #Compare counts



# def is_angram(str1,str2):
#     str1=str1.lower()
#     str2=str2.lower()
#     str1=str1.replace(" ","")
#     str2=str2.replace(" ","")
#     for_str1={}
#     for_str2={}
#     if len(str1)!=len(str2):
#         return False
#     for word1 in str1:
#         if word1 in for_str1:
#             for_str1[word1]+=1
#         else:
#             for_str1[word1]=1

#     for word2 in str2:
#         if word2 in for_str2:
#             for_str2[word2]+=1
#         else:
#             for_str2[word2]=1
#     # print(for_str2)
#     # if for_str1 == for_str2:
#     #     print("Strings  are same")
#     # else:
#     #     print("strings are different")                
#     if for_str2==for_str1:
#         return True
#     else:
#         return False
# print(is_angram("pyhton is easy","pyhton is easy"))


        #🚀 Question 5 – Medium Difficulty
        #The first character that appears only once
        #If none → return None



# def non_repeating_word(sentence):
#     words=sentence.lower()
#     # words=words.split()
#     characters={}

#     for x in words:
#         if x  in characters:
#             characters[x]+=1
#         else:
#             characters[x]=1


#     for key,value in characters.items():
#         if value ==1:
#             # print(f"First non-repeating item is: {key}")
#             return key
#     return None        
                    


# print(non_repeating_word("aabbccddeegghh"))


# s = "loveleetcode"
# if s=="":
#     print(-1)
# else:
#     freq={}
#     for ch in s:
#         if ch in freq:
#             freq[ch]+=1
#         else:
#             freq[ch]=1
#     for i in range(len(s)):
#         if freq[s[i]]==1:
#             print(i)
#             break
#         else:
#             print(None)



# def second_largest(nums):
#     maximum = None
#     smaximum=None
#     if not isinstance(nums,list):
#         raise TypeError("enter only list")
    
#     if len(nums) <=1:
#         return -1
    

#     for n in nums:
#         if not isinstance(n,int):
#             raise TypeError("enter integers only!")
    
    
#     for n in nums:
#         if maximum==None:
#             maximum=n
#         elif n>maximum:  
#             smaximum=maximum
#             maximum=n
#         elif n<maximum:
#             if smaximum==None or n>=maximum:
#                 smaximum=n
#     if smaximum is None:
#         return -1    
#     return smaximum        
    
# print(second_largest([1,1,0])) 



# def second_largest(nums):
#     if not isinstance(nums, list):
#         raise TypeError("Input must be a list")

#     if len(nums) <= 1:
#         return -1

#     maximum = None
#     smaximum = None

#     for n in nums:
#         if not isinstance(n, int):
#             raise TypeError("All elements must be integers")

#         if maximum is None:
#             maximum = n

#         elif n > maximum:
#             smaximum = maximum
#             maximum = n

#         elif n < maximum:
#             if smaximum is None or n > smaximum:
#                 smaximum = n

#     if smaximum is None:
#         return -1

#     return smaximum

# print(second_largest([10,0,0,30]))






# def is_prime(num):
#     prime=True
#     if num % 2==0:
#         return False
    
#     if not isinstance(num,int):
#         raise TypeError("enter integer only!")
#     if num<=0 or num==1:
#         return False
#     else:
        
#         for x in range(2,num):
#             if x%num==0:
#                 prime=False
#                 return prime
#     return prime        
           
# print(is_prime(14))





# def remove_duplicates(nums):
#     #check if user input is None or valid
#     if nums is None:
#         return -1
    
#     #if it has only one value or empty list
#     if len(nums)<=1:
#         return nums
    
#     #check if nums is a list?   
#     if not isinstance(nums,list):
#         raise TypeError("enter list type")
#     #check if nums[values are integer?]
#     for x in nums:
#         if not isinstance(x,int):
#             raise TypeError("Enter only integers!")
        
#     #if user input valid initialize 2 variables
#     last_element=nums[-1]
#     i=nums[0]
#     #using while iterate on elements of nums until we break loop
#     while True:
#         #checking in the first loop if true break
#         if last_element!= i:
#             break
#         else:
#             #check only untill i  < nums last element
#             while i<last_element:
#                 i+=1
#             print("all elements are same!") 
#             return
#     i=0
#     while i < len(nums):
#         j=i+1
#         #using nested while iterate on variables 
#         while j< len(nums):
#             #check if j==i?remove element:j+=1
#             if nums[i]==nums[j]:
#                 nums.pop(j)
#             else:
#                 j+=1
#         i+=1      
#     #return the updated list 
#     return nums      
# print(remove_duplicates([10,10,10,10,10]) )        


                

