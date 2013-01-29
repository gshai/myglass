'''
Created on Jan 28, 2013

@author: gshai

params = openanything.fetch(source, useragent)
     
    data = params['data']
    print('data = ', data)
    
    #process the JSON call back
    dataDict = ast.literal_eval(data)    
    for key in dataDict.keys():
        print "key: %s , value: %s" % (key, dataDict[key])
    
'''
import ast

def parseJSON(params):
    print(str(params))
    data = params['data']
    print('data = ', data)
    
    #process the JSON call back
    dataDict = ast.literal_eval(data)    
    for key in dataDict.keys():
        print "key: %s , value: %s" % (key, dataDict[key])
    items = dataDict["items"]
    print "items: %s" % (items)
    
    for item in items:
        print "caption: %s" % (item['caption'])
    pass
