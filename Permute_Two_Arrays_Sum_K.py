def permute_arrays(A,B,C):
    A.sort()
    B.sort(reverse = True)
    for i in range (len(A)):
        if A[i] + B[i] < K:
            return "No"
    return "Yes"    
A = [2,1,3]
B = [7,8,9]
K = 10
print(permute_arrays(A,B,K))