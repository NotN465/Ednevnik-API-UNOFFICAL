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
def get_personal_data(html_content):
    student_data = html_content.find_all('div',{"class":"l-two-columns"})
    personal_data =dict()
    for student in student_data:
        column_data = student.find_all('span',{"class":"column"})
        temp = []
        for column in column_data:
            column_text = str(column.text).strip().replace('\n','')
            temp.append(column_text)
        personal_data[temp[0]] = temp[1]
    return personal_data
def get_notes_tab(html_content):
    notes_data = html_content.find('div',{"class":"content"})
    titles = notes_data.find_all('div', {"class": "title"})
    notes = notes_data.find_all('div', {"class": "section-text"})
    notes_data = dict()
    for title,note in zip(titles,notes):
        title = str(title.text).replace('\n','').strip()
        note = str(note.text).replace('\n','').strip()
        notes_data[title] = note
    return notes_data


