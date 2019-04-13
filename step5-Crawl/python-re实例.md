# 《Python 正则表达式 之 实战》
## 爬取 HTML 文档的字符编码
网页中通常是将字符编码信息放在 [\<head\>](#welcome) 头部信息的 [\<meta\>](#welcome) 标签中。所以我们首先利用爬虫，爬取到网站的所有 html 内容：
```python
import requests
from bs4 import BeautifulSoup

url = 'http://www.baidu.com/'

html = requests.get(url)
```

利用正则表达式，得到 [\<head\>](#welcome) 标签中的所有内容：
```python
head = re.findall(r'<head>.*</head>', html.text)
```

注意，在 HTML 文档中，规定字符编码有两种格式，如下所示：
```python
htmlstr1 = '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
htmlstr2 = '<meta charset="UTF-8">'
```

要得到统一的规则是，字符编码全在`'charset='`后面，但是 `htmlstr1` 中比 `htmlstr2` 少了一个双引号 `"` ，所以我们得想办法忽略掉这个 `"` 引号的影响。

如果我们单纯的用 或 `|` ，比如 `("|)` ，双引号或者空格来匹配，是匹配不了的。这时候必须要用到正则表达式里一个[无捕获组 '(?:)'](#welcome)。

如：[[?:dog|cat]](#welcome) 它的有效范围是 [?:](#welcome) 后面 [|](#welcome)两边的整条规则。所以这里如果是 [(?:"|)](#welcome)（等价于[(?:|")](#welcome)），相当于匹配双引号 `"` 和一个空白字符，即相当于忽略掉双引号 `"` 的影响。

整体代码如下：
```python
import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.baidu.com/'

html = requests.get(url)
soup = BeautifulSoup(html.text,'lxml')
head = re.findall(r'<head>.*</head>', html.text)
# 注意每次 re.findall() 返回的是一个列表
charset = re.findall(r'charset=(?:|")([\w-]+)', head[0])
print(charset[0])
```

## 第二个
