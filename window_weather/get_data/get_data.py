
import requests
from bs4 import BeautifulSoup as BS
# import os
import time

useragent = {"User-Agent":
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)'}
def get_html(url,stream=False):
	if stream: return requests.get(url, headers = useragent,stream=stream)
	return requests.get(url, headers = useragent).text

class SoupForGis:
	def __init__(self,url):
		self.link_fallout = './view/img/fallout.svg'
		self._soup = BS(get_html(url), 'lxml').find('div',{'class':'main'})
		soup = self._soup.find('div',class_='forecast_wrap horizontal')
		self.wind = soup.find('div',{'class':"nowinfo__measure"}).text.replace(' ','').replace('\n',' ')
		self.param = [tag.text.strip()
			for tag in soup.find_all('div', {'class':"nowinfo__value"})]
		self.pressure = soup.find('div',{'class':"nowinfo__value"}).text
		self.temperature = [t.text.strip() 
			for t in soup.find_all('span', class_="unit unit_temperature_c") ]
		self.fallout = soup.find('span', {'class':"tip _top _center"}).text
		self.now_astro = sorted([tag.text 
			for tag in soup.find_all('div',{'class',"nowastro__time"})]
									,key=lambda i: int(i.split(':')[0]))
		
		self.img_weather = str(self._soup.find('div', class_="img"))
		self.save_link()
	def weather_data(self):
		t = 'Сейчас температура '+ " по ощущению ".join(self.temperature)
		v = 'Ветер '+ self.param[0]+self.wind
		p = 'Давление ' + self.param[3] + ' мм.рт.столба'
		return t,v,p 
	def astro_data(self):
		return ( time.strftime("%A %d %B %Y"),
				'Восход '+ self.now_astro[0],
				'Закат '+self.now_astro[1] )
	def save_link(self):
		first_row = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
		with open(self.link_fallout, 'w') as f:
			f.write(first_row+self.img_weather)
	def __str__(self):
		return "{},{}".format(self.weather_data(),self.astro_data())
def main():
	pass
	# url = 'https://www.gismeteo.ru/weather-miass-4566/now/'
	# temp = SoupForGis(url)


if __name__ == '__main__':
	main()