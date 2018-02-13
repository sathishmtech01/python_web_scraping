import requests
import bs4
import re

# link -http://cs224d.stanford.edu/syllabus.html (2016 syallabus)
#http://web.stanford.edu/class/cs224n/syllabus.html
url = "http://cs224d.stanford.edu/syllabus.html"

# convert to beautifulsoup object
soup = bs4.BeautifulSoup(requests.get(url).text)
#print(soup.find_all("a",href=True))

# Extracting all the a href
urls = []
for a in soup.find_all("a",href=True):
    urls = urls +[a['href']]


# adding "http://cs224d.stanford.edu" to string which are not having
for i in range(0,len(urls)):
    if re.match('(htt*)',urls[i]) == None:
        urls[i] = "http://cs224d.stanford.edu/"+urls[i]
#urls =['http://cs224d.stanford.edu/papers/neural_machine.pdf', 'http://cs224d.stanford.edu/lectures/CS224d-Lecture15.pdf', 'http://cs.stanford.edu/~quocle/', 'http://cs224d.stanford.edu/papers/seq2seq.pdf', 'http://cs224d.stanford.edu/papers/nmt.pdf', 'http://cs224d.stanford.edu/papers/ancm.pdf', 'http://cs224d.stanford.edu/papers/npil.pdf', 'http://cs224d.stanford.edu/lectures/CS224d-Lecture16.pdf', 'http://arxiv.org/abs/1506.07285', 'http://cs224d.stanford.edu/lectures/CS224d-Lecture17.pdf']
# downloading the data
for url in urls:

    # finding pdf and zip file name
    if re.match("(.*pdf|.*zip)",url) !=None:

        # extracting the file name
        file_name = url.split('/')[-1:][0]
        with open(file_name,"wb") as f:
            # saving the file
            f.write(requests.get(url).content)
