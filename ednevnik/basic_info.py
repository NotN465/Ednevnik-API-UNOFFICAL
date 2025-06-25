import requests
from bs4 import BeautifulSoup

def get_class_years(html_content):
    class_years_info = html_content.find("div",{"class":"classes"})
    data = []
    for class_year_ in class_years_info:
        try:
            class_ = class_year_.find("span",{"class":"bold"}).text
            school_year = class_year_.find("span",{"class":"class-schoolyear"}).text
            school_name = class_year_.find("span",{"class":"school-name"}).text
            grade = class_year_.find("span",{"class":"bold green"}).text
            grade = str(grade).replace(" ","")
            grade = grade.replace("\n", "")
            data.append([class_,school_year,school_name,grade])
        except:
            pass
    return data
