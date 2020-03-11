# tistory2md
html로 구성된 tistory 블로그 글을 markdown 파일로 백업하는 프로그램입니다. 직접 사용하기 위해 급하게 작성한 프로그램이므로 퀄리티가 떨어질 수 있습니다. 실행 중 오류로 인해 종료가 되면 다시 실행시켜 시도해보시기 바랍니다. 실행 중 버그&오류나 이외의 질문이 있으시면 123456ccdd@naver.com로 메일 보내주세요. 


## 스크린샷
<div>
<img width="698" alt="스크린샷 2020-03-10 오후 9 17 20" src="https://user-images.githubusercontent.com/21357649/76311576-9d6ec700-6314-11ea-9989-c4686154e26a.png"> <br/>
OS X 버전의 스크린샷입니다. Windows의 경우 다를 수 있습니다.


## 다운로드
<a href=https://github.com/2-Chae/tistory2md/releases/tag/v1.0>다운로드</a> 사이트에서 다운로드가 가능합니다. <br/>
<strong>Windows</strong>의 경우 <strong>tistory.exe.zip</strong>을 다운받으시면 됩니다.<br/>
<strong>OS X (Mac)</strong>의 경우 <strong>tistory2md.dmg</strong>를 다운받으시면 됩니다. <br/><br/>
위의 프로그램이 작동하지 않거나 python 파일로 다운받아서 실행시키고 싶으시면 아래 설명 중 python 실행법을 참고하시면 됩니다.<br/>
실행 전 반드시 아래의 설명을 읽어보시길 바랍니다.

## 항목 설명
#### blog 주소
본인의 tistory 주소를 적습니다. tistory.com을 제외한 앞의 주소만 적어주시면 됩니다.

#### Access Token
tistory 접근을 위한 본인의 access token을 적습니다. Access token을 얻는 방법은 구글링을 하시면 쉽게 찾을 수 있습니다. 저는 https://modu-print.tistory.com/135 의 도움을 받았습니다.

#### 문서 번호
본인 블로그의 몇 번 문서를 내려받을지 적으시면 됩니다. 끝 번호는 넉넉잡아 적으셔도 되긴 합니다. 만일 하나의 문서만 받고 싶으시면 시작번호와 끝 번호를 같게 적어주시면 됩니다. 예를 들어 13번 글을 받으시려면 시작도 13 끝도 13을 적으시면 됩니다.

#### 저장 위치
오른쪽의 ... 버튼을 눌러 새로운 디렉터리를 설정하시면 됩니다. 하지만 실행파일과 같은 위치를 추천합니다.

#### 체크박스
- image 다운로드 : tistory 블로그 포스트에 올렸던 이미지들도 가능한 한 모두 다운로드합니다.
- Tag 포함 : tistory 블로그 포스트에 적었던 태그들을 아래 이미지처럼 markdown 포스트에 tags로 적어줍니다. 
  <img width="231" alt="스크린샷 2020-03-10 오후 9 40 35" src="https://user-images.githubusercontent.com/21357649/76313158-c93f7c00-6317-11ea-9697-e9acee18fc06.png">
- Youtube : tistory 블로그에 올렸던 유튜브 링크들을 embedded 형식으로 삽입하게 도와줍니다. http://www.halryang.net/embed-youtube-responsively/ 사이트를 참고하시면 됩니다.

## 실행 순서
### 1. 항목을 채워줍니다.
<img width="698" alt="스크린샷 2020-03-10 오후 9 08 25" src="https://user-images.githubusercontent.com/21357649/76312844-37377380-6317-11ea-9132-9d60ea127223.png">

비어있는 항목을 모두 채워줍니다. <br/><br/>

### 2. 체크박스 옆 "설정 완료" 버튼을 여러 번 클릭해줍니다.
<img width="698" alt="스크린샷 2020-03-10 오후 9 08 35" src="https://user-images.githubusercontent.com/21357649/76379944-d6e71700-6394-11ea-81a2-42506ec292d0.png">

<strong>반드시 여러 번</strong> 클릭을 해주세요!! <br/><br/>

### 3. Start 버튼을 눌러 백업을 시작합니다.
<img width="698" alt="스크린샷 2020-03-10 오후 9 08 47" src="https://user-images.githubusercontent.com/21357649/76380053-262d4780-6395-11ea-8de0-097d9d069015.png">

간혹 start 버튼이 파란색으로 보이지 않는다거나 별 반응이 없어 보여도 "설정 완료" 버튼을 여러 번 클릭한 후라면 활성화가 되어있는 상태이니 start 버튼을 눌러주시면 됩니다. <br/><br/>

### 4. 설정한 디렉터리 파일 및 로그 파일을 확인합니다.
설정한 디렉터리에 백업파일들이 폴더별로 다운받아진 것을 확인한 후 log 화면을 확인합니다.<br/>
Windows의 경우 프로그램이 존재하는 디렉터리에 log.txt 파일이 작성됩니다.
- done : 잘 받아진 문서입니다. (다운로드 성공)
- [Error] OSError: [Errno 22] : Windows에서 나타나는 오류로 문서명에 특수문자가 포함된 경우입니다. 저장되는 markdown 파일명을 문서넘버로 대체하여 저장됩니다. 확인 후 직접 바꿔주시면 됩니다. (다운로드 성공)
- [Error] 비공개 카테고리 : 카테고리 자체가 비공개 상태입니다. (다운로드 실패)
- [Error] {"status":"404} : 없는 페이지이거나 비공개 문서입니다. (다운로드 실패)


## python 실행법
평소 python에 익숙하신 분들에게 추천드리는 방법입니다. <a href=https://github.com/2-Chae/tistory2md/releases/tag/v1.0>다운로드</a>사이트에서 source code를 다운받아 압축을 푸신 후 terminal 에서 해당 디렉터리로 들어가시면 됩니다.

pip를 이용하여 필요한 파일들을 다운받아 줍니다.
```
$ pip install -r requirements.txt
```

설치 후 아래 명령을 입력하면 프로그램이 실행됩니다.
~~~
$ python tistory2md.py
~~~
