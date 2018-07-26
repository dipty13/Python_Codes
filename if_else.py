#!/bin/python3

n = int(input())
if(n%2==1):
	print("Weird")
elif(n>=2 and n<=5):
	print("Not weird")
elif(n>=6 and n<=20):
	print("Weird")
else:
	print("Not weird")