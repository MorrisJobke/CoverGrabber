#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) Morris Jobke 2010 <morris.jobke@googlemail.com>
# 
# CoverGrabber is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# CoverGrabber is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import gtk
import sys
import imagesearch
import foldercheck

import pprint

musicDir = '~/Daten/Musik/Archiv'

class CoverGrabber:
	def __init__(self, images):
		self.images = images
		gladeFile = os.path.join(
			sys.path[0],
			'dialog.glade'
		)
		self.ui = gtk.Builder()	
		self.ui.add_from_file(gladeFile)	
		self.ui.connect_signals({
			'on_coverGrabberDialog_destroy': 		self.quit,
		})
		
		self.window = self.ui.get_object('coverGrabberDialog')	
		self.albumView = self.ui.get_object('albumView')
		self.folderName = self.ui.get_object('folderName')
		self.albumList = gtk.ListStore(str, gtk.gdk.Pixbuf)
		
		b = ['/tmp/CoverGrabber/Equilibrium-Rekreatur-2010-1.jpg', '/tmp/CoverGrabber/Equilibrium-Rekreatur-2010-2.jpg', '/tmp/CoverGrabber/Equilibrium-Rekreatur-2010-3.jpg', '/tmp/CoverGrabber/Equilibrium-Rekreatur-2010-4.jpg']
		for i in self.images:
			for j in self.images[i]:
				for k in self.images[i][j]:
					a = gtk.gdk.pixbuf_new_from_file(k)
					self.albumList.append([k, a])
		
		#self.albumView.set_text_column(0)
		self.albumView.set_pixbuf_column(1)
		self.albumView.set_model(self.albumList)	
		
		self.folderName.set_text('Grüße')
		
	def a(self, w):
		print 'asd'
		
	def main(self):
		self.window.show()
		gtk.main()
		
	def quit(self, widget):
		'''
			close window 
		'''
		gtk.main_quit()

if __name__ == '__main__':			
	musicDir = os.path.expanduser(musicDir)
	f = foldercheck.FolderCheck(musicDir, False)
	music = f.read()
	isearch = imagesearch.ImageSearch()
	for i in music:
		for j in music[i]:
			s = []
			s.append(i)
			for m in j.split('- '):
				if not m == '':
					s.append(m.strip())
			a = isearch.search(s)
			for k in a:
				music[i][j].append(k)
			
	pprint.pprint(music)
	
	c = CoverGrabber(music)
	c.main()
