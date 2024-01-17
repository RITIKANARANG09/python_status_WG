class Parent:

    def say_hello(self):
        print( f"Parent class" )

class Child(Parent):
    def say_hello(self):
       # super().say_hello()
        print( f"Child class" )

a=Child()
b=Parent()
super(Child,a).say_hello()

