# -*- coding: utf-8 -*-
import xlrd
import csv
from os import sys

def csv_from_excel(excel_file):
    workbook = xlrd.open_workbook(excel_file)
    all_worksheets = workbook.sheet_names()
    for worksheet_name in all_worksheets:
        worksheet = workbook.sheet_by_name(worksheet_name)
        your_csv_file = open(''.join([worksheet_name,'.csv']), 'w')
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

        for rownum in range(worksheet.nrows):
            for col_num in range ( worksheet.ncols ) :
                value = str ( worksheet.row (rownum ) [ col_num ].value )
                wr.writerow(list(x.encode('utf-8') if type(x) == type(u'') else x for x in worksheet.row_values(rownum)))
        your_csv_file.close()

#if __name__ == "__main__":
csv_from_excel('G:/Metrixx/Data/ETF_MostTraded.xlsx')
