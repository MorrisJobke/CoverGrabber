#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pprint import pprint
import shutil

FORMATS = ['mp3', 'mpc', 'wma', 'ogg']

musicDir = '~/Daten/Musik/Aktuelle'
musicDir = os.path.expanduser(musicDir)

tree = {}

artists = os.listdir(musicDir)
artists.sort()
for a in artists:
	tree[a] = {}
	albums = os.listdir(os.path.join(musicDir, a))
	for i in albums:
		tree[a][i] = []
		files = os.listdir(os.path.join(musicDir, a, i))
		for j in files:
			if not j[-3:] in FORMATS:				
				tree[a][i].append(j)
		if len(tree[a][i]) == 1 and tree[a][i][0] == 'folder.jpg':
			del tree[a][i]
	if len(tree[a]) == 0:
		del tree[a]

for i in tree:
	print i
	for j in tree[i]:
		tmp = len(tree[i][j])	
		print '\t', j, '\033[1m', tmp, '\033[0;0m'
		for k in tree[i][j]:
			print '\t\033[1m', k, '\033[0;0m'
		if tmp == 1 and tree[i][j][0][-3:] == 'jpg':
			root = os.path.join(
				musicDir,
				i,
				j
			)
			source = os.path.join(
				root,
				tree[i][j][0]
			)
			dest = os.path.join(
				root,
				'folder.jpg'
			)
			shutil.move(source, dest)
print len(tree)
