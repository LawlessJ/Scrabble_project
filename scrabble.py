letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letters_to_points = {key:value for key,value in zip(letters,points)}
letters_to_points[" "] = 0
print(letters_to_points)

def score_word(word):
  point_total = 0
  for letter in word:
    if letter not in letters_to_points:
      letter = letter.upper()
    points =letters_to_points.get(letter, 0)
    point_total += points
  return point_total
#print(score_word("QI"))  
brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {"player1":["Blue", "TENNIS", "EXIT"], "wordNerd":["EARTH", "EYES", "MACHINE"], "Lexi_Con":["ERASER", "BELLY", "HUSKY"], "Prof_Reader":["ZAP", "COMA", "PERIOD"]}

def update_point_totals():
  player_to_points = {}
  for player,words in player_to_words.items():
   player_points = 0
   for word in words:
    player_points += score_word(word)
    player_to_points[player] = player_points
  return player_to_points

def play_word(player,word):
  if player in player_to_words:
    player_to_words[player].append(word)
  else:
    player_to_words[player] = word
  return player_to_words  

print(update_point_totals())
play_word("player1", "WOW")
play_word("wordNerd", "Good")
print(update_point_totals())
