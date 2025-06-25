import requests
from bs4 import BeautifulSoup
import re

def get_current_grades(html_content):
    grades_info = html_content.find_all("div", {'aria-label': 'NewGradesTable'})
    grades = dict()
    dates = dict()
    pattern = r'^\d+\.\d+\.$'
    for grade_info in grades_info:
        subject_title = grade_info.attrs['data-action-id']
        grades[subject_title] = []
        rows = grade_info.find_all("div",{"class":"row"})
        for row in rows:
            temp = []
            date = row.find("div", {"class": "cell"}).text
            if re.match(pattern,date):
                print(date)
                temp.append(date)
                box = row.find("div",{"class":"box"})
                for item in box:
                    if item.text != "\n":
                        temp.append(item.text)
                grades[subject_title].append(temp)
        return grades
def get_year_grades(html_content,class_year,school,session,url):
    year_data = html_content.find_all("a",{"class":"school-data"})
    classes = dict()
    for year in year_data:
        href = year.attrs['href']
        fetched_class_year = year.find('span',{'class':'bold'})
        fetched_class_year = fetched_class_year.text
        fetched_school = year.find('span',{'class':'school-name'})
        fetched_school = fetched_school.text
        classes[fetched_class_year+"-"+fetched_school] = href

        input_year = class_year+"-"+school
    try:
        course = classes[input_year]
        course_request = session.get(url+course)
        soup = BeautifulSoup(course_request.content,'html.parser')
        classes = soup.find('ul',{"class":"list"})
        classes = classes.find_all('a')
        info = dict()
        for class_ in classes:
            grades_request = session.get(url+class_['href'])
            grades = BeautifulSoup(grades_request.content,'html.parser')
            class_name = grades.find("div",{"class":"section-menu-title"})
            class_name = class_name.find('span').text
            grades = grades.find('div',{"aria-label":"NotesTable"})
            date_grade_note = grades.find_all('div',{"class":"row"})
            info[class_name] = list()
            for temp in date_grade_note:
                date = temp.find('div',{"class":"cell"}).attrs
                info_list = []
                try:
                    date = date['data-date']
                    info_list.append(date)
                except:
                    pass
                try:
                    grade_note = temp.find_all('div',{"class":"cell"})
                    grade_note = temp.find('div',{'class':'box'})
                    grade_note = grade_note.find_all('span')
                    for x in grade_note:
                        info_list.append(x.text)
                except:
                    pass
                if info_list == [] or info_list == ['Ocjena', 'Bilješka']:
                    pass
                else:
                    info[class_name].append(info_list)
        return info


    except KeyError:
        return "You gave a wrong input or the given class doesn't exist."


