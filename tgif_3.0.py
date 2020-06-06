#https://open.kattis.com/problems/tgif
# WORK IN PROGRESS

month_dd = {
            "JAN": [3, 4], "FEB": [28, 29], "MAR": 14, "APR": 4, 
            "MAY": 9, "JUN": 6, "JUL": 11, "AUG": 8, 
            "SEP": 5, "OCT": 10, "NOV": 7, "DEC": 12
}

days = {
            "SUN": 0, "MON": 1, "TUE": 2, "WED": 3, "THU": 4, 
            "FRI": 5, "SAT": 6 
}

centuries = {3: 1500, 2: 1600, 0: 1700, 5: 1800}

days_num = {
            0: "SUN", 1: "MON", 2: "TUE", 3: "WED" , 4: "THU", 
            5: "FRI", 6: "SAT"
}

date, month = input().split()
day = input()

def century_alg(x):
    century = x
    c1 = int(century[0])
    c2 = int(century[-2:]) // 12
    c3 = int(century[-2:]) % 12
    c4 = c3 // 4

    c5 = c1 + c2 + c3 + c4

    if c5 > 6:
        c5 %= 7
    
    return c5


'''
Date = 13 
Month = JUL 
Year = 2020
Day = 
'''

