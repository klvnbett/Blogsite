# import urllib.request.json
from .models import Quotes
import urllib.request, json

QUOTE_URL ='http://quotes.stormconsultancy.co.uk/random.json'

def get_quote():
    """
    Function to get and consume http request and return a quote instance
    """

def get_quote():
    quotes_list=[]
    new_quote_url=QUOTE_URL.format()
    with urllib.request.urlopen(new_quote_url) as url:
        get_data=url.read()
        get_response = json.loads(get_data)
        id=get_response['id']
        quote=str(get_response['quote'])
        author=str(get_response['author'])
        new_list=[id, quote, author]
        quotes_list.append(new_list)
    return quotes_list[0]