#!pyhton27
'''
Description:
------------
GUI that displays md5, sha1, sha224, sha256, sha384, sha512
hashes of a string.
Author: S.Haseeb
'''
from tkinter import *
import hashlib

class App:
	def __init__(self):
    ''' Initialise important stuff on call '''
		self.tk = Tk()
		self.tk.title('Hash')
		self.tk.minsize(400, 400)
		self.HASHES = ['MD5', 'SHA1', 'SHA224','SHA256', 'SHA384','SHA512']
		
	def main(self):
		Label(text='Hash Generator', font=('', 20)).pack()
		Label(text='Plain Text').pack()
		self.PLAIN_INPUT = Entry(); self.PLAIN_INPUT.pack()
		Button(text='Generate', command=self.onGenerate).pack()
		
		# Display hashes of the string
		self.hashList()
		self.tk.mainloop()
		
	def hashList(self):
    '''Packs output hashes to GUI'''
		self.ENTRIES = []
		for i in self.HASHES:
			Label(text=i).pack()
			self.ENTRIES.append(Entry())
			for i in self.ENTRIES:
				i.pack(fill=X)

	def onGenerate(self, address=None):
    ''' Called by Generate button '''
		hash_li = []
		hash_li.append( hashlib.md5(self.PLAIN_INPUT.get()).hexdigest() )
		hash_li.append( hashlib.sha1(self.PLAIN_INPUT.get()).hexdigest() )
		hash_li.append( hashlib.sha224(self.PLAIN_INPUT.get()).hexdigest() )
		hash_li.append( hashlib.sha256(self.PLAIN_INPUT.get()).hexdigest() )
		hash_li.append( hashlib.sha384(self.PLAIN_INPUT.get()).hexdigest() )
		hash_li.append( hashlib.sha512(self.PLAIN_INPUT.get()).hexdigest() )
		
		for i in range(len(self.ENTRIES)):
			self.ENTRIES[i].delete(0, 'end')
			self.ENTRIES[i].insert(0, hash_li[i])
		

App().main()
