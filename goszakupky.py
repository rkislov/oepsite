import feedparser
import datetime
NewsFeed = feedparser.parse("https://zakupki.gov.ru/tinyurl/dd5f725ab013f8e834007c3265b819abcafe999ec2f2add484540dbfafffba54")
entry = NewsFeed.entries[1]
s = entry.summary

print(s.split('<br />')[7].replace('&nbsp;','').replace('&#039;','').replace('<strong>Наименование объекта закупки: </strong>', 
'').replace('&nbsp;','').replace('&laquo;','"').replace('&raquo;','"'))
print(s.split('<br />')[10].replace('&nbsp;','').replace('&#039;','').replace('<strong>Начальная цена контракта: </strong>','').replace('<strong> Валюта: </strong>Российский рубль',''))
print(datetime.datetime.strptime(s.split('<br />')[11].replace('&nbsp;','').replace('&#039;','').replace('<strong>Размещено: </strong>', ''), '%d.%m.%Y'))
print (entry.title)
print (entry.link)
#print (entry.summary)
