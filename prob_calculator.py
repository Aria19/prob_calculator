from random import randrange, sample
import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **args):
    self.contents = []
    for k, v in args.items():
      for i in range(v):
        self.contents.append(k)
    
  def draw(self, n):
    list2 = []
    if n > len(self.contents):
      list2.append(self.contents)
    else:
      for i in range(n):
        randomel = self.contents.pop(randrange(len(self.contents)))
        list2.append(randomel)
    return list2


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  N = num_experiments
  c = []
  for k, v in expected_balls.items():
    for i in range(v):
      c.append(k)
  for i in range(N):
    hatc = copy.deepcopy(hat)
    listt = hatc.draw(num_balls_drawn)
    for l in c:
      if l in listt:
        listt.remove(l)
    if len(listt) == 1:
      M = M + 1  
  prob = M / N
  print(c)
  print(listt)
  return prob
  
