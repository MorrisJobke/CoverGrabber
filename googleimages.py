#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import subprocess
import simplejson
import mimetypes
import os
import shutil

class ImageSearch:
	def __init__(self, folder = '/tmp/CoverGrabber'):
		self.folder = folder
		if os.path.exists(self.folder):
			shutil.rmtree(self.folder)
		os.mkdir(self.folder)
		
	def search(self, search):
		query = urllib.urlencode({'q' : search})
		url = 'http://ajax.googleapis.com/ajax/services/search/' + \
			'images?v=1.0&%s'%(query)
		searchResults = urllib.urlopen(url)
		json = simplejson.loads(searchResults.read())
		results = json['responseData']['results']

		filenameRoot = os.path.join(
			self.folder,
			'-'.join(search)
		)
		f = []
		c = 1
		for i in results:
			print i['url']
			filename = filenameRoot + '-%i.jpg'%c
			urllib.urlretrieve(i['url'], filename)
			mime = subprocess.Popen(
				'file -i %s'%filename, 
				shell=True,
				stdout=subprocess.PIPE
				).communicate()[0]
			mime = mime.split()[1][:-1]
			if not mime == 'image/jpeg':
				os.remove(filename)
			else:
				c += 1
				f.append(filename)
		return f



i = ImageSearch()
print i.search(['Equilibrium', 'Rekreatur', '2010'])
