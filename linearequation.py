import sys
 
print "area of the cubiod "
x = input( 'enter x cooridnate: ')
y =  input( 'enter y cooridnate: ')

 
l=x+y+4

if l==0 :
	print " point x and y lie on the  line "

if l>0 :
	print " point x and y lie on the  left hand side of the line "
if l<0 :
	print " point x and y lie on the the right hand side of the line "
print " l==", l
  
	
