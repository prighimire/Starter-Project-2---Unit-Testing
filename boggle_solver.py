class Boggle:
  def __init__(self, grid, dictionary):
    self.grid = self.setGrid(grid)
    print(self.grid)
    self.dictionary = [word.upper() for word in dictionary]
    self.solution=set() 
    self.N=len(grid)
    if self.N == 0 or len(self.grid[0]) == 0:     
      self.visited = []
    else:
      self.visited=[[False for x in range(self.N)] for x in range(self.N)] 
    self.word_map = {}
    self.build_word_map(self.dictionary)

  def build_word_map(self, dictionary):
    for word in dictionary:
      for i in range(1, len(word) + 1):
        prefix = word[:i]
        if prefix not in self.word_map:
          self.word_map[prefix] = 0
      self.word_map[word] = 1
  
  def setGrid(self,grid):
    if not grid:
      return []
    
    self.N = len(grid)
    return [[letter.upper() for letter in row] for row in grid] if grid else []
  
  def setDictionary(self,dictionary):
    self.dictionary=dictionary
  
  def setDictionary(self, dictionary):
    self.word_map = {} 
    self.build_word_map(dictionary)
  
  def is_valid(self, current_word):
    return len(current_word) >= 3 and self.word_map.get(current_word) == 1

  def getSolution(self):
    if not self.dictionary: 
        return []
    if self.N == 0 or len(self.grid[0]) == 0:
      return []
    for i in range(self.N):
      for j in range(self.N):
        self.dfs(i,j,self.grid[i][j])
    return list(self.solution)
  
  def isvalid(self,current_word):
    return len(current_word)>=3 and current_word in self.dictionary

  def dfs(self,i,j,current_word):
    if i < 0 or i >= self.N or j < 0 or j >= self.N or self.visited[i][j]:
      return

    if current_word not in self.word_map:
      return
    if self.is_valid(current_word):
      self.solution.add(current_word)
    self.visited[i][j] = True

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for dr, dc in directions:
      x = i + dr
      y = j + dc
      try:
        self.dfs(x, y, current_word+self.grid[x][y])
      except:
        continue
      
    self.visited[i][j] = False


def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    '''
    mygame = Boggle(grid, dictionary)
    print(sorted(mygame.getSolution()))
    print(sorted(mygame.dictionary))
    '''
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"], ["G", "Z", "Qu", "R"], ["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", 
                  "rat", "tar", "tarp", "ten", "went", "wet", "arty", "not", "quar"]
    mygame = Boggle(grid, dictionary)
    print(sorted(mygame.getSolution()))
    print(sorted(["ART", "EGO", "GENT", "GET", "NET", "NEW", "NEWT", "PRAT", "PRY", "QUA", "QUART", 
                "QUARTZ", "RAT", "TAR", "TARP", "TEN", "WENT", "WET", "NOT", "QUAR"]))

if __name__ == "__main__":
    main()
