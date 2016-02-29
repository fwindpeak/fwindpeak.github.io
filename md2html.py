#!/usr/env python
#coding:utf-8

from markdown2 import markdown as md
from markdown2 import markdown_path as mdf
import os
import time


BLOG_NAME = "fwindpeak's personal blog"
BLOG_DSC = " a test of markdown page"

md_list=[]

head='''
    <div id=head>
    <a href="../index.html">首页</a>
    </div>
'''

discus_name="fwindpeak"

disqus_content='''
<div id="disqus_thread"></div>
<script>

(function() { // DON'T EDIT BELOW THIS LINE
var d = document, s = d.createElement('script');

s.src = '//'''+discus_name+'''.disqus.com/embed.js';

s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>

'''

STYLE_PATH="./style/default.css"

def get_time(sec):
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(sec))

def write_html(title,body,fn,style_path=STYLE_PATH):

    dat='''<!DOCTYPE html>
<html>
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1" />  
        <title>'''+title+'''</title>
<link rel="stylesheet" type="text/css" href="'''+style_path+'''" />
</style>
    </head>
    <body>'''+body+'''</body>
</html>'''

    file(fn,"w").write(dat)

def init():
    try:
        os.mkdir("./content")
    except OSError,e:
        pass
    try:
        os.mkdir("./markdown")
    except OSError,e:
        pass
    
def get_title_and_abstract(fn):
    fp = open(fn,"r")
    title = fp.readline()
    title = title.strip()
    i = 0
    abstract = ""
    while True:
        ldat = fp.readline()
        if ldat == '':
            break
        if ldat=='\n' or ldat == '\n\r' or ldat == '\r\n':
            continue
        if ldat.startswith('#') or ldat.startswith("="):
            continue
        i = i+1
        abstract+=ldat
        if i>3:
            break
    fp.close()
    print title
    return title,abstract
        

def process_md():
    global md_list
    global head
    global disqus_content
    for fn in os.listdir("./markdown"):
        md_dict={}
        print fn
        fpath = "./markdown/"+fn
        fname = fn[:fn.rfind(".")]+".html"
        title,abstract = get_title_and_abstract(fpath)
        md_dict['fname'] = fname
        md_dict['title'] = title
        md_dict['abstract'] = abstract
        md_dict['ctime'] = os.path.getctime(fpath)
        md_dict['mtime'] = os.path.getmtime(fpath)
        
        if md_dict['ctime'] > md_dict['mtime']:
            md_dict['ctime'] = md_dict['mtime']
        
        md_list.append(md_dict)

        body = mdf(fpath).encode("utf-8")
        body = head+body+disqus_content
        write_html(title,body,"./content/"+fname)

    # sort md_list by create time down
    md_list.sort(key=lambda x:x['ctime'])
    md_list.reverse()

def write_index():
    global BLOG_NAME
    global md_list
    index_md = "# "+BLOG_NAME+"\n\n"+BLOG_DSC+"\n\n"
    for dic in md_list:
        index_md += "## [%s](./content/%s)\n"%(dic['title'],dic['fname'])
        ctime = get_time(dic['ctime'])
        index_md += "*%s*\n\n"%(ctime)
        index_md += dic['abstract']+"\n\n"
        index_md += "-------\n\n"
    open("./index.md","w").write(index_md)
    body = mdf("./index.md").encode("utf-8")
    write_html(BLOG_NAME,body,"./index.html","./content/style/default.css")
        

if __name__ == '__main__':
    init()
    process_md()
    write_index()
    
