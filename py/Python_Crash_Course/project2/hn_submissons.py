'''现在没钱翻墙，这个程序无法正确运行'''
import requests
from operator import itemgetter

#执行API调用并储存响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status code: ', r.status_code)

#处理有关每篇文章的信息
submission_ids = r.json( )
submission_dicts = [ ]
for submission_id in submission_ids[:30]:
    #对于每一篇文章都执行一个API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
           str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json( )

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
        }
    submisson_dicts.append(submission_dict)

submisson_dicts = sorted(submisson_dicts, key=itemgetter('comments'),
                         reverse=True)

for submission_dict in submisson_dicts:
    print('\nTitle:', submission_dict['title'])
    print('Discussion link:', submission_dict['link'])
    print('Comments:', submission_dict['commentd'])
    
