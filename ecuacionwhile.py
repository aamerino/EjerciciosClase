from urllib.request import urlopen

def get_page_3(url):
	pagina = urlopen(url)
	codigoHtml = pagina.read().decode('utf')
	pagina.close()
	return codigoHtml


def get_next_target(website):
        start_link= website.find('<a href')
        if (start_link) != -1:
                start_quote= website.find('"',start_link)
                end_quote= website.find('"',start_quote+1)
                url= website[start_quote+1:end_quote]
                page = website[end_quote+1:]
                return url 
        return start_link 


page = get_page_3('http://xkcd.com/353')

while get_next_target(page) != -1 :
        url = get_next_target(page)
        print (url)
        print (page)



