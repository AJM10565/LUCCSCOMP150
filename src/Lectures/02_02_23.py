"""
Agenda:
Lab 02_02_23.py

kabob-case => web pages
snake_case => python variables and function names
SCREAMING_SNAKE_CASE = constants
camelCase => javascript and java variables and function names
PascalCase => python, Java, Javascript class names
ALSOPascalCase
WikiCase => wiki cross-referencing, no consecutive double capital letters

Reference: https://www.youtube.com/watch?v=MtQoWQForqE

simple data structures review:
strings: "This is a string"
lists: ["this","is","a","list"]
dictionaries: {"Key":"Value"}
"""



# One nice homework solution example:
def problem4(coordinates: str) -> str:
    letters = coordinates[0:1]
    numbers = int(coordinates[1:])
    letter_map = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    letters = letter_map[letters]
    letters_is_even = letters % 2 == 0
    number_is_even = numbers % 2 == 0
    if letters_is_even == number_is_even:
        return "black"
    else:
        return "white"

# globals are bad, don't use them, pass it in if you need it.


# Dont do this:
number_dict = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th", 10: "10th",
               11: "11th", 12: "12th", 13: "13th", 14: "14th", 15: "15th", 16: "16th", 17: "17th", 18: "18th",
               19: "19th", 20: "20th", 21: "21st", 22: "22nd", 23: "23rd", 24: "24th", 25: "25th", 26: "26th",
               27: "27th", 28: "28th", 29: "29th", 30: "30th", 31: "31st", 32: "32nd", 33: "33rd", 34: "34th",
               35: "35th", 36: "36th", 37: "37th", 38: "38th", 39: "39th", 40: "40th", 41: "41st", 42: "42nd",
               43: "43rd", 44: "44th", 45: "45th", 46: "46th", 47: "47th", 48: "48th", 49: "49th", 50: "50th",
               51: "51st", 52: "52nd", 53: "53rd", 54: "54th", 55: "55th", 56: "56th", 57: "57th", 58: "58th",
               59: "59th", 60: "60th", 61: "61st", 62: "62nd", 63: "63rd", 64: "64th", 65: "65th", 66: "66th",
               67: "67th", 68: "68th", 69: "69th", 70: "70th", 71: "71st", 72: "72nd", 73: "73rd", 74: "74th",
               75: "75th", 76: "76th", 77: "77th", 78: "78th", 79: "79th", 80: "80th", 81: "81st", 82: "82nd",
               83: "83rd", 84: "84th", 85: "85th", 86: "86th", 87: "87th", 88: "88th", 89: "89th", 90: "90th",
               91: "91st", 92: "92nd", 93: "93rd", 94: "94th", 95: "95th", 96: "96th", 97: "97th", 98: "98th",
               99: "99th", 100: "100th", }

# Dont do this
chess_dict = {"a1": "black", "a2": "white", "a3": "black", "a4": "white", "a5": "black", "a6": "white", "a7": "black",
              "a8": "white", "b1": "white", "b2": "black", "b3": "white", "b4": "black", "b5": "white", "b6": "black",
              "b7": "white", "b8": "black", "c1": "black", "c2": "white", "c3": "black", "c4": "white", "c5": "black",
              "c6": "white", "c7": "black", "c8": "white", "d1": "white", "d2": "black", "d3": "white", "d4": "black",
              "d5": "white", "d6": "black", "d7": "white", "d8": "black", "e1": "black", "e2": "white", "e3": "black",
              "e4": "white", "e5": "black", "e6": "white", "e7": "black", "e8": "white", "f1": "white", "f2": "black",
              "f3": "white", "f4": "black", "f5": "white", "f6": "black", "f7": "white", "f8": "black", "g1": "black",
              "g2": "white", "g3": "black", "g4": "white", "g5": "black", "g6": "white", "g7": "black", "g8": "white",
              "h1": "white", "h2": "black", "h3": "white", "h4": "black", "h5": "white", "h6": "black", "h7": "white",
              "h8": "black", }

# don't do this:
nochange: dict[int, str] = dict()
nochange[1] = '1st'
nochange[2] = '2nd'
nochange[3] = '3rd'
nochange[4] = '4th'
nochange[5] = '5th'
nochange[6] = '6th'
nochange[7] = '7th'
nochange[8] = '8th'
nochange[9] = '9th'
nochange[10] = '10th'
nochange[11] = '11th'
nochange[12] = '12th'
nochange[13] = '13th'
nochange[14] = '14th'
nochange[15] = '15th'
nochange[16] = '16th'
nochange[17] = '17th'
nochange[18] = '18th'
nochange[19] = '19th'
nochange[20] = '20th'
nochange[21] = '21st'
nochange[22] = '22nd'
nochange[23] = '23rd'
nochange[24] = '24th'
nochange[25] = '25th'
nochange[26] = '26th'
nochange[27] = '27th'
nochange[28] = '28th'
nochange[29] = '29th'
nochange[30] = '30th'
nochange[31] = '31st'
nochange[32] = '32nd'
nochange[33] = '33rd'
nochange[34] = '34th'
nochange[35] = '35th'
nochange[36] = '36th'
nochange[37] = '37th'
nochange[38] = '38th'
nochange[39] = '39th'
nochange[40] = '40th'
nochange[41] = '41st'
nochange[42] = '42nd'
nochange[43] = '43rd'
nochange[44] = '44th'
nochange[45] = '45th'
nochange[46] = '46th'
nochange[47] = '47th'
nochange[48] = '48th'
nochange[49] = '49th'
nochange[50] = '50th'
nochange[51] = '51st'
nochange[52] = '52nd'
nochange[53] = '53rd'
nochange[54] = '54th'
nochange[55] = '55th'
nochange[56] = '56th'
nochange[57] = '57th'
nochange[58] = '58th'
nochange[59] = '59th'
nochange[60] = '60th'
nochange[61] = '61st'
nochange[62] = '62nd'
nochange[63] = '63rd'
nochange[64] = '64th'
nochange[65] = '65th'
nochange[66] = '66th'
nochange[67] = '67th'
nochange[68] = '68th'
nochange[69] = '69th'
nochange[70] = '70th'
nochange[71] = '71st'
nochange[72] = '72nd'
nochange[73] = '73rd'
nochange[74] = '74th'
nochange[75] = '75th'
nochange[76] = '76th'
nochange[77] = '77th'
nochange[78] = '78th'
nochange[79] = '79th'
nochange[80] = '80th'
nochange[81] = '81st'
nochange[82] = '82nd'
nochange[83] = '83rd'
nochange[84] = '84th'
nochange[85] = '85th'
nochange[86] = '86th'
nochange[87] = '87th'
nochange[88] = '88th'
nochange[89] = '89th'
nochange[90] = '90th'
nochange[91] = '91st'
nochange[92] = '92nd'
nochange[93] = '93rd'
nochange[94] = '94th'
nochange[95] = '95th'
nochange[96] = '96th'
nochange[97] = '97th'
nochange[98] = '98th'
nochange[99] = '99th'
nochange[100] = '100th'


# this is oK, but still pretty bad: pass in board to the function, don't use globals, don't repeat yourself
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
            (board[3] == icon and board[4] == icon and board[5] == icon) or \
            (board[6] == icon and board[7] == icon and board[8] == icon) or \
            (board[0] == icon and board[3] == icon and board[6] == icon) or \
            (board[1] == icon and board[4] == icon and board[7] == icon) or \
            (board[2] == icon and board[5] == icon and board[8] == icon) or \
            (board[0] == icon and board[4] == icon and board[8] == icon) or \
            (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False
