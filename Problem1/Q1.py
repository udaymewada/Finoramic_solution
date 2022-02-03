
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def threeSumClosest(self, A, B):
        A.sort()
        cSum=sys.maxsize

        for i in range(len(A)-2):
            p1=i+1
            p2=len(A)-1
            while(p1<p2):
                summ=A[i]+A[p1]+A[p2]
                if abs(B-summ) < abs(B-cSum):
                    cSum=summ
                if summ>B:
                    p2-=1
                else:
                    p1+=1
        return cSum

