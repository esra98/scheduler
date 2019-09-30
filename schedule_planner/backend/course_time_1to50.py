from bs4 import BeautifulSoup
import requests, itertools


def deneme(course_name, days_selected):
    days_available = []
    if 1 in days_selected:
        days_available.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])
    if 2 in days_selected:
        days_available.extend([11, 12, 13, 14, 15, 16, 17, 18, 19])
    if 3 in days_selected:
        days_available.extend([21, 22, 23, 24, 25, 26, 27, 28, 29])
    if 4 in days_selected:
        days_available.extend([31, 32, 33, 34, 35, 36, 37, 38, 39])
    if 5 in days_selected:
        days_available.extend([41, 42, 43, 44, 45, 46, 47, 48, 49])

    course_name_code = course_name[0:3]
    course_name = course_name.replace(" ", "+")
    url = "http://ituscheduler.com/courses?major=" + course_name_code + "&code=" + course_name + "&day=&semester=F19"
    r = requests.get(url)
    source = BeautifulSoup(r.content, "lxml")
    products = source.findAll("tr")
    list = []
    for element in products:
        course_time_code = []
        course_cnr = element.find("th").text
        course_day = str(element.select("td:nth-of-type(5)"))
        course_day = course_day[5:-11]
        course_slot = str(element.select("td:nth-of-type(6)"))
        course_slot = course_slot[5:-11]
        if len(course_day) > 12:
            if course_day.startswith("Pa"):

                if course_slot.startswith("8"):
                    course_time_code = [1, 2]
                if course_slot.startswith("9"):
                    course_time_code = [2, 3]
                if course_slot.startswith("10"):
                    course_time_code = [3, 4]
                if course_slot.startswith("11"):
                    course_time_code = [4, 5]
                if course_slot.startswith("12"):
                    course_time_code = [5, 6]
                if course_slot.startswith("13"):
                    course_time_code = [6, 7]
                if course_slot.startswith("14"):
                    course_time_code = [7, 8]
                if course_slot.startswith("15"):
                    course_time_code = [8, 9]
                if "Salı" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([11, 12])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([12, 13])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([13, 14])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([14, 15])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([15, 16])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([16, 17])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([17, 18])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([18, 19])
                if "Çarşamba" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([21, 22])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([22, 23])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([23, 24])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([24, 25])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([25, 26])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([26, 27])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([27, 28])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([28, 29])
                if "Perşembe" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([31, 32])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([32, 33])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([33, 34])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([34, 35])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([35, 36])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([36, 37])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([37, 38])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([38, 39])
                if "Cuma" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([41, 42])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([42, 43])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([43, 44])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([44, 45])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([45, 46])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([46, 47])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([47, 48])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([48, 49])
            if course_day.startswith("Sa"):

                if course_slot.startswith("8"):
                    course_time_code = [11, 12]
                if course_slot.startswith("9"):
                    course_time_code = [12, 13]
                if course_slot.startswith("10"):
                    course_time_code = [13, 14]
                if course_slot.startswith("11"):
                    course_time_code = [14, 15]
                if course_slot.startswith("12"):
                    course_time_code = [15, 16]
                if course_slot.startswith("13"):
                    course_time_code = [16, 17]
                if course_slot.startswith("14"):
                    course_time_code = [17, 18]
                if course_slot.startswith("15"):
                    course_time_code = [18, 19]
                if "Pazartesi" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([1, 2])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([2, 3])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([3, 4])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([4, 5])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([5, 6])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([6, 7])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([7, 8])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([8, 9])
                if "Çarşamba" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([21, 22])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([22, 23])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([23, 24])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([24, 25])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([25, 26])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([26, 27])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([27, 28])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([28, 29])
                if "Perşembe" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([31, 32])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([32, 33])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([33, 34])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([34, 35])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([35, 36])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([36, 37])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([37, 38])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([38, 39])
                if "Cuma" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([41, 42])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([42, 43])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([43, 44])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([44, 45])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([45, 46])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([46, 47])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([47, 48])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([48, 49])
            if course_day.startswith("Ça"):
                if course_slot.startswith("8"):
                    course_time_code = [21, 22]
                if course_slot.startswith("9"):
                    course_time_code = [22, 23]
                if course_slot.startswith("10"):
                    course_time_code = [23, 24]
                if course_slot.startswith("11"):
                    course_time_code = [24, 25]
                if course_slot.startswith("12"):
                    course_time_code = [25, 26]
                if course_slot.startswith("13"):
                    course_time_code = [26, 27]
                if course_slot.startswith("14"):
                    course_time_code = [27, 28]
                if course_slot.startswith("15"):
                    course_time_code = [28, 29]
                if "Pazartesi" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([1, 2])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([2, 3])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([3, 4])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([4, 5])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([5, 6])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([6, 7])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([7, 8])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([8, 9])
                if "Salı" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([11, 12])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([12, 13])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([13, 14])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([14, 15])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([15, 16])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([16, 17])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([17, 18])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([18, 19])
                if "Perşembe" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([31, 32])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([32, 33])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([33, 34])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([34, 35])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([35, 36])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([36, 37])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([37, 38])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([38, 39])
                if "Cuma" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([41, 42])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([42, 43])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([43, 44])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([44, 45])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([45, 46])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([46, 47])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([47, 48])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([48, 49])
            if course_day.startswith("Pe"):
                if course_slot.startswith("8"):
                    course_time_code = [31, 32]
                if course_slot.startswith("9"):
                    course_time_code = [32, 33]
                if course_slot.startswith("10"):
                    course_time_code = [33, 34]
                if course_slot.startswith("11"):
                    course_time_code = [34, 35]
                if course_slot.startswith("12"):
                    course_time_code = [35, 36]
                if course_slot.startswith("13"):
                    course_time_code = [36, 37]
                if course_slot.startswith("14"):
                    course_time_code = [37, 38]
                if course_slot.startswith("15"):
                    course_time_code = [38, 39]
                if "Pazartesi" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([1, 2])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([2, 3])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([3, 4])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([4, 5])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([5, 6])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([6, 7])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([7, 8])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([8, 9])
                if "Salı" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([11, 12])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([12, 13])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([13, 14])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([14, 15])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([15, 16])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([16, 17])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([17, 18])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([18, 19])
                if "Çarşamba" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([31, 32])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([32, 33])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([33, 34])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([34, 35])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([35, 36])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([36, 37])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([37, 38])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([38, 39])
                if "Cuma" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([41, 42])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([42, 43])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([43, 44])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([44, 45])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([45, 46])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([46, 47])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([47, 48])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([48, 49])
            if course_day.startswith("Cu"):

                if course_slot.startswith("8"):
                    course_time_code = [41, 42]
                if course_slot.startswith("9"):
                    course_time_code = [42, 43]
                if course_slot.startswith("10"):
                    course_time_code = [43, 44]
                if course_slot.startswith("11"):
                    course_time_code = [44, 45]
                if course_slot.startswith("12"):
                    course_time_code = [45, 46]
                if course_slot.startswith("13"):
                    course_time_code = [46, 47]
                if course_slot.startswith("14"):
                    course_time_code = [47, 48]
                if course_slot.startswith("15"):
                    course_time_code = [48, 49]
                if "Pazartesi" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([1, 2])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([2, 3])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([3, 4])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([4, 5])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([5, 6])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([6, 7])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([7, 8])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([8, 9])
                if "Salı" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([11, 12])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([12, 13])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([13, 14])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([14, 15])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([15, 16])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([16, 17])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([17, 18])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([18, 19])
                if "Çarşamba" in course_day:
                    if course_slot.endswith("10:29"):
                        course_time_code.extend([31, 32])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([32, 33])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([33, 34])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([34, 35])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([35, 36])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([36, 37])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([37, 38])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([38, 39])
                if "Perşembe" in course_day:

                    if course_slot.endswith("10:29"):
                        course_time_code.extend([31, 32])
                    if course_slot.endswith("11:29"):
                        course_time_code.extend([32, 33])
                    if course_slot.endswith("12:29"):
                        course_time_code.extend([33, 34])
                    if course_slot.endswith("13:29"):
                        course_time_code.extend([34, 35])
                    if course_slot.endswith("14:29"):
                        course_time_code.extend([35, 36])
                    if course_slot.endswith("15:29"):
                        course_time_code.extend([36, 37])
                    if course_slot.endswith("16:29"):
                        course_time_code.extend([37, 38])
                    if course_slot.endswith("17:29"):
                        course_time_code.extend([38, 39])
        else:

            if course_day.startswith("Pa"):
                if course_slot.startswith("8"):
                    if course_slot.endswith("9:29"):
                        course_time_code = [1]
                    if course_slot.endswith("10:29"):
                        course_time_code = [1, 2]
                    if course_slot.endswith("11:29"):
                        course_time_code = [1, 2, 3]
                if course_slot.startswith("9"):
                    if course_slot.endswith("10:29"):
                        course_time_code = [2]
                    if course_slot.endswith("11:29"):
                        course_time_code = [2, 3]
                    if course_slot.endswith("12:29"):
                        course_time_code = [2, 3, 4]
                if course_slot.startswith("10"):
                    if course_slot.endswith("11:29"):
                        course_time_code = [3]
                    if course_slot.endswith("12:29"):
                        course_time_code = [3, 4]
                    if course_slot.endswith("13:29"):
                        course_time_code = [3, 4, 5]
                if course_slot.startswith("11"):
                    if course_slot.endswith("12:29"):
                        course_time_code = [4]
                    if course_slot.endswith("13:29"):
                        course_time_code = [4, 5]
                    if course_slot.endswith("14:29"):
                        course_time_code = [4, 5, 6]
                if course_slot.startswith("12"):
                    if course_slot.endswith("13:29"):
                        course_time_code = [5]
                    if course_slot.endswith("14:29"):
                        course_time_code = [5, 6]
                    if course_slot.endswith("15:29"):
                        course_time_code = [5, 6, 7]
                if course_slot.startswith("13"):
                    if course_slot.endswith("14:29"):
                        course_time_code = [6]
                    if course_slot.endswith("15:29"):
                        course_time_code = [6, 7]
                    if course_slot.endswith("16:29"):
                        course_time_code = [6, 7, 8]
                if course_slot.startswith("14"):
                    if course_slot.endswith("15:29"):
                        course_time_code = [7]
                    if course_slot.endswith("16:29"):
                        course_time_code = [7, 8]
                    if course_slot.endswith("17:29"):
                        course_time_code = [7, 8, 9]
                if course_slot.startswith("15"):
                    if course_slot.endswith("16:29"):
                        course_time_code = [8]
                    if course_slot.endswith("17:29"):
                        course_time_code = [8, 9]

                if course_slot.startswith("16"):
                    if course_slot.endswith("17:29"):
                        course_time_code = [9]

            if course_day.startswith("Sa"):
                if course_slot.startswith("8"):
                    if course_slot.endswith("9:29"):
                        course_time_code = [11]
                    if course_slot.endswith("10:29"):
                        course_time_code = [11, 12]
                    if course_slot.endswith("11:29"):
                        course_time_code = [11, 12, 13]
                if course_slot.startswith("9"):
                    if course_slot.endswith("10:29"):
                        course_time_code = [12]
                    if course_slot.endswith("11:29"):
                        course_time_code = [12, 13]
                    if course_slot.endswith("12:29"):
                        course_time_code = [12, 13, 14]
                if course_slot.startswith("10"):
                    if course_slot.endswith("11:29"):
                        course_time_code = [13]
                    if course_slot.endswith("12:29"):
                        course_time_code = [13, 14]
                    if course_slot.endswith("13:29"):
                        course_time_code = [13, 14, 15]
                if course_slot.startswith("11"):
                    if course_slot.endswith("12:29"):
                        course_time_code = [14]
                    if course_slot.endswith("13:29"):
                        course_time_code = [14, 15]
                    if course_slot.endswith("14:29"):
                        course_time_code = [14, 15, 16]
                if course_slot.startswith("12"):
                    if course_slot.endswith("13:29"):
                        course_time_code = [15]
                    if course_slot.endswith("14:29"):
                        course_time_code = [15, 16]
                    if course_slot.endswith("15:29"):
                        course_time_code = [15, 16, 17]
                if course_slot.startswith("13"):
                    if course_slot.endswith("14:29"):
                        course_time_code = [16]
                    if course_slot.endswith("15:29"):
                        course_time_code = [16, 17]
                    if course_slot.endswith("16:29"):
                        course_time_code = [16, 17, 18]
                if course_slot.startswith("14"):
                    if course_slot.endswith("15:29"):
                        course_time_code = [17]
                    if course_slot.endswith("16:29"):
                        course_time_code = [17, 18]
                    if course_slot.endswith("17:29"):
                        course_time_code = [17, 18, 19]
                if course_slot.startswith("15"):
                    if course_slot.endswith("16:29"):
                        course_time_code = [18]
                    if course_slot.endswith("17:29"):
                        course_time_code = [18, 19]
                if course_slot.startswith("16"):
                    if course_slot.endswith("17:29"):
                        course_time_code = [19]

            if course_day.startswith("Ça"):
                if course_slot.startswith("8"):
                    if course_slot.endswith("9:29"):
                        course_time_code = [21]
                    if course_slot.endswith("10:29"):
                        course_time_code = [21, 22]
                    if course_slot.endswith("11:29"):
                        course_time_code = [21, 22, 23]
                if course_slot.startswith("9"):
                    if course_slot.endswith("10:29"):
                        course_time_code = [22]
                    if course_slot.endswith("11:29"):
                        course_time_code = [22, 23]
                    if course_slot.endswith("12:29"):
                        course_time_code = [22, 23, 24]
                if course_slot.startswith("10"):
                    if course_slot.endswith("11:29"):
                        course_time_code = [23]
                    if course_slot.endswith("12:29"):
                        course_time_code = [23, 24]
                    if course_slot.endswith("13:29"):
                        course_time_code = [23, 24, 25]
                if course_slot.startswith("11"):
                    if course_slot.endswith("12:29"):
                        course_time_code = [24]
                    if course_slot.endswith("13:29"):
                        course_time_code = [24, 25]
                    if course_slot.endswith("14:29"):
                        course_time_code = [24, 25, 26]
                if course_slot.startswith("12"):
                    if course_slot.endswith("13:29"):
                        course_time_code = [25]
                    if course_slot.endswith("14:29"):
                        course_time_code = [25, 26]
                    if course_slot.endswith("15:29"):
                        course_time_code = [25, 26, 27]
                if course_slot.startswith("13"):
                    if course_slot.endswith("14:29"):
                        course_time_code = [26]
                    if course_slot.endswith("15:29"):
                        course_time_code = [26, 27]
                    if course_slot.endswith("16:29"):
                        course_time_code = [26, 27, 28]
                if course_slot.startswith("14"):
                    if course_slot.endswith("15:29"):
                        course_time_code = [27]
                    if course_slot.endswith("16:29"):
                        course_time_code = [27, 28]
                    if course_slot.endswith("17:29"):
                        course_time_code = [27, 28, 29]
                if course_slot.startswith("15"):
                    if course_slot.endswith("16:29"):
                        course_time_code = [28]
                    if course_slot.endswith("17:29"):
                        course_time_code = [28, 29]
                if course_slot.startswith("16"):
                    if course_slot.endswith("17:29"):
                        course_time_code = [29]

            if course_day.startswith("Pe"):
                if course_slot.startswith("8"):
                    if course_slot.endswith("9:29"):
                        course_time_code = [31]
                    if course_slot.endswith("10:29"):
                        course_time_code = [31, 32]
                    if course_slot.endswith("11:29"):
                        course_time_code = [31, 32, 33]
                if course_slot.startswith("9"):
                    if course_slot.endswith("10:29"):
                        course_time_code = [32]
                    if course_slot.endswith("11:29"):
                        course_time_code = [32, 33]
                    if course_slot.endswith("12:29"):
                        course_time_code = [32, 33, 34]
                if course_slot.startswith("10"):
                    if course_slot.endswith("11:29"):
                        course_time_code = [33]
                    if course_slot.endswith("12:29"):
                        course_time_code = [33, 34]
                    if course_slot.endswith("13:29"):
                        course_time_code = [33, 34, 35]
                if course_slot.startswith("11"):
                    if course_slot.endswith("12:29"):
                        course_time_code = [34]
                    if course_slot.endswith("13:29"):
                        course_time_code = [34, 35]
                    if course_slot.endswith("14:29"):
                        course_time_code = [34, 35, 36]
                if course_slot.startswith("12"):
                    if course_slot.endswith("13:29"):
                        course_time_code = [35]
                    if course_slot.endswith("14:29"):
                        course_time_code = [35, 36]
                    if course_slot.endswith("15:29"):
                        course_time_code = [35, 36, 37]
                if course_slot.startswith("13"):
                    if course_slot.endswith("14:29"):
                        course_time_code = [36]
                    if course_slot.endswith("15:29"):
                        course_time_code = [36, 37]
                    if course_slot.endswith("16:29"):
                        course_time_code = [36, 37, 38]
                if course_slot.startswith("14"):
                    if course_slot.endswith("15:29"):
                        course_time_code = [37]
                    if course_slot.endswith("16:29"):
                        course_time_code = [37, 38]
                    if course_slot.endswith("17:29"):
                        course_time_code = [37, 38, 39]
                if course_slot.startswith("15"):
                    if course_slot.endswith("16:29"):
                        course_time_code = [38]
                    if course_slot.endswith("17:29"):
                        course_time_code = [38, 39]
                if course_slot.startswith("16"):
                    if course_slot.endswith("17:29"):
                        course_time_code = [39]

            if course_day.startswith("Cu"):
                if course_slot.startswith("8"):
                    if course_slot.endswith("9:29"):
                        course_time_code = [41]
                    if course_slot.endswith("10:29"):
                        course_time_code = [41, 42]
                    if course_slot.endswith("11:29"):
                        course_time_code = [41, 42, 43]
                if course_slot.startswith("9"):
                    if course_slot.endswith("10:29"):
                        course_time_code = [42]
                    if course_slot.endswith("11:29"):
                        course_time_code = [42, 43]
                    if course_slot.endswith("12:29"):
                        course_time_code = [42, 43, 44]
                if course_slot.startswith("10"):
                    if course_slot.endswith("11:29"):
                        course_time_code = [43]
                    if course_slot.endswith("12:29"):
                        course_time_code = [43, 44]
                    if course_slot.endswith("13:29"):
                        course_time_code = [43, 44, 45]
                if course_slot.startswith("11"):
                    if course_slot.endswith("12:29"):
                        course_time_code = [44]
                    if course_slot.endswith("13:29"):
                        course_time_code = [44, 45]
                    if course_slot.endswith("14:29"):
                        course_time_code = [44, 45, 46]
                if course_slot.startswith("12"):
                    if course_slot.endswith("13:29"):
                        course_time_code = [45]
                    if course_slot.endswith("14:29"):
                        course_time_code = [45, 46]
                    if course_slot.endswith("15:29"):
                        course_time_code = [45, 46, 47]
                if course_slot.startswith("13"):
                    if course_slot.endswith("14:29"):
                        course_time_code = [46]
                    if course_slot.endswith("15:29"):
                        course_time_code = [46, 47]
                    if course_slot.endswith("16:29"):
                        course_time_code = [46, 47, 48]
                if course_slot.startswith("14"):
                    if course_slot.endswith("15:29"):
                        course_time_code = [47]
                    if course_slot.endswith("16:29"):
                        course_time_code = [47, 48]
                    if course_slot.endswith("17:29"):
                        course_time_code = [47, 48, 49]

                    if course_slot.endswith("16:59"):
                        course_time_code = [47, 48, 49]

                if course_slot.startswith("15"):
                    if course_slot.endswith("16:29"):
                        course_time_code = [48]
                    if course_slot.endswith("17:29"):
                        course_time_code = [48, 49]
                if course_slot.startswith("16"):
                    if course_slot.endswith("17:29"):
                        course_time_code = [49]

        result = all(elem in days_available for elem in course_time_code)

        if result:
            list.append([course_cnr, course_time_code])
    list.pop(0)

    return (list)


def deneme_scheduler(course_1, course_2, course_3, course_4, course_5, course_6, course_7,days_selected):
    list_1 = deneme(course_1, days_selected)
    list_2 = deneme(course_2, days_selected)
    list_3 = deneme(course_3, days_selected)
    list_4 = deneme(course_4, days_selected)
    list_5 = deneme(course_5, days_selected)
    list_6 = deneme(course_6, days_selected)
    list_7 = deneme(course_7, days_selected)

    potential_schedules = []  # cnr'lardan olujşan liste

    for combination in itertools.product(list_1, list_2, list_3, list_4, list_5, list_6, list_7):
        comb_cnr = []
        comb_slot = []
        for element in combination:
            comb_cnr.append(element[0])
            comb_slot.append(element[1])
        flat_list_slot = [item for sublist in comb_slot for item in sublist]
        if len(flat_list_slot) == len(set(flat_list_slot)):
            potential_schedules.append(comb_cnr)

    return (potential_schedules)


