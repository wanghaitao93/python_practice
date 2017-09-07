# -*- encoding=utf-8 -*-

import sys

""" 寻找一个名字叫做thom的人，最少需要几层关系"""
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

# deque 双端队列
# https://docs.python.org/2/library/collections.html#collections.deque

from collections import deque

def person_is_seller(person):
    if person == 'thom':
        return True

def print_path(parents_dict):
    per = 'thom'
    path = []
    path.append('thom')
    while True:
        if per in parents_dict.keys():
            per = parents_dict[per]
            path.append(per)
        else:
            break
    print path[::-1] 

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched_list = []
    parents_dict = {}
    for per in graph[name]:
        parents_dict[per] = name 
    while search_queue:
        person = search_queue.popleft()
        if person not in searched_list:
            if person_is_seller(person):
                print person + ' is find'
                print_path(parents_dict)
                return True
            else:
                search_queue += graph[person]
                searched_list.append(person)
                for per in graph[person]:
                    parents_dict[per] = person
    return False
search('you')
