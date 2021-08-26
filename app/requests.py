from .models import Quotes
import urllib.request, json

#Get the url
QUOTE_URL ='http://quotes.stormconsultancy.co.uk/random.json'


def get_quote():
    quotes_list=[]
    new_quote_url=QUOTE_URL.format()
    with urllib.request.urlopen(new_quote_url) as url:
        get_data=url.read()
        get_responce = json.loads(get_data)
        id=get_responce['id']
        quote=str(get_responce['quote'])
        author=str(get_responce['author'])
        new_list=[id, quote, author]
        quotes_list.append(new_list)
    return quotes_list[0]
