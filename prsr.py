import requests

def load_arbitr_data(personal_tax_number):
    url = 'http://kad.arbitr.ru/Kad/SearchInstances'
    request = requests.post(
    	url,
    	cookies={
    		'CUID': '6c8dd63c-074e-4b21-b2e9-b5f04c6da465:EdLX4zH840EwsR7qT4foNw==',
    	},
    	params={
			'CaseNumbers':[],
			'Count': 25,
			'Courts': [],
			'DateFrom': None,
			'DateTo': None,
			'Judges': [],
			'Page':1,
    		'Sides': [{
    			'Name': personal_tax_number,
    			'Type': -1,
    			'ExactMatch': False,
    		}]
    	}
	)
    return request.text

if __name__ == '__main__':

	load_arbitr_data(3316018105)


# for inn in load_inn_from_file():
# 	raw_response = load_arbitr_data(inn)

# data = [
# 	{
# 	'INN': '',

# 	}
# ]