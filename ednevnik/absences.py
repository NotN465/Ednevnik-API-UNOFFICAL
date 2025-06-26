from bs4 import BeautifulSoup
import requests
def get_absences_from_class_year(html_content,session,class_year,school):
    class_id = html_content.find("div",{"class":"class-info"}).attrs['data-action-id']
    url = f'https://ocjene.skole.hr/class_action/{class_id}/absent'
    absences_request = session.get(url)
    html_content = BeautifulSoup(absences_request.content,'html.parser')
    months = html_content.find_all("div",{"aria-label":"CalendarTable"})
    absences = dict()
    for month in months:
        month_name = f"{month.attrs['data-action-id']}"
        absences[month_name] = list()
        entries = month.find_all("div",{"class":"cell has-entry"})
        for entry in entries:
            day = entry.attrs['data-attribute-day']
            number_of_absences = entry.find("div",{"class":"number-of-absents"}).text
            number_of_absences = str(number_of_absences).replace(' ','')
            number_of_absences = str(number_of_absences).replace('\n', '')
            absences[month_name].append([day,number_of_absences])
    return absences
def get_absences_from_month(html_content,session,class_year,school,month):
    try:
        return {month:get_absences_from_class_year(html_content=html_content,session=session,class_year=class_year,school=school)[month]}
    except KeyError:
        return "On the specified month there were no absences or you entered a wrong month name"