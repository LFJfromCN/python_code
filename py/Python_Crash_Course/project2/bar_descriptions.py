import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#89F7FE', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title =  'Python Projects'
chart.x_labels = ['awesome-python', 'youtube-dl', 'public-apis']

plot_dicts = [
    {'value': 49293, 'label': 'Description of awesome-python.'},
    {'value': 36513, 'label': 'Description of youtube-dl.'},
    {'value': 36169, 'label': 'Description of public-apis.'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar-descriptions.svg')
    
