#6 tag HTML yang terdefinisi (case-sensitive):
#1. html
#2. head
#3. h1
#4. body
#5. title
#6. p

def DFA(baris):
    state = "1"
    status = "Rejected"
    for char in baris:
        #print(state)
        if state == "1":
            if char == '<':
                state = "2"
            else:
                state = "0"
        elif state == "2":
            if char == 'h':
                state = "3"
            elif char == 'b':
                state = "33"
            elif char == 't':
                state = "45"
            elif char == 'p':
                state = "59"
            elif char == '/':
                state = "65"
            else:
                state = "0"
        elif state == "3":
            if char == 't':
                state = "4"
            elif char == 'e':
                state = "15"
            elif char == '1':
                state = "26"
            else:
                state = "0"
        elif state == "4":
            if char == 'm':
                state = "5"
            else:
                state = "0"
        elif state == "5":
            if char == 'l':
                state = "6"
        elif state == "6":
            if char == '>':
                state = "7"
            else:
                state = "0"
        elif state == "7":
            if char == ' ':
                state = "7"
            elif char == '<':
                state = "8"
            else:
                state = "0"
        elif state == "8":
            if char == '/':
                state = "9"
            else:
                state = "0"
        elif state == "9":
            if char == 'h':
                state = "10"
            else:
                state = "0"
        elif state == "10":
            if char == 't':
                state = "11"
            else:
                state = "0"
        elif state == "11":
            if char == 'm':
                state = "12"
            else:
                state = "0"
        elif state == "12":
            if char == 'l':
                state = "13"
            else:
                state = "0"
        elif state == "13":
            if char == '>':
                state = "14"
            else:
                state = "0"
        elif state == "15":
            if char == 'a':
                state = "16"
            else:
                state = "0"
        elif state == "16":
            if char == 'd':
                state = "17"
            else:
                state = "0"
        elif state == "17":
            if char == '>':
                state = "18"
            else:
                state = "0"
        elif state == "18":
            if char == ' ':
                state = "18"
            elif char == '<':
                state = "19"
            else:
                state = "0"
        elif state == "19":
            if char == '/':
                state = "20"
            else:
                state = "0"
        elif state == "20":
            if char == 'h':
                state = "21"
            else:
                state = "0"
        elif state == "21":
            if char == 'e':
                state = "22"
            else:
                state = "0"
        elif state == "22":
            if char == 'a':
                state = "23"
            else:
                state = "0"
        elif state == "23":
            if char == 'd':
                state = "24"
            else:
                state = "0"
        elif state == "24":
            if char == '>':
                state = "25"
            else:
                state = "0"
        elif state == "26":
            if char == '>':
                state = "27"
            else:
                state = "0"
        elif state == "27":
            if char == ' ':
                state = "27"
            elif (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z') or (char >= '0' and char <= '9') or (char == ' ') or (char == '.') or (char == ',') or (char == ';') or (char == ':'):
                state = "71"
            elif char == '<':
                state = "28"
            else:
                state = "0"
        elif state == "71":
            if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z') or (char >= '0' and char <= '9') or (char == ' ') or (char == '.') or (char == ',') or (char == ';') or (char == ':'):
                state = "71"
            elif char == '<':
                state = "28"
            else:
                state = "0"
        elif state == "28":
            if char == '/':
                state = "29"
            else:
                state = "0"
        elif state == "29":
            if char == 'h':
                state = "30"
            else:
                state = "0"
        elif state == "30":
            if char == '1':
                state = "31"
            else:
                state = "0"
        elif state == "31":
            if char == '>':
                state = "32"
            else:
                state = "0"
        elif state == "33":
            if char == 'o':
                state = "34"
            else:
                state = "0"
        elif state == "34":
            if char == 'd':
                state = "35"
            else:
                state = "0"
        elif state == "35":
            if char == 'y':
                state = "36"
            else:
                state = "0"
        elif state == "36":
            if char == '>':
                state = "37"
            else:
                state = "0"
        elif state == "37":
            if char == ' ':
                state = "37"
            elif char == '<':
                state = "38"
            else:
                state = "0"
        elif state == "38":
            if char == '/':
                state = "39"
            else:
                state = "0"
        elif state == "39":
            if char == 'b':
                state = "40"
            else:
                state = "0"
        elif state == "40":
            if char == 'o':
                state = "41"
            else:
                state = "0"
        elif state == "41":
            if char == 'd':
                state = "42"
            else:
                state = "0"
        elif state == "42":
            if char == 'y':
                state = "43"
            else:
                state = "0"
        elif state == "43":
            if char == '>':
                state = "44"
            else:
                state = "0"
        elif state == "45":
            if char == 'i':
                state = "46"
            else:
                state = "0"
        elif state == "46":
            if char == 't':
                state = "47"
            else:
                state = "0"
        elif state == "47":
            if char == 'l':
                state = "48"
            else:
                state = "0"
        elif state == "48":
            if char == 'e':
                state = "49"
            else:
                state = "0"
        elif state == "49":
            if char == '>':
                state = "50"
            else:
                state = "0"
        elif state == "50":
            if char == ' ':
                state = "50"
            elif (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z') or (char >= '0' and char <= '9') or (char == ' ') or (char == '.') or (char == ',') or (char == ';') or (char == ':'):
                state = "73"
            elif char == '<':
                state = "51"
            else:
                state = "0"
        elif state == "73":
            if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z') or (char >= '0' and char <= '9') or (char == ' ') or (char == '.') or (char == ',') or (char == ';') or (char == ':'):
                state = "73"
            elif char == '<':
                state = "51"
            else:
                state = "0"
        elif state == "51":
            if char == '/':
                state = "52"
            else:
                state = "0"
        elif state == "52":
            if char == 't':
                state = "53"
            else:
                state = "0"
        elif state == "53":
            if char == 'i':
                state = "54"
            else:
                state = "0"
        elif state == "54":
            if char == 't':
                state = "55"
            else:
                state = "0"
        elif state == "55":
            if char == 'l':
                state = "56"
            else:
                state = "0"
        elif state == "56":
            if char == 'e':
                state = "57"
            else:
                state = "0"
        elif state == "57":
            if char == '>':
                state = "58"
            else:
                state = "0"
        elif state == "59":
            if char == '>':
                state = "60"
            else:
                state = "0"
        elif state == "60":
            if char == ' ':
                state = "60"
            elif (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z') or (char >= '0' and char <= '9') or (char == ' ') or (char == '.') or (char == ',') or (char == ';') or (char == ':'):
                state = "72"
            elif char == '<':
                state = "61"
            else:
                state = "0"
        elif state == "72":
            if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z') or (char >= '0' and char <= '9') or (char == ' ') or (char == '.') or (char == ',') or (char == ';') or (char == ':'):
                state = "72"
            elif char == '<':
                state = "61"
            else:
                state = "0"
        elif state == "61":
            if char == '/':
                state = "62"
            else:
                state = "0"
        elif state == "62":
            if char == 'p':
                state = "63"
            else:
                state = "0"
        elif state == "63":
            if char == '>':
                state = "64"
            else:
                state = "0"
        elif state == "65":
            if char == 'h':
                state = "66"
            elif char == 'b':
                state = "80"
            elif char == 't':
                state = "85"
            elif char == 'p':
                state = "92"
            else:
                state = "0"
        elif state == "66":
            if char == 't':
                state = "67"
            elif char == 'e':
                state = "74"
            elif char == '1':
                state = "78"
            else:
                state = "0"
        elif state == "67":
            if char == 'm':
                state = "68"
            else:
                state = "0"
        elif state == "68":
            if char == 'l':
                state = "69"
            else:
                state = "0"
        elif state == "69":
            if char == '>':
                state = "70"
            else:
                state = "0"
        elif state == "74":
            if char == 'a':
                state = "75"
            else:
                state = "0"
        elif state == "75":
            if char == 'd':
                state = "76"
            else:
                state = "0"
        elif state == "76":
            if char == '>':
                state = "77"
            else:
                state = "0"
        elif state == "77":
            if char == ' ':
                state == "77"
            elif char == '<':
                state = "93"
            else:
                state = "0"
        elif state == "78":
            if char == '>':
                state = "79"
            else:
                state = "0"
        elif state == "80":
            if char == 'o':
                state = "81"
            else:
                state = "0"
        elif state == "81":
            if char == 'd':
                state = "82"
            else:
                state = "0"
        elif state == "82":
            if char == 'y':
                state = "83"
            else:
                state = "0"
        elif state == "83":
            if char == '>':
                state = "84"
            else:
                state = "0"
        elif state == "84":
            if char == ' ':
                state = "84"
            elif char == '<':
                state = "100"
            else:
                state = "0"
        elif state == "85":
            if char == 'i':
                state = "86"
            else:
                state = "0"
        elif state == "86":
            if char == 't':
                state = "87"
            else:
                state = "0"
        elif state == "87":
            if char == 'l':
                state = "88"
            else:
                state = "0"
        elif state == "88":
            if char == 'e':
                state = "89"
            else:
                state = "0"
        elif state == "89":
            if char == '>':
                state = "90"
            else:
                state = "0"
        elif state == "91":
            if char == '>':
                state = "92"
            else:
                state = "0"
        elif state == "93":
            if char == '/':
                state = "94"
            else:
                state = "0"
        elif state == "94":
            if char == 'h':
                state = "95"
            else:
                state = "0"
        elif state == "95":
            if char == 't':
                state = "96"
            else:
                state = "0"
        elif state == "96":
            if char == 'm':
                state = "97"
            else:
                state = "0"
        elif state == "97":
            if char == 'l':
                state = "98"
            else:
                state = "0"
        elif state == "98":
            if char == '>':
                state = "99"
            else:
                state = "0"
        elif state == "100":
            if char == '/':
                state = "101"
            else:
                state = "0"
        elif state == "101":
            if char == 'h':
                state = "102"
            else:
                state = "0"
        elif state == "102":
            if char == 't':
                state = "103"
            else:
                state = "0"
        elif state == "103":
            if char == 'm':
                state = "104"
            else:
                state = "0"
        elif state == "104":
            if char == 'l':
                state = "105"
            else:
                state = "0"
        elif state == "105":
            if char == '>':
                state = "106"
            else:
                state = "0"
        elif state == "0":
            state = "0"

    if state == "7" or state == "14" or state == "18" or state == "25" or state == "27" or state == "32" or state == "37" or state == "44" or state == "50" or state == "58" or state == "60" or state == "64" or state == "70" or state == "77" or state == "79" or state == "84" or state == "90" or state == "92" or state == "99" or state == "106":
        status = "ACCEPTED"
        #<html>
        if state == "7":
            return "1", status
        #<html> </html>
        elif state == "14":
            return "p", status
        #<head>
        elif state == "18":
            return "2", status
        #<head> </head>
        elif state == "25":
            return "q", status
        #<h1>
        elif state == "27":
            return "3", status
        #<h1> data </h1>
        elif state == "32":
            return "r", status
        #<body>
        elif state == "37":
            return "4", status
        #<body> </body>    
        elif state == "44":
            return "s", status
        #<title>
        elif state == "50":
            return "5", status
        #<title> data </title>
        elif state == "58":
            return "t", status
        #<p>
        elif state == "60":
            return "6", status
        #<p> data </p>
        elif state == "64":
            return "u", status
        #</html>
        elif state == "70":
            return "a", status
        #</head>
        elif state == "77":
            return "b", status
        #</h1>
        elif state == "79":
            return "c", status
        #</body>
        elif state == "84":
            return "d", status
        #</title>
        elif state == "90":
            return "e", status
        #</p>
        elif state == "92":
            return "f", status
        #</head> </html>
        elif state == "99":
            return "j ", status
        #</body> </html>
        elif state == "106":
            return "k ", status
    else:
        return "NULL", status
    
def Parser(data):
    state = "0"
    stack = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"] 
    top = 0
    for char in data:
        #print (state)
        if state == "0":
            if char == '1':
                stack[top] = "#"
                top += 1
                state = "1"
            elif char == 'p':
                state = "9"
            else:
                state = "error"
        elif state == "1":
            if char == '2':
                stack[top] = "2"
                top += 1
                state = "2"
            elif char == 'a':
                top -= 1
                if stack[top] == "#":
                    stack[top] = "x"
                    state = "9"
                else:
                    state = "error"
            else:
                state = "error"
        elif state == "2":
            if char == 't':
                state = "3"
            elif char == 'b':
                top -= 1
                if stack[top] == "2":
                    stack[top] = "x"
                    state = "4"
                else:
                    state = "0"
            elif char == 'j':
                top -= 1
                if stack[top] == "2":
                    stack[top] = "x"
                    state = "10"
                else:
                    state = "0"
            else:
                state = "error"
        elif state == "3":
            if char == 'b':
                top -= 1
                if stack[top] == "2":
                    stack[top] = "x"
                    state = "4"
                else:
                    state = "0"
            elif char == 'j':
                top -= 1
                if stack[top] == "2":
                    stack[top] = "x"
                    state = "10"
                else:
                    state = "0"
            else:
                state = "error"
        elif state == "4":
            if char == '4':
                stack[top] = "4"
                top += 1
                state = "5"
            elif char == 'a':
                top -= 1 
                if stack[top] == "#":
                    stack[top] = "x"
                    state = "9"
                else:
                    state = "0"
            else:
                state = "error"
        elif state == "5":
            if char == 'r':
                state = "5"
            elif char == 'u':
                state = "5"
            elif char == 'd':
                top -= 1
                if stack[top] == "4":
                    stack[top] = "x"
                    state = "8"
                else:
                    state = "error"
            elif char == 'k':
                top -= 1
                if stack[top] == "4":
                    stack[top] = "x"
                    state = "10"
                else:
                    state = "error"
            else:
                state = "error"
        elif state == "7":
            if char == 'd':
                top -= 1
                if stack[top] == "4":
                    stack[top] = "x"
                    state = "8"
                else:
                    state = "error"
            elif char == 'k':
                top -= 1
                if stack[top] == "4":
                    stack[top] = "x"
                    state = "10"
                else:
                    state = "error"
            else:
                state = "error"
        elif state == "8":
            if char == 'a':
                top -= 1
                if stack[top] == "#":
                    stack[top] = "x"
                    state = "9"
                else:
                    state = "error"
            else:
                state = "error"
        elif state == "10":
            if char == ' ':
                top -= 1
                if stack[top] == "#":
                    stack[top] = "x"
                    state = "9"
                else:
                    state = "error"
            else:
                state = "error"
        elif state == "error":
            state = "error"
    if state == "9":
        return "Accepted"
    else:
        return "Rejected"

def main():
    kondisi3 = True
    kalimat = ""
    print("Mengecek sususan file HTML")
    while kondisi3:
        try:
            token = input()
            kata, result = DFA(token)
            kalimat += kata
            result = Parser(kalimat)
        except EOFError:
            kondisi3 = False
    print()
    print(f"Hasil dari struktur yang Anda buat: {result}")
    print("=============================================")

main()