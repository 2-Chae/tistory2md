import requests
import json
import html2text
import os
import errno
import re
from io import StringIO
import urllib

import ssl

def create_folder(filename):
    if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

class BackUp():
    def __init__(self, blogName, token, dir, checkbox):
        ssl._create_default_https_context = ssl._create_unverified_context
        self.blogName = blogName
        self.token = token
        self.dir = dir
        self.checkbox = checkbox

        self.h = html2text.HTML2Text()
        self.h.ignore_links = True



    def start_backup(self, i):
        headers = {'Content-Type': 'application/json;'} 
        url = "https://www.tistory.com/apis/post/read"
        parms = {'access_token': self.token,
                'blogName': self.blogName,
                'postId': i,
                'output': 'json'}
        response = requests.get(url, headers=headers, params = parms)
        return response

    def save_document(self, r):
        message = ''
        link_list = []
        ref_list = []

        catid   = r['tistory']['item']['categoryId']
        docid   = r['tistory']['item']['id']
        date    = r['tistory']['item']['date']
        title   = r['tistory']['item']['title']
        content = r['tistory']['item']['content']

        tagsExist = False
        if len(r['tistory']['item']['tags']) > 0:
            tags = r['tistory']['item']['tags']['tag']
            tagsExist = True

        if not catid:
            catid = 'no_category'

        cat = catid
        # # if catid in cats:
        # #     cat = cats[catid][0]
             
        folder = self.blogName  + '/' + cat + '/' + docid
        filename = self.dir + '/' + folder + '/' + date.split(' ')[0] + '-' + title + '.md'
        create_folder(filename)


        try:
            final = self.h.handle(content)
            buf = final.split('\n')
            
            for k, line in enumerate(buf):
                if 'https://t1.daumcdn.net/tistory_admin/assets/' in line or 'http://kage.tistory.com/image/' in line:
                    continue
                
                version = 0
                if '[##_Image' in line: # 최신버전 이미지  서버
                    links = [line]
                    version = 1
                elif 'cfile' in line or 'data:image' in line or 'k.kakaocdn.net' in line or 'tutorialspoint' in line:
                    links = re.findall(r'!\[\]\((.*?)\)', line)
                    version = 2
                else: # 구버전
                    links = re.findall(r'!\[\]\((.*?)\)', line)

                newline = ''
                for l in links:               
                    if ('img.png' not in l) and ('image' not in l) and ('Image' not in l):
                        continue

                    if version == 1:
                        temp = l.split('@')[1]
                        temp = temp.split('|')[0]
                        if 'img' in temp:
                            l = 'https://k.kakaocdn.net/dn/' + temp
                        else:
                            l = 'https://t1.daumcdn.net/cfile/tistory/' + temp
                    elif version == 2:
                        l = l
                    else:
                        l = 'https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https://k.kakaocdn.net/dn/' + l.split('@')[1]
                        
                    # print(l)
                    link_list.append(l)
                    i = len(ref_list)
                    ref = '[link{}]:{}'.format(i, l)
                    newline += '![][link{}]'.format(i)
                    ref_list.append(ref)
                    
                if len(links) > 0:
                    buf[k] = newline
            
            buf.extend(ref_list)


            try:
                f = open(filename, 'w', encoding='utf-8')

            except:
                message += 'OSError: [Errno 22]'
                filename = self.dir + '/' + folder + '/' + date.split(' ')[0] + '-' +docid + '.md'
                f = open(filename, 'w', encoding='utf-8')

            f.write('---' + '\n')
            f.write('layout: post' + '\n')
            f.write('title: \'' + title + '\'\n')
            if self.checkbox['tag'] and tagsExist:
                f.write('tags: [')
                for tag in tags:
                    f.write('\''+ tag + '\',')
                f.write(']\n')
            f.write('---' + '\n')

            for line in buf:
                if ('https://youtu.be/' in line) or  ('https://www.youtube.com/' in line): 
                    # Responsive embedded youtube 넣기
                    if self.checkbox['youtube']:
                        f.write('{% youtube '+ line +' %}')
                    else:
                        f.write((str(line) + '\n'))
    
                 # invalid-file 제거하기 or 거르고 싶은 문자열 제거.
                elif ('data-origin-width' in line) or ('invalid-file' in line) or ('---|---' in line) or ('|' == line) or ('https://t1.daumcdn.net/tistory_admin/assets/' in line) or ('origin-width' in line) or ('##]' in line):
                    continue
                else:
                    f.write((str(line) + '\n'))
        

            # print(link_list)
            if self.checkbox['image']:
                for k, link in enumerate(link_list):
                    imagefile = folder + '/' + str(k) + '.jpg'
                    create_folder(imagefile)
                    try:
                        urllib.request.urlretrieve(link, imagefile)
                    except:
                        message += 'failed to download image :' + link +'\n'
                        # print('failed to download image :', link)

            return message

        except UnicodeEncodeError as e:
            # print(e)
            return e
    