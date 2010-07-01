#!/usr/bin/env python
# -*- coding: utf-8 -*-
FORMATS = ['mp3', 'mpc', 'wma', 'ogg']

import os
import shutil

class FolderCheck:
	def __init__(self, musicDir, renameIfOne=True):
		self.musicDir = musicDir
		self.imageName = 'folder.jpg'
		self.renameIfOne = renameIfOne
	
	def read(self):
		tree = {}
		artists = os.listdir(self.musicDir)
		artists.sort()
		for a in artists:
			tree[a] = {}
			albums = os.listdir(os.path.join(self.musicDir, a))
			for i in albums:
				tree[a][i] = []
				files = os.listdir(os.path.join(self.musicDir, a, i))
				for j in files:
					if not j[-3:] in FORMATS:				
						tree[a][i].append(j)
				if len(tree[a][i]) == 1 and tree[a][i][0][-3:] == 'jpg':
					if self.renameIfOne:
						root = os.path.join(
							self.musicDir,
							a,
							i
						)
						source = os.path.join(
							root,
							tree[a][i][0]
						)
						dest = os.path.join(
							root,
							self.imageName
						)
						shutil.move(source, dest)
						
					if tree[a][i][0] == self.imageName:
						del tree[a][i]
			if len(tree[a]) == 0:
				del tree[a]		
		return tree
