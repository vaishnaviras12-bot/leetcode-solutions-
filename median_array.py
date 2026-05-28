#question -- Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n))

class Solution:
    def findMedianSortedArrays(self, nums1 ,nums2):
        i=0
        j=0
        l=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                l.append(nums1[i])
                i+=1
            else:
                l.append(nums2[j])
                j+=1
        l.extend(nums1[i:])
        l.extend(nums2[j:])

        mid=len(l)//2
        if len(l)%2==0:
            median=(l[mid]+l[mid-1])/2
        else:
            median=l[mid]
        return median