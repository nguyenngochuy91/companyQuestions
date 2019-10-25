# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 23:45:02 2019

@author: Huy Nguyen
"""

#merge sorted array in place
def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        while p1>=0 and p2>=0:
            n1 = nums1[p1]
            n2 = nums2[p2]
            if n2>=n1:
                nums1[p1+p2+1]= n2
                p2-=1
            elif n2<n1:
                nums1[p1+p2+1]= n1
                p1-=1
        while p2>=0:
            nums1[p2]=nums2[p2]
            p2-=1