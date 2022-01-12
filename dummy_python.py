"""Dummy python: just a way to demonstrate how a module is written conventionally"""
from time import sleep

def hello_world(name):
  """Prints hello world with a name immediately"""
  print(f'hello world from {name}!')

class DelayedGreeter:
  """Greets with hello world after a specifc delay"""
  delay = 0.2 # a class attribute
  mult = 1
  
  def __init__(self, name): # this is nescessary to initiate the instance of a class.
    self.name = name
    self.greets = 0
  
  def greet(self):  # a class method
    """Run the greeting procedure"""
    for i in range(mult):
      sleep(delay)
      hello_world(self.name)
      self.greets += 1 
      
  def set_greeting_multiple(self, mult=1): # a setter method, with conventional classes, this can be done directly
    self.mult = mult
          
  def __str__(self):
     return f'DelayedGreeter(delay={self.delay}, mult={self.mult}, greetings={self.greets})'
   
class DoubleDelayedGreeter(DelayedGreeter): # inherit attributes from the other class
    """Greeter which delays for twice the specified time, and allows caps to be set"""
    
  def __init__(self, name, caps=True):
    super().__init__(self, name)  # super() calls the parent class' init method
    self.caps = caps

  def greet(self):  # a modified greeter method which behaves with new attributes
    """Run the greeting procedure"""
    for i in range(mult):
      sleep(delay*2)
      output_name = self.name
      if self.caps:
        output_name = self.name.upper()
      hello_world(self.name)
    

        
def main(): ## the below will only be run if the module is run as a script. Otherwise, the classes and functions are imported. 
  print('dummy python')
  n = input('name: ')
  print(f'>>> hello_world({n})')
  hello_world(n)
  print(f'>>> dg = DelayedGreeter(n)')
  dg = DelayedGreeter(n)
  print(f'>>> dg.greet()')
  dg.greet()
  print(f'>>> dg.set_greeting_multiple(2)')
  dg.set_greeting_multiple(2)
  print(f'>>> dg.greet()')
  dg.greet()
  print(f'>>> print(dg)')
  print(dg)
  print(f'>>> dg.delay = 0.1')
  dg.delay = 0.1
  print(f'>>> print(dg)')
  print(dg)
  print(f'>>> dg.greet()')
  dg.greet()
  print(f'>>> ddg = DoubleDelayedGreeter(n, caps=True)')
  ddg = DoubleDelayedGreeter(n, caps=True)
  print(f'>>> ddg.greet()')
  ddg.greet()
  print(f'>>> # if this was a prompt, enter: >>> quit()')
  print('...end')
  
        
# the boilerplate below checks the code is being run as a script, not as a module import. 
if __name__ == '__main__': 
  main()
