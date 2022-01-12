"""Dummy python: just a way to demonstrate how a module is written conventionally"""
from time import sleep

def hello_world(name):
  """Prints hello world with a name immediately"""
  print(f'hello world from {name}!')

class DelayedGreeter:
  """Greets with hello world after a specifc delay"""
  delay = 0.2 # a class attribute
  mult = 1
  
  def __init__(self, name):
    self.name = name
  
  def greet(self):
    """Run the greeting procedure"""
    for i in range(mult):
      sleep(delay)
      hello_world(self.name)
      
  def set_greeting_multiple(self, mult=1):
    self.mult = mult
          
  def __str__(self):
     return f'DelayedGreeter(delay={delay}, mult={mult})
   
class DoubleDelayedGreeter(DelayedGreeter): # inherit attributes from the other class
    """Greeter which delays for twice the specified time, and allows caps to be set"""
    
  def __init__(self, name, caps=True):
    super().__init__(self, name)
    self.caps = caps

  def greet(self):
    """Run the greeting procedure"""
    for i in range(mult):
      sleep(delay)
      output_name = self.name
      if self.caps:
        output_name = self.name.upper()
      hello_world(self.name)
    

        
def main():
  print('delayed greeter')
        
  
if __name__ == '__main__':
  main()
