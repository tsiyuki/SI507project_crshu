# SI final project

Chenrui Shu

[Link to this repository](https://github.com/tsiyuki/SI507project_crshu)

---

## Project Description

My project will collect the data of national parks scraped from a website and display corresponding visualized results based on users’ action on the Flask based website. 

On the homepage, the user could either search the detailed infomation of a particular park by the park name or start searching from the state. If the user choose to start from state, they will be navigated to a form, and then they can select a state name and submit the form to see a histogram indicating the number of different types of parks in that state. Then, they can select a type from that state, and a list of park name of that type in the state would be shown up. After that, the user could click the park name and the detailed park infomation would be displayed.
## How to run

1. Download the whole project
2. `cd` to the directory where ***requirements.txt*** is located
3. creat a new virtual environment, `python3 -m venv env` for python3 and `virtualenv env` for python2.
4. activate your virtual environment `source env/bin/activate`
5. insall required dependencies`pip install -r requirements.txt `
6. run `python SI507project.py runserver`
7. After finishing using the application, deactivate your virtual environment. `deactivate`

## How to use
This park would be implemented later after check in.

1. A useful instruction goes here
2. A useful second step here
3. (Optional): Markdown syntax to include an screenshot/image: ![alt text](image.jpg)

## Routes in this application
- `/` -> this is the home page
- `/stateForm` -> this route has a form for user to select state
- `/stateResult` -> this route is where the form sends the result.
- `/stateTypeResult/<state_name>/<type_name>` -> This route takes state name and type name as input and shows users a list of park name.
- `/park/<park_name>` -> this route takes input of a park name and shows users the detaild infomation of that park.

## How to run tests
1. First `cd` to the directory where ***SI507project_tests.py*** is located
2. Second run the test file `python SI507project_tests.py`


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
- parks.db

---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [ ] Project is submitted as a Github repository
- [ ] Project includes a working Flask application that runs locally on a computer
- [x] Project includes at least 1 test suite file with reasonable tests in it.
- [ ] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [ ] Includes a diagram of your database schema
- [ ] Includes EVERY file needed in order to run the project
- [ ] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [ ] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [ ] Interactions with a database that has at least 2 tables
- [ ] At least 1 relationship between 2 tables in database
- [ ] Information stored in the database is viewed or interacted with in some way

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
- [ ] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [ ] I included a summary of my project and how I thought it went **in my Canvas submission**!
