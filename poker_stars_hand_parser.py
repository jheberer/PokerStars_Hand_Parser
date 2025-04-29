
hand_history_path = r"C:\Users\jrheb\AppData\Local\PokerStars.USMI\HandHistory\OldGregg686\HH20250429 Rigel - $0.02-$0.05 - USD No Limit Hold'em.txt"

hands = {}

with open(hand_history_path, 'r', encoding='utf-8-sig') as file:
    table_contents = file.read()

# hands are separated by 4 new lines
hands_list = table_contents.split('\n\n\n\n')

# delete the last "hand"--it's a lonely new line
# del hands_list[-1]

hand_list_length = len(hands_list)

for hand in hands_list:
    print('_________NEW____________')
    hand_breakdown = hand.split('\n')
    print(hand_breakdown)
    # for item in hand:
    #     print("-------------------NEW----------------------")
    #     print(hand_breakdown)

    # get hand index. this is static
    # uq_hand_id_index_start = hand.index('#')
    # uq_hand_id_index_end = hand.index('#')
    # print(hand[uq_hand_id_index+1])