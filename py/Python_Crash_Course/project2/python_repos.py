import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#执行API调用并储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

#将API响应储存在一个变量中
response_dict = r.json( )
print('Total repositories:', response_dict['total_count'])

#处理结果print(response_dict.keys( ))
#print(response_dict['incomplete_results'])为False表明已经完整

#探索有关仓库的信息
repo_dicts = response_dict['items']

names, plot_dicts = [ ], [ ]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
       'value': repo_dict['stargazers_count'],
       'label': str(repo_dict['description']),
       'xlink': repo_dict['html_url'],      #这个功能真是棒棒哒
       }
    plot_dicts.append(plot_dict)

#可视化
my_style = LS('#40A798', base_style=LCS)

my_config = pygal.Config( )
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)    #通过my_config传递了所以配置
chart.title = 'Most-Starrred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

