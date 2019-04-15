import os
from time import sleep

def message(title,body,params):
	os.system("DISPLAY=:0 notify-send \
		 {} '{}' '{}'".format(
		 ' '.join([' '.join((key,params[key])) for key in params]),title,'\n'.join(body)))
	# sleep(0.6)

class ViewMessage:
	link_img = 'file://'+ os.getcwd()+'/view/img/fallout.svg'
	params = {'-i':link_img, '-t': str(2000), '-u':'low'}
	def write(self, text):
		for msg in eval(text):
			message(msg[0],msg[1:],self.params)

