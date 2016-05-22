# _*_ coding: utf-8 _*_

name = 'Zed A. Shaw'
age = 35 #totally a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are unually %s depending on the coffee." %teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)

