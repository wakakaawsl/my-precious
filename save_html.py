import urllib.request


def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html


def saveHtml(file_name, file_content):
    with open(file_name.replace('/', '_') + ".html", "wb") as f:
        f.write(file_content)


html = getHtml("https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4")
saveHtml("text1", html)

print("结束")