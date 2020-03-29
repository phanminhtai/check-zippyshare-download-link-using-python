from urllib.request import urlopen
zippyshare_list = ["https://www94.zippyshare.com/v/ojSloc44/file.html","https://www94.zippyshare.com/v/ojSloc4/file.html"]
for i in range(len(zippyshare_list)):
    get_html = urlopen(zippyshare_list[i]).read()
    string = get_html.decode('utf-8')
    string2 = string.count('<div class="download"></div>')
    if string2 == 1:
      print(zippyshare_list[i],"| Okey");
    else:
      print(zippyshare_list[i],"| Died");
