from BeautifulSoup import BeautifulSoup
import requests
import urlparse
from time import gmtime, strftime

URL = 'https://egov.uscis.gov/casestatus/landing.do'
s = requests.Session()

def fetch(url, data=None):
    if data is None:
        return s.get(url).content
    else:
        return s.post(url, data=data).content

def fetch_result(number):
    soup = BeautifulSoup(fetch(URL))
    form = soup.find('form')
    fields = form.findAll('input')[1:]

    formdata = dict((field.get('name'), field.get('value')) for field in fields)

    formdata['appReceiptNum'] = number

    posturl = urlparse.urljoin(URL, form['action'])

    r = s.post(posturl, data=formdata)

    result_text = r.content
    soup1 = BeautifulSoup(result_text)

    result = soup1.find('div', {'class': 'rows text-center'})
    if result is None:
        return 'None'
    res = result.find('h1')
    return res

begin_number = 1890017759
end_number = 1890016759
file_name = 'results/' + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + '.txt'
file = open(file_name, 'w')
for n in range(begin_number, end_number, -1):
   number = 'YSC' + str(n)
   file.write(str(number) + '\t')
   file.write(str(fetch_result(number)) + '\n')
   file.flush()
file.close()
