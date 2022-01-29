class Solution:
	# @param A : string
	# @return an integer
	def braces(self, A):
        # list of all operator 
		operators=['+','-','/','*'] 

        # list for storing brackets
		st=[]
		for i in A:

            # if open bracket then push into the list
			if i=='(':
				st.append(i)
			if len(st)>0 and i in operators  :
				st.pop()			
		if st:
			return 1
		else:
			return 0

