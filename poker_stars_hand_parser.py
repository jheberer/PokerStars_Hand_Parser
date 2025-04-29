
hand_history_path = r"C:\Users\jrheb\AppData\Local\PokerStars.USMI\HandHistory\OldGregg686\HH20250429 Rigel - $0.02-$0.05 - USD No Limit Hold'em.txt"

hands = {}

with open(hand_history_path, 'r', encoding='utf-8-sig') as file:
    table_contents = file.read()

# hands are separated by 4 new lines
hands_list = table_contents.split('\n\n\n\n')

# delete the last "hand"--it's a lonely new line
del hands_list[-1]

hand_list_length = len(hands_list)

for hand in hands_list:
    hand_breakdown = hand.split('\n')
    hands[hand_breakdown[0]] = hand_breakdown[1:]

print(hands["PokerStars Hand #255768010672:  Hold'em No Limit ($0.02/$0.05 USD) - 2025/04/29 14:08:59 ET"])