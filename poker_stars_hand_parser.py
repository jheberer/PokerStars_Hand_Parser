
hand_history_path = r"C:\Users\jrheb\AppData\Local\PokerStars.USMI\HandHistory\OldGregg686\HH20250429 Rigel - $0.02-$0.05 - USD No Limit Hold'em.txt"

hands = {}

with open(hand_history_path, 'r', encoding='utf-8-sig') as file:
    table_contents = file.readlines()

for row in table_contents:
    line = row.split()

    if len(line) > 0:
        # first word of line
        first_word = line[0]
        
        if first_word == 'PokerStars':
            print('Start of Hand')