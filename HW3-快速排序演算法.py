#!/usr/bin/env python
# coding: utf-8

# In[1]:


#先定義函式，該函式接受列表arr的輸入
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


# Demo
arr = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
sorted_arr = quick_sort(arr)
print(sorted_arr)


# In[ ]:




