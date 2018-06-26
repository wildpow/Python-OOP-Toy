def front_x(words):
  # Your code here
  x_words = []
  other_w = [] # Did have to create 2 lists
  for w in words: 
    # w.split() // not needed becuase your already comparing 
    # the first letter of the string below
    if w[0] == 'x':
      # w.join(x_words) // join takes at least one argument 
      x_words.append(w)
    else:
      other_w.append(w)
    x_words.sort()  
    other_w.sort()
  return x_words + other_w

a = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']

print(front_x(a))