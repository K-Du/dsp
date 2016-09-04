# Matrix Algebra
import numpy as np

A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])
u = np.array([[6,2,-3,5]])
v = np.array([[3,5,-1,4]])
w = np.array([[1,8,0,5]]).T
alpha = 6

print "Problem #1"
print A.shape
print B.shape
print C.shape
print D.shape
print u.shape
print w.shape

print "\nProblem #2"
print u + v
print u - v
print alpha*u
print np.inner(u,v)
print np.linalg.norm(u)

print "\nProblem #3"
print "undefined" # print A + C 
print A - C.T
print C.T + 3*D
print np.dot(B, A)
print "undefined" # print np.dot(B, A.T)

print "\nOptional"
print "undefined" # print np.dot(B, C)
print np.dot(C, B)
print np.dot(np.dot(np.dot(B,B),B),B)
print np.dot(A, A.T)
print np.dot(D.T, D)





'''
Solutions:
Problem #1
(2L, 3L)
(2L, 2L)
(3L, 2L)
(2L, 3L)
(1L, 4L)
(4L, 1L)

Problem #2
[[ 9  7 -4  9]]
[[ 3 -3 -2  1]]
[[ 36  12 -18  30]]
[[51]]
8.60232526704

Problem #3
undefined
[[-4 -7 -3]
 [ 3  6  4]]
[[14  3  3]
 [ 2  7  9]]
[[-1 -5 -1]
 [ 2  7  4]]
undefined

Optional
undefined
[[ 5 -6]
 [ 9 -8]
 [ 6 -6]]
[[ 1 -4]
 [ 0  1]]
[[14 28]
 [28 69]]
[[10 -4  0]
 [-4  8  8]
 [ 0  8 10]]
 '''
