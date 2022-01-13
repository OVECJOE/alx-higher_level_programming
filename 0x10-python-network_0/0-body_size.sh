#!/bin/bash
# Sends a request to that URL, and displays the size of the response body
curl -s "$1" | wc -c
