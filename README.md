# What is this?
This is an E-dnevnik Unofficial API/Scraper that gets some information about your E-dnevnik account.<br/>
You must have an AAI@EduHr account to access your E-dnevnik account.<br/>
This is useful mainly for people in primary schools and high schools.
# How to use?
To start using the API/Scraper firstly you need to import the ednevnik package with this line:
`import ednevnik`<br/>
After that you need to provide your password and AAI@EduHr email with this line:<br/>
`ednevnik_object = ednevnik.Ednevnik(username="YOUR_EMAIL",password="YOUR_PASSWORD")`<br/>
YOUR_EMAIL - your AAI@EduHr email<br/>
YOUR_PASSWORD - your AAI@EduHr password
# Basic functions
`def get_year_grades(class_year,school)`<br/>
Returns all the grades from the school and class year specified in the following format<br/>
`dict('MONTH NAME':list(list(DATE,CLASS,NOTE)))`<br/><br/>
`def get_exams_by_month(class_year,school,month):`<br/>
Returns all the exams from the school, class year and month specified(by name, not by number) in the following format<br/>
`list(list(DATE,CLASS,EXAM_NOTE))`<br/><br/>
`def get_class_years()`<br/>
Returns all the class years followed by the year followed by the school in the following format<br/>
`list(list(CLASS_YEAR,YEAR,SCHOOL_NAME))`




