#!/usr/bin/python3
# This Python file uses the following encoding: utf-8

"""
This module contains the functions that relate to the first three
lectures of the course (basic training and lists). 
"""
import math

def distance(t, accel):
    """Print the distance travelled.

    Calculates the distance travelling in a given time (t) at a given
    acceleration (accel).

    You should round the result to ONE decimal places (use the round
    method, for example round(10.01,1) creates the output 10.0). Why
    do this? To hide any problems related to floating point precision.

    Args:
       t is an integer
       accel is a float

    """
    
    print(round (0.5*accel*t**2 , 1))  #calculating the distance, with a given time and accel
    

def pythagoras(a, b):
    """Find the length of a third side of a triangle.

    Uses pythagoras' theorem to calculate the length, that is the sum
    of the squares of two legs (a and b) is equal to the sum of the
    squares of the other leg.

    If a and b are both equal or greater than zero, print
    the length of the leg.

    If a is zero or negative print "First leg is invalid"

    If b is zero or negative print "Second leg is invalid"

    Again you should round the output to one decimal place (hide
    precision problems).

    Args:
       a is an integer or float
       b is an integer or float

    """
    if a == 0 or a < 0:  			# a is equal to 0 or less than 0 prints an invalid statement
        print ("First leg is invalid") 
    elif b == 0 or b < 0:		    # b is equal to 0 or less than 0 prints an invalid statement
        print ("Second leg is invalid")
    else: 							# otherwise calculate the length of a triangle with the given a and b 	
        l = math.sqrt((a**2) + (b**2))
        l = round(l,1)
        print (l)
    
    #print(a,b)

def grade(mark,mcr):
    """Assign a letter grade based on a mark

    Implement this grading scheme.

    A between 80 and 100
    B between 65 and 79
    C between 50 and 65
    D between 40 and 49
    E between 0 and 39

    K Fail due to not satisfying mandatory course requirements, even
      though the student’s numerical course mark reached the level
      specified for a pass, usually 50%. A student whose course mark
      is below 50 should be given a D (40–49) or E (0 –39), regardless
      of whether they met the mandatory course requirements.

    You should sanity check the types of the inputs.

    Args: 
       mark is an integer mark, if not integer print "Invalid mark"

       mcr is a boolean (True if met mandatory requirements, False
        if have not met them), if not boolean print "Invalid mcr"

    """
    if not isinstance(mark,int):		#print invalid if mark is not an instance of int
    	print ("Invalid mark")
    elif not isinstance(mcr, bool):		#print invalid if mcr is not an instance of boolean
    	print ("Invalid mcr")
    elif not mcr:						#print K if not met the mandatory requirements
    	print ("K")
    elif mark >= 80 and mark <= 100:	#print A if mark is between 80 and 100
    	print ("A")
    elif mark >=65 and mark <= 79:		#print B if mark is between 65 and 79
    	print ("B")
    elif mark >= 50 and mark <= 65:		#print C if mark is between 50 and 65
    	print ("C")
    elif mark >= 40 and mark <= 49:		#print D if mark is between 40 and 49
    	print ("D")
    else:								#Otherwise print E 
    	print("E")
    	
    #print(mark, mcr)

def print_before(text, marker):
    """Count how many words occur in a given piece of text up to a marker 

    Given a piece of text and a given marker word, display all the
    words from the beginning of the text through to (and including the
    marker word).

    Print the entire list of words in the text should the marker not
    be found (use list operators to implement this functionality).
     
    You should check the arguments and print an error message if the
    types of the argument are different from expected.

    For example, if the text is not a list display "Expected a list of
    words" and if the marker is not string display "Expected a string".

    Args:
      text is a list of words
      marker is a string

    """
    if not isinstance(text, list): 			#checks if the text is an instance of list
    	print ("Expected a list of words")
    elif not isinstance(marker, str):		#checks if the marker is an instance of String
    	print ("Expected a string")
    else:									#otherwise display all the words before the given marker words
    	text_Before = []					#temporary array
    	for val in text:					#for loop in the text list
    		if val == marker:				#check if val is equal to marker if it is then break
    			break
    		else:							#otherwise add the val inside the temp array and print it
    			text_Before.append(val)
    	print(text_Before)
    #print(text, marker)

