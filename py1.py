#Initialization
class xd:
  def __init__(self, name):
    self.name = name
    
  def hello(self):
    print('Nice to meet you again',self.name,'. This cringy kingdom is for you! Glhf')

print('Welcome, the chosen one from the bottom of society!')
n = input('Let me know your sacred name: ')
v = xd(n)
v.hello()
