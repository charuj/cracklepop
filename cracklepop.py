import unittest 

class Cracklepop:
  def __init__(self, start, end):
    self.start= start
    self.end= end

  def division(self,i):
      if (i%3==0) & (i%5==0):
        return "CracklePop"
      if (i%3==0) & (i%5!=0):
        return "Crackle"
      elif (i%5==0) & (i%3!=0):
        return "Pop"
      else: 
        return i 

  def function(self):
    num_list=[]
    for k in range(self.start, self.end+1):
      num_list.append(self.division(k))
    print (num_list)
    

class TestCracklepop(unittest.TestCase):
  def test_division(self):
    self.assertEqual(Cracklepop.division(self, 5), "Pop")
    self.assertEqual(Cracklepop.division(self, 6), "Crackle")
    self.assertEqual(Cracklepop.division(self, 90), "CracklePop")
    self.assertEqual(Cracklepop.division(self, 22), 22)




if __name__ == '__main__':
    c=Cracklepop(1,100)
    c.function()  
    unittest.main(argv=['first-arg-is-ignored'], exit=False)