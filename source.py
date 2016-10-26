from requests import session
from bs4 import BeautifulSoup
import re
import datetime
import socket
import cookielib
import sys
import smtplib
import time
import urllib2
from getpass import getpass

Remote_Server = "www.google.com"

def is_connected():
    try:
        # set if we can resolve the host name
        host = socket.gethostbyname(Remote_Server)
        """connect to the host - tells us if the host is actually reachable"""
        s = socket.create_connection((host,80), 2)
        return True
    except:
        pass
    return False


def sendsms(message):
    username = "your way2sms username here"
    passwd = "your way2sms password here"
    number = "mobile no."
    #Logging into the SMS Site
    url = 'http://site24.way2sms.com/Login1.action?'
    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

    #For Cookies:
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    # Adding Header detail:
    opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]

    try:
       usock = opener.open(url, data)
    except IOError:
       return False

    jession_id = str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]

    try:
       sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
       return False
    return True
# end of  sendsms() method

def scrap():
    payload = {
        'TB1_ClientState':'{"ActiveTabIndex":0,"TabEnabledState":[true,true,true],"TabWasLoadedOnceState":[true,false,false]}',
        '__EVENTTARGET':'',
        '__EVENTARGUMENT':'',
        '__VIEWSTATE':'cb5o9GSlDuqYuTiu2iXY9JNCivMGezGstSP5M0DyR5cHMZ37oOCemmSKa/fGRbTm6H5SCy8mAsNRV4eRVqU1epRXusu73+fu0pahsoe2RIHRcoYMrC6CuCPzz2WtpJPGlS7merhmHYTJ8PLkHiPV2hzNFRBLeaPEKQpVQgK99LHtZ+VwC1mfV4rTuTqRqPXxZXcZom+/IxbYYDGzIiwBERkEgzbYaQ02KLJ/HVq9606iGDfqMSjYeYFrzuhBB0zAmVLPDf/kq9MBuyGmm7Fq73Saf3x8BZo3NW79V3Po9aKremrRGR3a3J46VXmcBZXIR0DvLlZfsEpIyvBRnqwzNXkWfSJqKzJbsKrtqMFDXZ896juUuYrqo22V8WVaF1FNbHELFDjtGzpsySNbcBAOnRSJEJVkVqUNwH00N7HIjN5cgNNqf/Mz4fKFchtOLRD68tDAYLvq7sbFcju8nygcvcW7QaTNTnbWtZwayrC8ITXM2eXxCC+WlrICHqBTdxo62amE41tF/+F1zsMaVgTAPVLwnDIB0ombO1sQszo4oF6p/Qr/cxomMUOrRFO4WR5M0mWq2a9pIsFvvkoygXPDkSmGALGNXzTOWB8xXzbc5rcOarpYT2imGoO89wpRxMUME1tK9k77BqEzTtLDxslya9ohYZPqtMaXXLhOpEeJJtOVaZIy7UkX2/HqQVg/T9rmTqHwC4jYP6ICAO98bplWFN/8f8EKOp1nWZB6Wze42PXhqUHpCy6nDikkwyx9rXcTxZ5l2joXMNGqKy3Sckqu+BjYCHC+PboECBMnksV9DHwYh5Mm',
        '__EVENTVALIDATION':'uX8YsgjPan0LQ6dDTyZ/q2hXTM6Jk3KZVEknfv98cdymIjXo6yynDFfV+c/NxGAds2Wf63sBUyQA9SLOSf6M9PKClEqzRDFw6o2QPU+4uxMqbuQQrQWOS2fsfEW0W/srD6inQMPpKMf9HxJQjC6boTWMqpvjDJyHMxN4A0bY6V9AutOWYOSY/8FSZWOJEJ2lRljEuTSvE4dtJODpZHe9lAcH4r4GmkPf5hEDJNN4rT0Bs6XMOQrzRyAAOeeqLGK5l4YZs8AMp2dJcizAAI/45QqgOL8P0g8s3VFAcXW4KwcUUXr487YRONzI7W0A8RlFvnSO3UrBSmdZ6voT1s0Lkk+sFY6gFl2OZ54MJNniSCROedb+5FBkm8uphXxNaIjGoSnwZvPX1thN6hIdEa8diuquz+PvPDxz8kaoHJ3dqFNjaQ/AzVHN78TqNJthBt/O6VaXPAA67csmA6RaBL/7bNlJLXvxlDGkVyXNvK/StDzqc5S3',
        'TB1$TabPanel1$txt_user_name': '2016******',
        'TB1$TabPanel1$txt_password': '6******',
        'TB1$TabPanel1$btn_log':'Login',
        'TB1$tbpanel2$F_drp_college':1,
        'TB1$tbpanel2$tb_emp_id':'',
        'TB1$tbpanel2$tb_emp_password':'',
        'TB1$TabPanel2$txtusernameparent':'',
        'TB1$TabPanel2$txtPasswordParent':''
    }

    book = list()
    date = list()

    with session() as c:
        c.post('http://erp.sangamuniversity.ac.in/Default1.aspx', data=payload)
        response = c.get('http://erp.sangamuniversity.ac.in/Student/Student_Home.aspx')
        page = response.text.encode('utf-8')
        soup = BeautifulSoup(page, 'html.parser')

        elm = soup.find_all('tr')
        for index, elm in enumerate(soup.find_all("span", id=re.compile("^ContentPlaceHolder1_grd_reminder_Label"))):
            if index in (0,2,3,5,6,8,9,11):
                if index in (0,3,6,9):
                    book.append(elm.get_text())
                else:
                    date.append(elm.get_text())

    # now we have all books name in book list and all the dates text in date list
    # now comparing date of books with today's date

    today = datetime.datetime.now().strftime ("%Y%m%d")

    for i,val in enumerate(date):
        d = date[i] = datetime.datetime.strptime (val,"%d-%b-%Y").strftime ("%Y%m%d")
        today = datetime.datetime.strptime(today,"%Y%m%d")
        d = datetime.datetime.strptime(d,"%Y%m%d")
        diff = abs((today - d).days)
        if diff < 5:
            books =""
            for i,val in enumerate(book):
                books = books + str(val) + " - "
            message = "Library - " + books + " on " + str(d)
            loop(message)
            break



def loop(message):
    while 1:
        if is_connected() == False:      # no internet connection
            time.sleep(45)
            continue
        elif is_connected() == True:
            # sending sms
            if sendsms(message) == False:
                time.sleep(45)
                continue
            else:
                break

if __name__ == '__main__':
    scrap()
