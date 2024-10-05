import unittest
import sys

from boggle_solver import Boggle

class TestSuite_Alg_Scalability_Cases(unittest.TestCase):

  def test_Normal_case_3x3(self):
    grid = [["A", "B", "C"],["D", "E", "F"],["G", "H", "I"]]
    dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["abc", "abdhi", "cfi", "dea"];
    expected = [x.upper() for x in expected]
    solution = sorted(solution)   
    expected = sorted(expected)
    self.assertEqual(expected, solution)

  def test_4x4_grid(self):
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"], ["G", "Z", "Qu", "R"], ["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", 
                  "rat", "tar", "tarp", "ten", "went", "wet", "arty", "not", "quar"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["ART", "EGO", "GENT", "GET", "NET", "NEW", "NEWT", "PRAT", "PRY", "QUA", "QUART", 
                "QUARTZ", "RAT", "TAR", "TARP", "TEN", "WENT", "WET", "QUAR"]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

  def test_7x7_grid(self):
    grid = [
      ["A", "B", "C", "D", "E", "F", "G"],
      ["H", "I", "J", "K", "L", "M", "N"],
      ["O", "P", "Q", "R", "S", "T", "U"],
      ["V", "W", "X", "Y", "Z", "A", "B"],
      ["C", "D", "E", "F", "G", "H", "I"],
      ["J", "K", "L", "M", "N", "O", "P"],
      ["Q", "R", "S", "T", "U", "V", "W"]
    ]
    dictionary = ["abc", "tuv", "xyz", "qrst", "klmn", "abcdefg", "hijklmno", "qrstuvw", "wxyz", "nopqrs", "ekq"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["ABC", "TUV", "XYZ", "QRST", "KLMN", "ABCDEFG", "QRSTUVW", "WXYZ", "EKQ"]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

class TestSuite_Simple_Edge_Cases(unittest.TestCase):
  def test_SquareGrid_case_1x1(self):
    grid = [["A"]];
    dictionary = ["a", "b", "c"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

  def test_EmptyGrid_case_0x0(self):
    grid = [[]];
    dictionary = ["hello", "there", "general", "kenobi"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)
  
  def test_EmptyDictionary(self):
    grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    dictionary = []  
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

  

class TestSuite_Complete_Coverage(unittest.TestCase):

  def test_NoWordsFromDictionary(self):
    grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    dictionary = ["xyz", "mno", "pqr"]  
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []  
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)
  
  def test_PartialWordsFromDictionary(self):
    grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    dictionary = ["abc", "cfi", "xyz", "ghi"]  
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["ABC", "CFI", "GHI"]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

class TestSuite_Qu_and_St(unittest.TestCase):

  def test_GridWithMultiLetterCellsValidWords(self):
    grid = [["Qu", "A", "B"], ["C", "Th", "E"], ["F", "G", "H"]]  
    dictionary = ["quiz", "quail", "the", "bat", "cat", "hat"]  
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["THE"]  
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)
  
  def test_GridWithMultipleMultiLetterCellsValidWords(self):
    grid = [["St", "A", "R"], ["Qu", "E", "T"], ["F", "G", "H"]]  
    dictionary = ["star", "start", "quest", "quiet", "rat", "hat", "set"] 
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["STAR", "START", "QUEST", "RAT"] 
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)
  
  def test_GridWithMultipleMultiLetterCellsValidWords(self):
    grid = [["St", "A", "R"], ["Qu", "E", "T"], ["F", "G", "H"]]  
    dictionary = ["stqufgearth", "startequfgh", "star", "start", "quest", "quiet", "rat", "hat", "set"] 
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["STAR", "START", "QUEST", "RAT", "STARTEQUFGH", "STQUFGEARTH"] 
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)



if __name__ == '__main__':
  unittest.main()

