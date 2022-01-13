#!/bin/bash
# sends a GET request to a URL with the header variable X-School-User-Id as 98
curl -sH 'X-School-User-Id: 98' "$1"
