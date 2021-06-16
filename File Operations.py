#!/usr/bin/env python
# coding: utf-8

# In[ ]:


myFile = open("myFirstTextFile.txt","r") #This is opening my file in the RAM, r - reading, w - writing, r+ - both and a - append
myFile.close()#This is closing my file


# In[2]:


#Writing in a file
myFile = open("myFirstTextFile.txt","w")
myFile.write("Hi! My name is Vivaan!")
myFile.close()


# In[8]:


#Adding square numbers in a file
squareNumbers = [1,4,9,16,25,36,49,64,81,100]
myFile = open("squareNumbers.txt","w")
def square(squareNumbers):
    for num in squareNumbers:
        num2 = str(num)
        num2 = num2+"\n"
        myFile.write(num2)       
square(squareNumbers)
myFile.close()


# In[11]:


#Reading a file
myFile = open("myFirstTextFile.txt","r")
Output = myFile.read()#This method returns what is inside the file
print(Output)
myFile.close()


# In[16]:


#Reading a file line by line
myFile = open("myFirstTextFile.txt","r")
print(myFile.readline())#This reads the first line, and then moves to the next
print(myFile.readline())#This reads the second line
myFile.close()


# In[18]:


#Appending in a file
myFile = open("myFirstTextFile.txt","a")
myFile.write("\nHi! My name is Kanishk!")
myFile.close()


# In[3]:


#Reading and Writing in a file
myFile = open("myFirstTextFile.txt","r+")
print(myFile.readline())
myFile.write("\nHi! My name is Daksh!")
myFile.close()

