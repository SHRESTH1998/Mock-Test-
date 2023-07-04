#!/usr/bin/env python
# coding: utf-8

# # Q17. Ans

# In[2]:


def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output_list = get_even_numbers(input_list)
print(output_list)


# # Q18. Ans

# In[5]:


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.5f} seconds")
        return result
    return wrapper

@timer
def my_function():
    # Function code goes here
    time.sleep(2)

my_function()


# # Q19. Ans

# In[4]:


def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

data = [10, 15, 20, 25, 30]
mean_value = calculate_mean(data)
print("Mean:", mean_value)


# # Q20. Ans

# In[8]:


from scipy import stats

def perform_hypothesis_test(sample1, sample2):
    t_statistic, p_value = stats.ttest_ind(sample1, sample2)
    return p_value

sample1 = [5, 10, 15, 20, 25]
sample2 = [10, 20, 30, 40, 50]
p_value = perform_hypothesis_test(sample1, sample2)
print("P-value:", p_value)


# In[ ]:





# In[ ]:




