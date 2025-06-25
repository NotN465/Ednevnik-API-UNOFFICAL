import requests
from bs4 import BeautifulSoup

def get_current_exams(html_content):
    exams_by_month = html_content.find('div',{"class":"table-wrapper"})
    months = exams_by_month.find_all('div',{"aria-label":"ExamTable"})
    all_exams = dict()
    for exams in months:
        month = exams.attrs['data-action-id']
        all_exams[month] = []
        exams = exams.find_all('div',{"class":"row"})
        for exam in exams:
            date = exam.find('div',{"class":"cell"}).text
            if any(char in "abcdefghijklmnoprstuvz" for char in date):
                pass
            else:
                class_and_note = exam.find('div',{"class","box"})
                temp = list(class_and_note.text.split("\n"))
                temp = temp[1:-1]
                temp.insert(0,date)
                all_exams[month].append(temp)

    return all_exams

def get_exams_by_month(session,html_content,class_year,school,month):
    year_data = html_content.find_all("a", {"class": "school-data"})
    year = ''
    school_name = ''
    for data in year_data:
        year = data.find("span",{"class":"bold"}).text
        school_name = data.find("span",{"class":"school-name"}).text
        if school_name == school and class_year == year:
            break
    year_request = session.get("https://ocjene.skole.hr/class_action/7277090590/exam")
    soup =  BeautifulSoup(year_request.content,"html.parser")
    months = soup.find_all("div",{"aria-label":"ExamTable"})
    month_name = ''
    month_data = ''
    data = []
    for month_content in months:
        month_name = month_content.attrs['data-action-id']
        if month_name == month:
            month_data = month_content
            break
    for data1 in month_data.find_all('div',{'class':'row'}):
        temp = []
        date = data1.find("div",{"class":"cell"}).text
        box = data1.find("div",{"class":"box"})
        temp.append(date)
        try:
            for content in box.contents:
                if content.text != '\n':
                    temp.append(content.text)
        except AttributeError:
            pass
        data.append(temp)
    return data[1:]
def get_exams_by_class(session,html_content,class_year,school):
    class_info = html_content.find_all('div',{"class":"class-info"})
    for class_ in class_info:
        class_year_ = class_.find('span',{"class":"bold"})
        school_name_ = class_.find('span',{"class":"school-name"})
        if class_year_.text == class_year and school_name_.text == school:
            class_info = class_
            break
    url = f'https://ocjene.skole.hr/class_action/{class_info.attrs['data-action-id']}/exam'
    year_request = session.get(url)
    html_content = BeautifulSoup(year_request.content,'html.parser')
    exams_by_month = html_content.find('div', {"class": "table-wrapper"})
    months = exams_by_month.find_all('div', {"aria-label": "ExamTable"})
    all_exams = dict()
    for exams in months:
        month = exams.attrs['data-action-id']
        all_exams[month] = []
        exams = exams.find_all('div', {"class": "row"})
        for exam in exams:
            date = exam.find('div', {"class": "cell"}).text
            if any(char in "abcdefghijklmnoprstuvz" for char in date):
                pass
            else:
                class_and_note = exam.find('div', {"class", "box"})
                temp = list(class_and_note.text.split("\n"))
                temp = temp[1:-1]
                temp.insert(0, date)
                all_exams[month].append(temp)

    return all_exams