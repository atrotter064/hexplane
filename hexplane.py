class Hexplane:
  
  def __init__(self, edge_length):
    self.edge = edge_length
    self._hex = [0 for _ in range(0, (self.edge * 2  - 1) ** 2)]
    
  def __getitem__(self, key):
    if self._validate_key(key):
      return self._hex[self._translate(key)]
    
  def __setitem__(self, key, item):
    if self._validate_key(key):
      self._hex[self._translate(key)] = item
      
  def _translate(self, key):
    return key[0] * ((self.edge * 2) - 1) + key[1]
    
  def _validate_key(self, key):
    if isinstance(key, tuple):
      return abs(key[0] - key[1]) < self.edge
    raise TypeError("hex indices must be tuples")
    
  def __str__(self):
    s = ""
    for i in range(self.edge * 2 - 1):
      s +=  " " * abs(self.edge - 1 - i)
      for j in range(self.edge * 2 - 1):
        if self._validate_key((i, j)):
          s += str(self[(i, j)]) + " "
      s += "\n"
    return s


a = Hexplane(4)
a[(4, 2)] = 3
print(a)


