#!/usr/bin/python3

#Exercise1. Modifiy print_matrix1 function to generate the same matrix found in:
#https://upload.wikimedia.org/wikipedia/commons/2/28/Smith-Waterman-Algorithm-Example-Step2.png
#or like sw.PNG

from time import sleep
import numpy as np

def print_matrix1(a,x,y):
	mrows = len(x) + abs((len(x) - len(y)))
	ncols = len(y) + abs((len(x) - len(y)))

	
	print('     ', end='')
	for i in range(len(y)): #print y 
		print(y[i], end='  ')
	print()
		
	b = 0
	
	for i in range(mrows):
		for j in range(ncols):

			if(j==0 and i == 0):
				print(end=' ') # fix spacing on first line
			if(j == 0 and i > 0 ): # loop for printing 
				print(x[b], end='')	# print x
				b = b+1 			# increment iterator for x
			print("%2d" % a[i][j], end=' ')
		print()

def gen_matrix(x, y, match_score=3, gap_cost=2):
	mrows = len(x)
	ncols = len(y)

	#initialize matrix to zeroes
	a = [0] * (mrows + 1)
	for i in range(mrows + 1):
		a[i] = [0] * (ncols + 1)
	
	# print_matrix(a,x,y)
	
	for i in range(1,mrows+1):
		for j in range(1,ncols+1):
			match = a[i-1][j-1] - match_score
			if(x[i-1] == y[j-1]):
				match = a[i-1][j-1] + match_score
			delete = a[i - 1][j] - gap_cost
			insert = a[i][j - 1] - gap_cost
			a[i][j]=max(match,delete,insert,0)

	return(a)
	
x = "GATTACA"	
y = "TGTTACGG"

a=gen_matrix(x,y)

matr = print_matrix1(a,x,y)

# pseudocode for smith waterman's algorithm

# # while i = max and j = max:
# check max neighbors: x[i-1]y[j] x[i]y[j-1] x[i-1][j-1] 
# if x == y: align
first = []
second = []

def insert_to_list(i,j,x,y): #


	if(x[i-1] == y[j-1]): 
			# print('link')
		first.insert(0,y[j-1])
		second.insert(0,x[i-1])
		
	else:
		# print('no link')
		first.insert(0,'-')
		second.insert(0,x[i-1])

def print_alignment(list1,list2): 
	connection = []
	for i in range(len(list1)):
		if(list1[i] == list2[i]):
			connection.append('|')
		else: 
			connection.append(' ')
	
	
	for i in range(len(list1)):
		print(list1[i], end=' ')
	print()
	for i in range(len(connection)):
		print(connection[i], end=' ')
	print()
	for i in range(len(list2)):
		print(list2[i], end=' ')
	print()

	# print(list1)
	# print(connection)
	# print(list2)

def generate_alignment(matr,x,y):
	mrows = len(x) + abs((len(x) - len(y)))
	ncols = len(y) + abs((len(x) - len(y)))
	
	biggest = (max(map(max,matr)))
	bigger = 0 #variable for comparing neighbor values

	c = 0 #index for x in reverse
	d = 0 #index for y in reverse


	for i in range(mrows):
		for j in range(ncols):
			if matr[i][j] == biggest:
				c = i
				d = j
	
				insert_to_list(c,d,x,y)

	for i in range(c,0,-1):
		for j in range (d,0,-1):
			
			# indexing prompts
			# print()
			# print(c,d,i,j)
			# print('current value', matr[i][j], 'left: ',matr[i][j-1], 'top: ',matr[i-1][j], 'diagonal: ',matr[i-1][j-1])
			
			if matr[i-1][j-1] >= matr[i][j-1]: #diagonal > left
				if matr[i-1][j-1] > matr[i-1][j]: #diagonal > top

					# print('diagonal index: (',i-1,j-1,') value: ',matr[i-1][j-1])
					# print('diagonal next value: ', matr[i-1][j-1], 'index: ', (i-1),(j-1))
					i = i-1
					j = j-1
					c = i
					d = j
					insert_to_list(i,j,x,y)

				else: # top > diagonal

					if(matr[i-1][j] > matr[i][j-1]): #if top > left
						# print('top next value: ', matr[i-1][j], 'index: ',(i-1),j)
			
						i = i-1
						j = j
						c = i
						d = j
						insert_to_list(i,j,x,y)

						# print(i,j, matr[i][j])

					else:
					
						i = i
						j = j-1
						c = i
						d = j
						# print('check 1')
											
			else: 	#left > diagonal
				if matr[i][j-1] > matr[i-1][j]:  #left > top
				
					i = i
					j = j-1
					c = i
					d = j
					insert_to_list(i,j,x,y)
		
				else:

					i = i-1
					j = j
					c = i
					d = j
					insert_to_list(i,j,x,y)

			#prompts
			# print('current index',x[i-1], y[j-1],matr[i][j])
			# print(c,d,i,j)
			# print()
	print_alignment(first,second)





generate_alignment(a,x,y)