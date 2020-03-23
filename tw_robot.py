import tweepy
from datetime import datetime
from time import sleep
import msvcrt
import random

horario = []
msg = []

consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth)

def hora_atual():

	now = datetime.now()

	h = str(now.hour)
	if len(h) < 2:
		h = '0'+h

	m = str(now.minute)
	if len(m) < 2:
		m = '0'+m

	s = str(now.second)
	if len(s) < 2:
		s = '0'+s

	return h+':'+m+':'+s


def atualiza_list():
	global horario
	global msg

	horario = []
	msg = []

	arquivo = open('list.txt','r')

	for line in arquivo:
		if ' - ' in line:
			lin_str = line.split(' - ')
			horario.append(lin_str[0])
			msg.append(lin_str[1])
			#print(lin_str)

	arquivo.close()

	print('---------------- ATUALIZADO COM SUCESSO ----------------')

def use_msg(i):
	arquivo = open('list.txt', 'r')

	buff = []

	j = 0

	for line in arquivo:
		if j != i:
			buff.append(line)
		j = j+1	

	arquivo.close()

	n_arquivo = open('list.txt', 'w')
	n_arquivo.writelines(buff)
	n_arquivo.close()

def hashtags(i):
	arquivo = open('hashtags.txt', 'r')

	hashs = []

	for lines in arquivo:
		hashs.append(str('#')+lines.strip('\n'))

	arquivo.close()

	if i > len(hashs):
		leng = len(hashs)
	else:
		leng = i

	leng = len(hashs) - leng

	for j in range(leng):
		hashs.pop(random.randint(0,len(hashs)-1))

	hashs = ' '.join(hashs)

	return hashs


def send_status(m):
	txt = m+'\n\n'+hashtags(4)
	print('-------------------------------------------------------\n'+txt+'\n-------------------------------------------------------')
	api.update_status(status = txt)

atualiza_list()

while True:
	if hora_atual() in horario:
		ind = horario.index(hora_atual())

		send_status(msg[ind])
		use_msg(ind)
		atualiza_list()
		sleep(5)

	sleep(0.5)
	if msvcrt.kbhit():
		key_stroke = msvcrt.getch()
		if key_stroke == b'q':
			print('---------------- SAINDO ----------------')
			break
		if key_stroke == b'r':
			atualiza_list()