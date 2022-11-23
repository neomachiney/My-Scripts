#!/usr/bin/python3
from requests import post

url = "https://discord.com/api/webhooks/983812381685731408/Sy6woQdql3Q6B39p2EZNKKO0ihS7XDL2obbMXJXR-sV9PMxiZSRFRKRfRdRnj6iLKj2i" #do
url = "https://discord.com/api/webhooks/985119540318986271/MTz3obtdW-fY5M6VPSZP1s0yNoc3nWywV8LPdP6jvXRjNEFs7E0yPWGpOVIVvt1nk5fG" #swap 
content = "$help"
message = {
    "content": content,
}
headers = {
    'Content-Type': 'application/json',
}

hook = post(url, headers = headers, json=message)
