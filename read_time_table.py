import openpyxl
from time import strftime
from os import system


def load_data(work_book_name:str, sheet_name:str, weekday:str):
    wb = openpyxl.load_workbook(work_book_name)
    sheet = wb[sheet_name]
    week_day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    weekday_index = week_day.index(weekday)
    info = []
    table = ''
    for row in sheet.rows:
        info.append((row[0].value, row[weekday_index].value))
        table += str(row[0].value) + '  ' + str(row[weekday_index].value) + '\n'
    print(info)
    return info

def save_data(info):
    with open('Lesson.txt', mode='w', encoding='utf-8') as f:
       for i in info:
           f.write(str(i[0]) + '  ' + str(i[1]) + '\n')

# print(time.strftime('%A'))
info = load_data('课程表.xlsx', 'Sheet1', strftime('%A'))
# info = load_data('课程表.xlsx', 'Sheet1', 'Wednesday')
save_data(info)
# startfile('Chatting.bat')
system('Chatting.bat')
