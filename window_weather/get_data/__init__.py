from get_data import get_data 


def sfg():
	url = 'https://www.gismeteo.ru/weather-miass-4566/now/'
	return get_data.SoupForGis(url)
