from idaapi import *
import operator

funcs = Functions()
dictNameFunc = {}
for f in funcs:
   nameFunc = Name(f)
   xrefs = len(list(XrefsTo(f)))
   dictNameFunc.update({nameFunc:xrefs})

sorted_dict = sorted(dictNameFunc.items(),key=operator.itemgetter(1))
for i in sorted_dict:
	print str(i[0]),str(i[1]),"\n"