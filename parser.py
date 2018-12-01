from extractPdf import extractPdf

# both online and offline converters are in place
# however online one gives better parsed results

def offlineConverter(ticketName):

	exContent = extractPdf(ticketName + '.pdf')
	return exContent

def onlineConverter(ticketName):

	import convertapi
	
	convertapi.api_secret = 'sWeEtApIkEy'
	convertapi.convert('txt', {
	    'File': './data/pdf/' + ticketName
	}, from_format = 'pdf').save_files('./data/txt/')
	
	exContent = [line.rstrip('\n') for line in open('./data/txt/' + ticketName[:-4] + '.txt')]

	return exContent