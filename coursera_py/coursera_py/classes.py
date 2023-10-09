class Point:
    def __init__(self):
        self.x = initX
        self.y = initY

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx,my)

    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)
    
    # Override method for adding two point objects
    def __add__(self, otherPoint):
        return Point(self.x + otherPoint.x,
                     self.y + otherPoint.y)
    
    #method to override subtraction
    def __sub__(self, otherPoint):
        pass

    
    
p1 = Point(-5, 10)
p2 = Point(15, 20)

print(p1) # will use __str__ method
print(p2)

print(p1+p2) # will use __add__ then __str__ method 

mid = p.halfway(q) # should return point halfway between self and target

#SORTING LISTS OF INSTANCES
class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

# returns the price to be used for sorting criteria
    def sort_priority(self):
        return self.price()

L = [
    Fruit('Cherry',10),
    Fruit('Apple',5),
    Fruit('Blueberry' 20)
    ]
#print(sorted(L,key)) would return ValueError because "dont know how to compare Fruit and Fruit object"
# Instead use:

#for f in sorted(L,key=Fruit.sort_priority):
    # print(f.name)
# will print fruits in order of lowest to highest price
# notice that we do not write Fruit.sort_priority()  - must write w/out parentheses because we want to 
#return the fcn object itself and not the return value of the function

# OR

# can pass in a lambda function
# for f in sorted(L,key= lambda x: x.sort_priority):
    # print(f.name)
# x is every instance

# sort_priority fcn must be one that returns a number

# CLASS VARIABLES VS INSTANCE VARIABLES
# Python first searches through instance variables THEN class variables
# runtime error if not in either
# Class variables are accessed in the same way as instance variables i.e. self.Var

# When the interpreter sees an expression of the form <obj>.<varname>, it:
# Checks if the object has an instance variable set. If so, it uses that value.
# If it doesn’t find an instance variable, it checks whether the class has a class variable. If so it uses that value.
# If it doesn’t find an instance or a class variable, it creates a runtime error (actually, it does one other check first, which you will learn about in the next chapter).

# When the interpreter sees an assignment statement of the form <obj>.<varname> = <expr>, it:
# Evaluates the expression on the right-hand side to yield some python object;

# Sets the instance variable <varname> of <obj> to be bound to that python object. Note that an assignment statement of this form never sets the class variable; it only sets the instance variable.

# In order to set the class variable, you use an assignment statement of the form <varname> = <expr> at the top-level in a class definition, like on line 4 in the code above to set the class variable printed_rep.

# In case you are curious, method definitions also create class variables. Thus, in the code above, graph becomes a class variable that is bound to a function/method object. p1.graph() is evaluated by:
# looking up p1 and finding that it’s an instance of Point
# looking for an instance variable called graph in p1, but not finding one
# looking for a class variable called graph in p1’s class, the Point class; it finds a function/method object
# Because of the () after the word graph, it invokes the function/method object, with the parameter self bound to the object p1 points to.

#   INHERITANCE
# Take all of instance variables and methods that other class has and add more variables/methods
# Use inheritance when you want all of the methods and variables of the parent class AND MORE
# Do not use inheritance if all methods and variables of child class are subsets of parents methods
# and variables
# Instead use composition i.e. initialize a list of objects in the sub glass where each object
# in the list is an instance of the parent class.
# Composition is for when one class is a collection of instances from another class
# Important to make the distinction - subclass --> when one class's properties are a subset of
#another
#Composition - when the items/instances of of one class are all of a particular class type i.e.
# instances of another class


#INVOKING the PARENT CLASS METHODS
# If parent and sub class have methods of the same name & you want to call parent methods from the 
# subclass do: ParentClass.Method(self) instead of the usual : self.Method() (this would call the
# subclass's method)
# Can be done for the constructor as well e.g. ParentClass.__init__(self, required_params_in_parent c
# onstructor)
#
