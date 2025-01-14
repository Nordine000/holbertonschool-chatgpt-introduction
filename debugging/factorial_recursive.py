#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
        if len(sys.argv) > 1: 
          try: 
           f = factorial(int(sys.argv[1]))
           print(f)
          except ValueError: 
            print("Invalid input. Please enter a valid integer.") 
        else: 
          print()
