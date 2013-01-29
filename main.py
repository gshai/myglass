'''
Created on Jan 25, 2013

@author: gshai
'''
# Add the library location to the path
import logging
import openanything
import parseCaption

 
if __name__ == '__main__':
    logging.info('gshai - main')
    print('print - yeah!')
    useragent = 'MyHTTPWebServicesApp/1.0'
    source = "http://hearst.api.mashery.com/ArticleImage/search?_pretty=0&shape=brief&site_id=817&start=0&limit=2&sort=name%2Casc&total=0&api_key=r26w2jzhsv6jv8m476fty4dz"
    print(source)
    params = openanything.fetch(source, useragent)
    parseCaption.parseJSON(params)
    
    
    pass