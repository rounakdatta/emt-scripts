import os

tktFiles = [f for f in os.listdir('./data/pdf')]

from parser import onlineConverter

for ticket in tktFiles:
	tktRaw = onlineConverter(ticket)