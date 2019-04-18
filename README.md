# SI507 final project

Chenrui Shu

[Link to this repository](https://github.com/tsiyuki/SI507project_crshu)

---

## Project Description

My project will collect the data of national parks scraped from a website [Link to the website](https://www.nps.gov/index.htm.) and display corresponding visualized results based on users’ action on the Flask based website. 

On the homepage, the user could either search the detailed infomation of a particular park by the park name or start searching from the state. If the user choose to start from state, they will be navigated to a form, and then they can select a state name and submit the form to see a histogram indicating the number of different types of parks in that state. Then, they can select a type from that state, and a list of park name of that type in the state would be shown up. After that, the user could click the park name and the detailed park infomation would be displayed.
## How to run

1. Download the whole project
2. `cd` to the directory where ***requirements.txt*** is located
3. creat a new virtual environment, `python3 -m venv env` for python3 and `virtualenv env` for python2.
4. activate your virtual environment `source env/bin/activate`
5. insall required dependencies`pip install -r requirements.txt `
6. Before running the main program, make sure to `conda install python.exe`, then run `pythonw SI507project.py runserver`.
7. After finishing using the application, deactivate your virtual environment. `deactivate`

## How to use
- First, we would see the home page which is shown in the screenshot below. There are three parts in this homepage. 
	- The first part shows the total number of parks stored in the database, i.e. the total number is 489 in this case. 
	- The second part allows the user to enter a park name ,and after the user clicks the `submit` button, the application would return a corresponding infomation regarding that park name. 
	- The third part will navigate the user to the state selection form after the user click `Go to the state selection form` link.

![homepage](https://github.com/tsiyuki/SI507project_crshu/blob/master/screenshots/homepage.png)

- For the second part of the homepage, if the user entered an invalid park name which is not stored in the database, an error message page would show up. The screenshot is displayed below. Also in the bottom of the page, a link is provided to return to the home page.

![wrong_name](https://github.com/tsiyuki/SI507project_crshu/blob/master/screenshots/wrong_park_name.png)

- For the second part of the homepage, if the user entered an valid park name which exists in the database, then an page with the detailed infomation about that park would show up. The screenshot is displayed below. Also in the bottom of the page, a link is provided to return to the home page.

![correct_name](https://github.com/tsiyuki/SI507project_crshu/blob/master/screenshots/park_info.png)

- For the third part of the homepage, if the user click the `Go to the state selection form` link, the user would be naviageted to the state selection form shown below in the screentshot. The user are able to select the state from the drop down list and click the `submit` botton. The drop down list is shown in the second screenshot below. Also in the bottom of the page, a link is provided to return to the home page.

![state_form](https://github.com/tsiyuki/SI507project_crshu/blob/master/screenshots/state_form.png)

![state_form](https://github.com/tsiyuki/SI507project_crshu/blob/master/screenshots/drop_down_list.png)

- After the user click the `submit` botton, the user would see a histogram showing the number of different types of parks in that state. Meanwhile, users could click the type name to see the park list. Moreover, users could click `Go to the state selection form` and return to the state selection form. Also in the bottom of the page, a link is provided to return to the home page. 

  A screenshot is given below to show the result when the user choose the Washington state. In the screentshot, we could know that there are 1 park in type National Historical Reserve, 2 parks in type National Historical Park, 1 park in type National Recreation Area, 3 parks in type National Park, 1 park in type National Historic Site and 1 park in type Affiliated Area.

![state_type_result](https://github.com/tsiyuki/SI507project_crshu/blob/master/screenshots/state_result2.png)

- After the user click the type name, a list of park name would display. The user is able to click the park name to see the detaild infomation of that park. Also in the bottom of the page, a link is provided to return to the home page. The screentshot is shown below when the user click the National Park in the Washington state. We could see that there are three parks with name Mount Rainier, North Cascades and Olympic. 

![park_result](https://github.com/tsiyuki/SI507project_crshu/blob/master/screenshots/state_type_result.png)

- After the user click the park name, a detailed infomation page would show up. Also in the bottom of the page, a link is provided to return to the home page. The screentshot is shown below when the user click the Mount Rainier in the park list.

![park_info2](https://github.com/tsiyuki/SI507project_crshu/blob/master/screenshots/park_info2.png)

Note: No need to type a word in the url during the procedure in using the application.
## Routes in this application
- `/` -> this is the home page
- `/stateForm` -> this route has a form for user to select state
- `/stateResult` -> this route is where the form sends the result.
- `/stateTypeResult/<state_name>/<type_name>` -> This route takes state name and type name as input and shows users a list of park name.
- `/park/<park_name>` -> this route takes input of a park name and shows users the detaild infomation of that park.

## How to run tests
1. First `cd` to the directory where ***SI507project_tests.py*** is located
2. Second run the test file `pythonw SI507project_tests.py`


## In this repository:
- static
  - state.png
- templates
  - index.html
  - parkInfo.html
  - stateForm.html
  - stateResult.html
  - stateTypeResult.html
- SI507project.py
- SI507project_tools.py
- SI507project_tests.py
- README.md
- sample_parks.db
- SI507project_db_schema.png
- requirements.txt 

---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [x] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [x] Project includes at least 1 test suite file with reasonable tests in it.
- [x] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [x] Use of a new module
- [x] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [x] At least one form in your Flask application
- [x] Templating in your Flask application
- [x] Inclusion of JavaScript files in the application
- [x] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [x] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [ ] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [x] Caching of data you continually retrieve from the internet in some way

### Submission
- [x] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [ ] I included a summary of my project and how I thought it went **in my Canvas submission**!
