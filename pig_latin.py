
vowels = ["a", "e", "i", "o", "u", 'A','E','I','O','U' ]
constiantants= ["b","c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "y", "z"]
def translate(word_or_phrase):
  translated = ""
  words = word_or_phrase.split()
  # print(words)
  for word in words:
    if word[0] in vowels:
  #   if word.startswith(vowels):
      # print(word)
      word += 'ay '
      translated += word
    else:translated += word[1:] + word[0] + "ay "
  return (translated)
    
translate('apple pie laundry oats cracker Eggplant')

translate('apple')

translate('three')

translate('school')