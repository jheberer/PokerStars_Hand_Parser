
from datetime import datetime


def extract_hand_header_info(header_line: list, sub_header_line: list) -> dict:
    header_info = {}

    # table_name

    # button_seat

    # hand_id
    hand_id_start_index = hand_header.find('#') + 1
    hand_id_end_index = hand_header.find(':')
    hand_id = hand_header[hand_id_start_index:hand_id_end_index]

    header_info['hand_id'] = hand_id

    # small_blind_amt
    hand_stakes_sb_start_index = hand_header.find('$') + 1
    hand_stakes_sb = hand_header[hand_stakes_sb_start_index:hand_stakes_sb_start_index + 4]

    header_info['small_blind_amt'] = hand_stakes_sb

    # big_blind_amt
    hand_stakes_bb_start_index = hand_header.find('$', hand_stakes_sb_start_index + 1) + 1
    hand_stakes_bb = hand_header[hand_stakes_bb_start_index:hand_stakes_bb_start_index + 4]

    header_info['big_blind_amt'] = hand_stakes_bb

    # stakes
    stakes_desc = str(int(float(hand_stakes_bb) * 100)) + 'NL'
    header_info['stakes_desc'] = stakes_desc

    # hand time

    return header_info


hand_history_path = r"C:\Users\jrheb\AppData\Local\PokerStars.USMI\HandHistory\OldGregg686\HH20250429 Rigel - $0.02-$0.05 - USD No Limit Hold'em - test.txt"

hands = {}

with open(hand_history_path, 'r', encoding='utf-8-sig') as file:
    table_contents = file.read()

# hands are separated by 4 new lines
hands_list = table_contents.split('\n\n\n\n')

# delete the last "hand"--it's a lonely new line
# del hands_list[-1]

# hand_list_length = len(hands_list)

for hand in hands_list:
    hand_breakdown = hand.split('\n')

    # hand info function can go here
    hand_header = hand_breakdown[0]
    header_info = extract_hand_header_info(hand_header)
    print(header_info)
    

    # hands[hand_id] = hand_breakdown[1:]

# print(hands["255768010672"])