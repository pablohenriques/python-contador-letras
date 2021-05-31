
########################
def count_vowels(str):
  """
  Retorne o número de vogais dentro da string
  """
  """lista_vogais = ["a", "e", "i", "o", "u"]
  
  cont = 0
  for item in str.lower():
    if item in lista_vogais:
      cont += 1
  """

  return sum([i.count(j) for i in str.lower() for j in 'aeiou'])



#########################
import unittest

class TestCountVowels(unittest.TestCase):
  def test_lower(self):
    self.assertEqual(count_vowels('aaaaa'), 5)
  
  def test_many_lowers(self):
    self.assertEqual(count_vowels('aaaaaeeeei'), 10)

  def test_lowers_inside_others(self):
    self.assertEqual(count_vowels('You are the best!'), 6)

  def test_upper_and_lowers(self):
    self.assertEqual(count_vowels('A SIMPLE UPPER FOLLOWED BY A lower'), 11)

  def test_edge_cases(self):
    self.assertEqual(count_vowels('u'), 1)
    self.assertEqual(count_vowels('!!!!!'), 0)
    self.assertEqual(count_vowels(''), 0)
    self.assertEqual(count_vowels('aei' * 300000), 900000)

unittest.main(verbosity=1, exit=False)
#########################
