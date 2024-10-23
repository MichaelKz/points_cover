# Covering Points (hitting objects problem)


<b>Description:</b> Imagine having a set of points on a Cartesion coordinate system. You want to cover them with a set of straight lines. The goal is to find the minimum number of lines that pass through the points and cover them all. 
This problem is called a "hitting objects problem" because it can be understood as trying to "hit" a set of objects (represented by points) with as few shots as possible.

<b>Method of Solution:</b> To solve this, we would normally need to find a set of all possible lnes passing through the given points. This process is an example of a more general set covering problem, which is computationally hard to solve in polynomial time. Specifically, we would need to
1) Generate all subsets of lines that cover the points
2) Check each subset to see if it covers all of the points
3) Pick the smallest subset

With given "m" lines and "n" points, the number of possible subsetts of lines is 2<sup>m</sup> (since each line can either be included or excluded from a subset). Then, for each subsett, you would need tto check if it covers all points, which can take O(n) time.
So, the time complexity is: O(2<sup>m</sup> ⋅ n)

This is <b>exponential time complexity</b>, making it impractical for large values of m (numbers of lines). 
Besides using a "brute force" algorithm, like the one above, we can also make a more approximative algorithm "greedy" to find a locally-optimal choice that isn't far apart from the most optimal one. 

To do this
