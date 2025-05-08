
import re
from datetime import datetime
from pathlib import Path


hand_info = {}


def parse_hand_header_info(header_line: str, sub_header_line: str) -> dict:
    header_info = {}

    # table_nm
    sub_header_elements = sub_header_line.split()
    header_info['table_nm'] = sub_header_elements[1].strip("'")

    # button_seat
    header_info['button_seat_num'] = sub_header_elements[4].strip('#')

    # table_size
    header_info['table_size'] = sub_header_elements[2][0]

    # hand_id
    hand_id_start_index = header_line.find('#') + 1
    hand_id_end_index = header_line.find(':')
    hand_id = header_line[hand_id_start_index:hand_id_end_index]

    header_info['hand_id'] = hand_id

    # small_blind_amt
    hand_stakes_sb_start_index = header_line.find('$') + 1
    hand_stakes_sb = header_line[hand_stakes_sb_start_index:hand_stakes_sb_start_index + 4]

    header_info['small_blind_amt'] = hand_stakes_sb

    # big_blind_amt
    hand_stakes_bb_start_index = header_line.find('$', hand_stakes_sb_start_index + 1) + 1
    hand_stakes_bb = header_line[hand_stakes_bb_start_index:hand_stakes_bb_start_index + 4]

    header_info['big_blind_amt'] = hand_stakes_bb

    # stakes
    stakes_desc = str(int(float(hand_stakes_bb) * 100)) + 'NL'
    header_info['stakes_desc'] = stakes_desc

    # hand time
    date_match = re.search(r'- (\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}) ET', header_line)
    if date_match:
        hand_start_dttm = datetime.strptime(date_match.group(1), "%Y/%m/%d %H:%M:%S")
        header_info['hand_start_dttm'] = hand_start_dttm

    return header_info


def parse_board_runout(lines: list) -> dict:
    board = {
        'flop_card_1': None,
        'flop_card_2': None,
        'flop_card_3': None,
        'turn_card': None,
        'river_card': None,
        'showdown_ind': False,
        'hero_hole_card_1': None,
        'hero_hole_card_2': None
    }

    for line in lines:
        if 'Dealt to' in line:
            hole_cards = re.findall(r'\[([^\]]+)\]', line)[0].split()
            if hole_cards:
                board['hero_hole_card_1'] = hole_cards[0]
                board['hero_hole_card_2'] = hole_cards[1]

        elif '*** FLOP ***' in line:
            flop_cards = re.findall(r'\[([^\]]+)\]', line)[0].split()
            if flop_cards:
                board['flop_card_1'] = flop_cards[0]
                board['flop_card_2'] = flop_cards[1]
                board['flop_card_3'] = flop_cards[2]

        elif '*** TURN ***' in line:
            turn_match = re.findall(r'\[([^\]]+)\] \[([^\]]+)\]', line)
            if turn_match:
                board['turn_card'] = turn_match[0][1]

        elif '*** RIVER ***' in line:
            river_match = re.findall(r'\[([^\]]+)\] \[([^\]]+)\]', line)
            if river_match:
                board['river_card'] = river_match[0][1]

        elif '*** SHOW DOWN ***' in line:
            board['showdown_ind'] = True
    
    return board


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
    hand_lines = hand.split('\n')

    # headers
    hand_header = hand_lines[0]
    hand_subheader = hand_lines[1]
    header_info = parse_hand_header_info(hand_header, hand_subheader)
    hand_info.update(header_info)

    # board
    board = parse_board_runout(hand_lines)
    hand_info.update(board)

    print(hand_info)