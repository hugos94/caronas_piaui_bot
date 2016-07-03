# -*- coding: UTF-8 -*-
import re
import os
import urllib.request, urllib.error, urllib.parse

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

#Grava o id de todo chat iniciado com o bot
def save_id(chat_id):
	f = open("chat_ids", "r+")
	if str(chat_id) not in f.read():
		f.write(str(chat_id)+"\n")
		f.close()
	else:
		f.close()

#Retorna as caronas disponíveis no momento
def get_caronas():
	return 'nenhuma carona está disponível no momento! ' +(u'\U0001f615')

#Insere uma nova carona
def set_new_carona():
	return 'você adicionou uma nova carona!'
