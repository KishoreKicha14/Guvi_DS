# Guvi_DS

## problem 1
Dora, the little adventure was busy helping her Mom Tanya at the kitchen. What's special that was getting ready? Tanya was preparing her special chicken noodle soup to give it to Diego, Dora's cousin. Once the soup was ready, Dora along with Boots set out to give the hot soup pot to Diego.

 
Dora asked help from the Map to show the directions to Diego's house. The Map directed Dora and Boots that they should reach the Bug House first and then solve a riddle asked by Bug King Typo following which they could proceed to Diego's house. Typo showed them a queue of N bugs of which only X bugs are to be selected. Each bug has some power associated with it. There are X iterations on the queue.
 

In each iteration, X bugs are dequeued (if queue has less than X entries, all of them will be dequeued) and the one with maximum power is selected and remaining bugs are enqueued back to the queue (in the order they were dequeued) but their power is decreased by one unit. If there are multiple bugs with maximum power in those dequeued bugs, the one which comes first in the queue is selected. If at any moment , power of any bug becomes 0, it can't be decremented any further, it remains the same.

 
Now, Typo's riddle to Dora and Boots is to tell him the positions of all the selected bugs (positions in the initial given queue) in the order they are selected. As Dora and Boots are too young to solve this riddle they call you for the rescue. Help them get the answer fast and reach Diego's house sooner.

 
### Input Format:
The first line consists of two space separated integers N and X, denoting the number of bugs in the queue and the number of bugs that have to be selected respectively.
The next line consists of an array A, A[i] denoting the power of bug at position i (1≤i≤N).

 
### Output Format:
For each of the X iterations, output the position of the selected bug in that iteration. Position refers to the index at which the bug was present in the initial given queue (1 based indexing).

Refer sample input and output for formatting specifications.

```
Sample Input:

6 5

1 2 2 3 4 5

```
```
Sample Output:

5 6 4 1 2
```
 
### Explanation:

The initial queue: 1,2,2,3,4,5
In first iteration, starting 5 entries are removed from the queue.
The removed entries are:[1,2,2,3,4].
The queue now becomes: [5] The maximum power bug is present at index 5 in the given initial queue. So, we print 5 and power of remaining bugs in the removed ones is decremented by 1 unit and enqueued back to the queue.
The queue now becomes: [5,0,1,1,2]

In the second iteration, we print index 6 as element 5 is present at index 6 in the initial queue.
After the second iteration, the queue becomes: [0,0,0,1]
Note that the power of bug with power 0 after the first iteration still remains 0.

## Problem 2

David loves Cakes and is much interested in baking. Hence he joined as a Manager at a famous bakery 'Cake Walk' which is called the cake lovers' paradise in the town. Because of the bakery's tantalising and delicious wide range of freshly baked cakes served in attractive cake boxes, people are seen always queuing up to have one of those boxes, which is why David's job is not so easy. Each cake box has a cost associated with it. The cake boxes are kept as a pile. He needs to handle two types of queries:

 

1) Customer Query:
When a customer demands a cake box, the box on the top of the pile is given and the customer is charged according to the cost of the box. This reduces the height of the pile by 1.
In case the pile is empty, the customer goes away empty-handed.

 

2) Baker Query:
The baker prepares a cake, wraps it in a box and adds it on top of the pile. And reports the cost of the box to David.
 

Help David manage the process.

 

Input Format:
First line contains an integer Q, the number of queries. Q lines follow.
A Type-1 (Customer) Query, is indicated by a single integer 1 in the line.
A Type-2 (Baker) Query, is indicated by two space separated integers 2 and Cwhere C is the cost of the box prepared.

 

Output Format:
For each Type-1 Query, output the price that customer has to pay i.e. cost of the box given to the customer in a new line. If the pile is empty, print "No Cake" (without the quotes).

 

#Sample Input and Output:
```
Sample Input:

 6
1
2 5
2 7
2 9
1
1
``` 
```
Sample Output:

 No Cake
9
7
 
```
### Explanation:

Initially, The pile is empty.
Baker adds a box with cost=5.
Baker adds a box with cost=7.
Baker adds a box with cost=9.
Customer takes the box on the top i.e. cost=9. Now box of cost=7 on top. Customer takes the box on the top i.e. cost=7.

## Problem 3

Corporate Fiesta
Corporate Fiesta is the first of its kind Carnival that has a unique blend of sports and arts, catering to varied interest of employees belonging to the Corporate companies of all sizes across the City. The Carnival had many events for different sections of employees.

One notable event is a simple ball passing game called FORWARD and REVERSE organised for the smart Coders in the Corporate. In this event, the coders were given N passes and players having ids between 1 and 1000000. Initially some player with a given id had the ball in his possession. The coders had to make a program to display the id of the player who possessed the ball after exactly N passes.

Description of the passes:
There were two kinds of passes:
1. F ID
2. R

Explanation :
For the first kind of pass, the player in possession of the ball passes the ball to player with id=ID, while for the second kind of a pass, the player in possession of the ball passes the ball back to the player who had passed the ball to him.

Note:
It is guaranteed that the given order of all the passes will be a valid order .

Input Format :
The first line of the input contains two space separated integers N, the number of passes and ID of the player possessing the ball in the very beginning. (1≤N≤100000 and 1≤ID≤1000000)
N lines follow describing the passes. ( for description of the passes, refer the statement above. )

Output Format :
Output to each test case should be a single line containing the "Player" ID (quotes for clarity) of the player who possesses the ball after N passes.
Refer sample input and output for formatting specifications.
```
Sample Input:
10 23
F 86
F 63
F 60
R
F 47
R
F 99
F 9
R
R
```
```
Sample Output:
Player 9
```
Explanation:
Initially, Player having id=23 possesses the ball. After pass 1, Player having id=86 possesses the ball. After pass 2, Player having id=63 possesses the ball. After pass 3, Player having id=60 possesses the ball. After pass 4, Player having id=63 possesses the ball. After pass 5, Player having id=47 possesses the ball. After pass 6, Player having id=63 possesses the ball. After pass 7, Player having id=99 possesses the ball. After pass 8, Player having id=9 possesses the ball. After pass 9, Player having id=99 possesses the ball. After pass 10, Player having id=9 possesses the ball. So the output is 9.
