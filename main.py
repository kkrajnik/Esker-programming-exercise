analysis = {
  'character count' : 0,
  'line count' : 0,
  'word count' : 0,
  'letter count' : 0,
  'number count' : 0,
  'other characters': 0,
}
word_lengths = {}

with open("samplefile.txt", "r") as text_file:
  end = False
  while   end == False:
    line = text_file.readline()
    if  line == "":
      end = True
    else:
      line = line.strip("\n")
      analysis['line count'] += 1
      analysis['character count'] += len(line)
      words = line.split(" ")
      for word in words:
        word = word.strip(".")
        if word.isalpha():
          analysis['word count'] += 1
          analysis['letter count'] += len(word)
          if len(word) in word_lengths:
            pass
          else:
            word_lengths[len(word)] = 0
          word_lengths[len(word)] += 1
        elif word.isdigit():
          analysis['number count'] += len(word)
  analysis['other characters'] = analysis['character count'] - analysis['letter count'] - analysis['number count']
        
        
      
  print "Line Count: " + str(analysis['line count'])
  print "Character count: " + str(analysis['character count'])
  print "Letter count: " + str(analysis['letter count'])
  print "Number Count: " + str(analysis['number count'])
  print "Other Characters: " + str(analysis['other characters'])
  print "Word Count: " + str(analysis['word count'])
  for count in word_lengths:
    print "Number of " + str(count) + " letter words: " + str(word_lengths[count])
