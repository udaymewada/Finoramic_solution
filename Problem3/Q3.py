class Solution:
	# @param A : tuple of strings
	# @return a list of list of integers
	def anagrams(self, A):
        arr = list(A)
        for i in range(len(arr)):
            arr[i] = "".join(list(sorted(list(arr[i]))))
        ans=[]
        for i in range(0,len(arr)):
            if arr[i]==" ":
                continue
            else:
                res=[i+1]
                for j in range(i+1,len(arr)):
                    if arr[i]==arr[j]:
                        res.append(j+1)
                        arr[j]=" "
                ans.append(res)
        return ans