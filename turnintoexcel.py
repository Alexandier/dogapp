import xlwt
from getdata import *
import xlsxwriter
from PIL import Image
from convertintophoto import *

def käännä(data: list):

    lista1, lista2 = data

    lista2 = kuva(lista2)

    wb = xlsxwriter.Workbook('jotain.xls')

    sheet = wb.add_worksheet()

    määrä = min(len(lista1), len(lista2))

    sheet.set_column('A:B', 20)
    sheet.set_column('B:B', 15)
    sheet.set_default_row(50)

    for i in range(määrä):
        sheet.write(i, 0, lista1[i])

    for i in range(määrä):
        image = Image.open("image{}.png".format(i))
        new_image = image.resize((120, 65))
        new_image.save("image{}.png".format(i))
        sheet.insert_image(i, 1, "image{}.png".format(i))

    wb.close()


käännä(getdata("https://dogtime.com/dog-breeds/profiles"))