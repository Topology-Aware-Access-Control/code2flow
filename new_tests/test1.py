import requests

def c():
    pass

def a():
    b()
    requests.get('http://localhost:5000/')

def b():
    c()
