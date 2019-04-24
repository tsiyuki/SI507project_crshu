from bs4 import BeautifulSoup 
import requests, json 
import requests_cache 
from csv import writer
from matplotlib import pyplot as plt
import matplotlib
from SI507project import State, Type, Park, session
import csv


class ParkInfo:
	def __init__(self, park):
		self.name = park.name
		self.description = park.description
		self.location = park.location
		self.pysical_address = park.pysical_address
		self.state = park.state.name
		self.type = park.type.name


	def __str__(self):
		return "The park is {}".format(self.name)

	def __repr__(self):
		return "Park's name is {}".format(self.name)

	def get_info(self):
		info = {"name": self.name,
				"type":  self.type,
				"state": self.state,
				"location": self.location,
				"pysical address": self.pysical_address,
				"description": self.description}
		return info
	# return [self.name, self.description, self.location, self.pysical_address, self.state, self.type]


###### help functions ######################
def save_figure(types, state_name):
	matplotlib.use('TkAgg')

	x = []
	y = []
	i = 1
	for type in types:
		tag = "#" + str(i)
		x.append(tag)
		y.append(types[type])
		i += 1


	plt.bar(x, y, color = "blue")
	plt.xlabel("park types")
	plt.ylabel("number of parks in the state")
	plt.title("Number of parks with different type in the {}".format(state_name))
	plt.savefig('static/state.png')
	plt.close()



######### web scraping ######################

def web_scraping():

	#overal base url for both homepage and sub-pages

	BASE_URL = "https://www.nps.gov"


	with open('park_data.csv','w') as file:
		csv_writer = writer(file)
		csv_writer.writerow(['Name', 'Type', 'Description', 'Location', 'State', 'Physical_Address'])

	#initialize the cache
	requests_cache.install_cache('parks_cache', backend='sqlite', expire_after=1000)

	#homepage
	url = BASE_URL + "/index.htm" 

	data_raw = requests.get(url)
	data = data_raw.text

	soup = BeautifulSoup(data, "html.parser") 


	state_menu = soup.find("ul", attrs={"class": "dropdown-menu SearchBar-keywordSearch", "role": "menu"})
	states = state_menu.find_all("li")
	for state in states:
		state_name = state.a.text  #get the name for the state
		state_url = BASE_URL + state.a['href']
		print("Now scaping: ", state_url, "......")

		# get cached data for this state
		state_data_raw = requests.get(state_url)
		state_data = state_data_raw.text 

		state_soup = BeautifulSoup(state_data, "html.parser") 
		# print(state_soup.title)
		park_menu = state_soup.find("ul", id = "list_parks")
		parks = park_menu.find_all("li", {"class": "clearfix"})
		for park in parks:
			with open('park_data.csv','a') as file:
				csv_writer = writer(file)

				Type = park.find("div").h2.get_text()
				if not Type:
					Type = "None"
					
				Name = park.find("div").h3.a.get_text()
				if not Name:
					Name = "None"
				
				Description = park.find("div").p.get_text()
				if not Description:
					Description = "None"

				Location = park.find("div").h4.get_text()
				if not Location:
					Location = "None"

				url_links = park.find("div", {"class": "col-md-12 col-sm-12 noPadding stateListLinks"})
				basic_urls = url_links.find_all("li")
				if len(basic_urls) < 2:
					address = "None"
				else:
					basic_url = basic_urls[1].a['href']
					address_soup = BeautifulSoup(requests.get(basic_url).text, "lxml")
					address_container = address_soup.find("div", {"itemprop": "address"})
					# print(address_container)
					if not address_container:
						address = "None"
					else:
						address = address_container.find_all("span")
						# print(address)
						streetAddress = address[0].get_text()
						addressLocality = address[1].get_text()
						addressRegion = address[2].get_text()
						postalCode = address[3].get_text()
						address = " ".join([address[0].get_text(), address[1].get_text()])
					# print(address)

				csv_writer.writerow([Name, Type, Description, Location, state_name, address])



################## database population #######################

def insert_park(park_name, park_type, park_description, park_location, state_name, pysical_address):
    # first query based on human knowledge
    state = get_or_create_state(state_name)
    type = get_or_create_type(park_type)

    park = session.query(Park).filter_by(name=park_name).first()
    if park:
        return
    else:
        park = Park(name=park_name,type=type,description = park_description, location=park_location, state = state, pysical_address = pysical_address)
        session.add(park)
        session.commit()


def get_or_create_state(state_name):
    state = session.query(State).filter_by(name=state_name).first()
    if state:
        return state
    else:
        state = State(name=state_name)
        session.add(state)
        session.commit()
        return state


def get_or_create_type(type_name):
    type = session.query(Type).filter_by(name=type_name).first()
    if type:
        return type
    else:
        type = Type(name=type_name)
        session.add(type)
        session.commit()
        return type


def main_populate(dataset_filename):
    """Accepts dataset filename with expected CSV format. Opens CSV file, loads contents, closes file appropriately, and invokes above functions to populate database"""
    try:
        with open(dataset_filename, "r") as f:
        	# print("Populating Database.......")
            f.seek(0)
            reader = csv.reader(f)
            next(reader, None)
            for line in reader:
                park_name = line[0]
                park_type = line[1]
                park_description = line[2]
                park_location = line[3]
                state_name = line[4]
                pysical_address = line[5]
                insert_park(park_name, park_type, park_description, park_location, state_name, pysical_address)
    except:
        return False   


if __name__ == "__main__":
	pass









