from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')

def index():
	return "Hello World"

def load_arbitr_data(personal_tax_number):
	
	url = 'http://kad.arbitr.ru/Kad/SearchInstances'
	headers = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
			'ASP.NET_SessionId': 'msc5wjtvgeo20ktuyk0quavc', 
			'_ym_uid': '1476092108930033681', 
			'CUID': 'e41e0c8e-49fa-4e03-9bb7-02d494097b63:+/mH1qCuI2qgqQBEFZyrPw==',
			'__utma': '14300007.782338541.1476092049.1476092049.1476195428.2',
			'__utmc': '14300007',
			'__utmz': '14300007.1476092049.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
			'KadLVCards': '%d0%9040-1849%2f2013~%d0%9040-14909%2f2015~%d0%9082-13919%2f2016~%d0%9012-49036%2f2015~%d0%9012-15085%2f2016',
			'__utmt': '1',		
			'__utma': '228081543.1963383588.1476091771.1476431081.1476367211.9',
			'__utmb': '228081543.9.10.1476367211',
			'__utmc': '228081543',
			'__utmz': '228081543.1476431081.8.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)'
					}
	params = {
			
			'Page': 1,
			'Count': 25,
			'Courts': [],
			'DateFrom': '',
			'DateTo': '',
			'Sides': [{'Name': personal_tax_number, 'Type': -1, 'ExactMatch': False}],
			'Judges': [],
			'CaseNumbers': [],
			'WithVKSInstances': False
						}

	request = requests.post(url, headers = headers, data = params)

	with open('prsr.txt', 'a', encoding='utf-8') as prsr:
		prsr.write("{}\n".format(request.text))
		prsr.close()

	return request.text


if __name__ == '__main__':
	app.run(port=5010, debug=True)
	print('!', load_arbitr_data('3316018105'))