#!/bin/bash
# takes in a URL, sends a request to that URL, and displays
# the size of the body of the response
curl -sI "$1" | grep -oIE 'Content-Length: [0-9]+' | cut -d " " -f2 
