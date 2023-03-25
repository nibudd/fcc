import urllib.request, urllib.parse, urllib.error

page = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in page:
    print(line.decode().rstrip())