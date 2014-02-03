'''
Created on 25.1.2014

@author: DannyUfonek

based on LazyImageLoading from the pygame Cookbook:
http://www.pygame.org/wiki/LazyImageLoading?parent=CookBook
'''

import pygame
import weakref
 
class ResourceLoader(object):
    def __init__(self, loader):
        self.__dict__.update(dict(
            #create a resource dictionary
            names = {},
            cache = weakref.WeakValueDictionary(),
            loader = loader
        ))
        
    def __setattr__(self, name, value):
        self.names[name] = value
        
    def __getattr__(self, name):
        try:
            img = self.cache[name]
        except KeyError:
            img = self.loader(self.names[name])
            self.cache[name] = img
        return img
        
    
class ImageLoader(ResourceLoader):
    def __init__(self):
        ResourceLoader.__init__(self, pygame.image.load)
        
