file1 = open('text_test.txt', 'r')
Lines = file1.readlines()
print(Lines[1].strip()[11:])
dic = {'Bullish Two_Crows': 0,
       'Bearish Two_Crows': 0,
       'Bullish Three_Black_Crows': 0,
       'Bearish Three_Black_Crows': 0,
       'Bullish Three_Inside_Up_Down': 0,
       'Bearish Three_Inside_Up_Down': 0,
       'Bullish Three_Line_Strike': 0,
       'Bearish Three_Line_Strike': 0,
       'Bullish Three_Stars_In_The_South': 0,
       'Bearish Three_Stars_In_The_South': 0,
       'Bullish Three_Advancing_White_Soldiers': 0,
       'Bearish Three_Advancing_White_Soldiers': 0,
       'Bullish Abandoned_Baby': 0,
       'Bearish Abandoned_Baby': 0,
       'Bullish Belt_hold': 0,
       'Bearish Belt_hold': 0,
       'Bullish Breakaway': 0,
       'no_pattern':0}

for i in range(1, len(Lines), 2):
    print(Lines[i].strip()[12:len(Lines[i].strip()) - 1])
    dic[Lines[i].strip()[12:len(Lines[i].strip()) - 1]] = 0

# print("dict", dic)
res = 100000000000000000000000000000000000000
for i in dic.items():
       if i[0] == 'Bullish Engulfing_Pattern':
              dic[i[0]] = res
print(dic)
for i in dic.items():
       print(i)
