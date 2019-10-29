# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:18:40 2019

@author: huyn
"""
"""
1186. Maximum Subarray Sum with One Deletion
Given an array of integers, return the maximum sum for a non-empty subarray 
(contiguous elements) with at most one element deletion. In other words, you want 
to choose a subarray and optionally delete one element from it so that there is still 
at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.
"""
class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans  = arr[0]
        suf_no_del = arr[0]
        suf_del = 0
        for num in arr[1:]:
            # for sub_del, we add num to the one already deleted, and check with the suffice thata did not delete
            suf_del = max(suf_del + num,suf_no_del)
            # for suf_no_del, either we keep lengthening what we have before, or starting with this num as our new
            suf_no_del = max(suf_no_del+num,num)
            ans = max(ans,suf_del,suf_no_del)
        return ans