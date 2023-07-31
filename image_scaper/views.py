from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen 
import logging
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def home_page(request):
    logging.basicConfig(filename="image_scraper.log" , level=logging.INFO)
    if request.method == 'GET':
        try:
            return render(request,"search.html")
        except:
            logging.info("no home page")
        

@api_view(['GET','POST'])
def image_scrap(request):
    if request.method == 'POST':
        try:
            searchString = request.POST.get('content').replace(" ","")
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
            response=requests.get(f"https://www.google.com/search?q={searchString}&tbm=isch&sxsrf=AB5stBjOz848SwobIPpU16I8wOR9Prswmg:1690653907293&source=lnms&sa=X&ved=2ahUKEwjg-NPMwLSAAxW_avUHHewZDUYQ_AUoA3oECAIQBQ&biw=1366&bih=643&dpr=1")
            soap=bs(response.content,"html.parser")
            images_tags=soap.find_all("img")
            scr=[]
            for i in images_tags:
                try:
                    image_url=i["src"]
                    link=requests.get(image_url)
                    scr.append(image_url)
                    context = {
                        "searchString":searchString,
                        'scr': scr,
                    }
                except:
                    logging.info("not valid link")
            return render(request, 'result.html',context)     
        except:
            logging.info("error choice")   
  
        
            