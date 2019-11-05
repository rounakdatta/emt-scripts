from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

import re

def extractPdf(pdfname):

    # initial essentials
    rsrcmgr = PDFResourceManager()
    sio = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # extract text
    f = open(pdfname, 'rb')
    for page in PDFPage.get_pages(f):
        interpreter.process_page(page)
    f.close()

    text = sio.getvalue()
    device.close()
    sio.close()

    text = text.replace(u'\xa0', u' ').replace(u'\xad', u'-')
    return text.split(u'\x0c')[0]

def processText(pdfName):
    rawText = extractPdf(pdfName)
    dateOfBooking = re.findall(r'Booking Date:(.+?)\|', rawText)[0]
    timeOfBooking = re.findall(r'Booking Time:(.+?)H', rawText)[0]
    travelRouteFrom, travelRouteTo = re.findall(r'Your flight ticket for (.+?)is confirm', rawText)[0].split("-")
    flightTimingData = re.findall(r'further communication with us.(.+?)Passengers', rawText)[0]
    flightNumber = re.findall(r'(.+?)' + travelRouteFrom, flightTimingData)[0]
    fromAirportDetails = re.findall(travelRouteFrom + r'(.+?)' + travelRouteTo, flightTimingData)[0]
    toAirportDetails = re.findall(travelRouteTo + r'(.+?)$', flightTimingData)[0]
    boardTiming = re.findall(r'(.+?)(Mon|Tue|Wed|Thu|Fri|Sat|Sun)', fromAirportDetails)[0][0]
    arrivalTiming = re.findall(r'(.+?)(Mon|Tue|Wed|Thu|Fri|Sat|Sun)', toAirportDetails)[0][0]

    dateOfBoarding = re.findall(r'(Mon|Tue|Wed|Thu|Fri|Sat|Sun)(.+?)Terminal', fromAirportDetails)[0][1][1:]
    dateOfArrival = re.findall(r'(Mon|Tue|Wed|Thu|Fri|Sat|Sun)(.+?)Terminal', toAirportDetails)[0][1][1:]

    passengerData = re.findall(r'Passengers -(.+?)Flight Inclusion', rawText)[0]
    passengerName = re.findall(r'Seat No(.+?)(Confirm|Not Confirmed)', rawText)[0][0]

    flightCost = re.findall(r'00Total(.+?)Cancellation Charges', rawText)[0]

    print(dateOfBooking)
    print(timeOfBooking)
    print(travelRouteFrom)
    print(travelRouteTo)
    # print(flightTimingData)
    print(flightNumber)
    # print(fromAirportDetails)
    # print(toAirportDetails)
    print(boardTiming)
    print(arrivalTiming)
    print(dateOfBoarding)
    print(dateOfArrival)

    # print(passengerData)
    print(passengerName)
    print(flightCost)
