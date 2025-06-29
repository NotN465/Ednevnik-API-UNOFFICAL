from .grades import get_current_grades,get_year_grades
from .exams import get_current_exams,get_exams_by_month,get_exams_by_class
from .basic_info import get_class_years, get_personal_data,get_notes_tab
from .absences import get_absences_from_class_year,get_absences_from_month
import requests
from bs4 import BeautifulSoup


class Ednevnik():
    def __init__(self,username,password):
        self.url = "https://ocjene.skole.hr/"
        self.session = requests.Session()
        response = self.session.get(self.url + "login")
        soup = BeautifulSoup(response.text, 'html.parser')
        value = soup.find('input', {'name': 'csrf_token'})['value']

        payload = {'username': username,
                   'password': password,
                   'csrf_token': value}
        response = self.session.post(self.url + "login", data=payload)
        html = self.session.get(self.url + "grade/all")
    def get_current_grades(self): # Gets the grades from the current year in the following format: CLASS:[[DATE,GRADE_NOTE,FIELD,GRADE]]
        html = self.session.get(self.url + "grade/all")
        soup = BeautifulSoup(html.content, "html.parser")
        return get_current_grades(html_content=soup)
    def get_year_grades(self,class_year,school): # Gets the grades from the selected year, has 2 parameters, class_year - year of the class followed by its letter, school
        html = self.session.get(self.url + "class")
        soup = BeautifulSoup(html.content, "html.parser")
        return get_year_grades(html_content=soup,class_year=class_year,school=school,session=self.session,url=self.url)
    def get_current_exams(self): # Gets the exams from the current year, has 2 parameters, class_year - year of the class followed by its letter, school
        html = self.session.get(self.url + "exam")
        soup = BeautifulSoup(html.content, "html.parser")
        return get_current_exams(html_content=soup)
    def get_exams_by_month(self,class_year,school,month): # Gets the exams of a specified year and school in a month
        html = self.session.get(self.url + "class")
        soup = BeautifulSoup(html.content,"html.parser")
        return get_exams_by_month(session=self.session,html_content=soup,class_year=class_year,school=school,month=month)
    def get_exams_by_class(self,class_year,school): # Gets all the exams of a specified class year and school
        html = self.session.get(self.url + "class")
        soup = BeautifulSoup(html.content,"html.parser")
        return get_exams_by_class(session=self.session,html_content=soup,class_year=class_year,school=school)
    def get_class_years(self):
        html = self.session.get(self.url+"class")
        soup = BeautifulSoup(html.content,"html.parser")
        return get_class_years(html_content=soup)
    def get_absences_from_class_year(self,class_year,school): # Gets all the absences of a specified class year and school, returns the following format: dict(MONTH:[[DAY,NUMBER_OF_ABSENCES]])
        html = self.session.get(self.url + "class")
        soup = BeautifulSoup(html.content, "html.parser")
        return get_absences_from_class_year(html_content=soup,session=self.session,class_year=class_year,school=school)
    def get_absences_from_month1(self,class_year,school,month): # Gets all the absences of a specified month, returns the following format: dict(MONTH:[[DAY,NUMBER_OF_ABSENCES]])
        html = self.session.get(self.url + "class")
        soup = BeautifulSoup(html.content, "html.parser")
        return get_absences_from_month(html_content=soup,session=self.session,class_year=class_year,school=school,month=month)
    def get_personal_data(self):
        html = self.session.get(self.url + "personal_data")
        soup = BeautifulSoup(html.content, "html.parser")
        return get_personal_data(html_content=soup)
    def get_personal_data(self):
        html = self.session.get(self.url + "notes")
        soup = BeautifulSoup(html.content, "html.parser")
        return get_notes_tab(html_content=soup)
__all__ = ['Ednevnik']