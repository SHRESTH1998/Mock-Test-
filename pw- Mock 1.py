#!/usr/bin/env python
# coding: utf-8

# In[3]:


s = "abdce"
print ( s[ 2 : -1 ])


# In[6]:


def func(n):
          if n == 1 :
              return 2

          return n*func(n-1) // 2
print(func(5))   


# In[12]:


def func(s):

        if len(s) <= 1:
            return s

        return func(s[ 2 : ]) + s[0]
print( func( "AeI123" ) ) 


# In[13]:


def moveZeroes(nums):
    """
    Moves all zeroes to the end of the array while maintaining the order of non-zero elements.
    """
    # Initialize two pointers
    left = 0  # Points to the current non-zero element
    right = 0  # Traverses the array
    
    # Traverse the array
    while right < len(nums):
        # If the current element is non-zero
        if nums[right] != 0:
            # Swap the current element with the left pointer
            nums[left], nums[right] = nums[right], nums[left]
            # Move the left pointer forward
            left += 1
        # Move the right pointer forward
        right += 1

# Test the function
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

nums = [0]
moveZeroes(nums)
print(nums)  # Output: [0]


# In[14]:


def firstUniqChar(s):
    """
    Finds the index of the first non-repeating character in the string.
    Returns -1 if no such character exists.
    """
    # Create a dictionary to store the frequency of each character
    freq = {}
    
    # Count the frequency of each character
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Find the first non-repeating character
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i
    
    # No non-repeating character found
    return -1

# Test the function
s = "leetcode"
print(firstUniqChar(s))  # Output: 0

s = "loveleetcode"
print(firstUniqChar(s))  # Output: 2

s = "aabb"
print(firstUniqChar(s))  # Output: -1


# In[ ]:




