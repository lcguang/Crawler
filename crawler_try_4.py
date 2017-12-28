import re
import requests
import pandas as pd

def hot_github(keyword):
    url = 'https://github.com/trending/{0}'.format(keyword)
    main_url = 'https://github.com{0}'
    html = requests.get(url).content.decode('utf-8')
    reg_hot_url = re.compile('<h3 class="repo-list-name">\s*<a href="(.*?)">')
    hot_url = [main_url.format(i) for i in re.findall(reg_hot_url, html)]
    url_abstract_reg = re.compile('<p class="repo-list-description">\s*(.*?)\s*</p>')
    summary_text = re.findall(url_abstract_reg, html)
    hotDF = pd.DataFrame()
    hotDF['Project Summary'] = summary_text
    hotDF['Project Address'] = hot_url
    hotDF.to_csv('/Users/chenguangliu/Documents/crawlers/tables/github_hot.csv', index=False)

if __name__ == '__main__':
    #keyword = input('input the hot language:')
    keyword = 'python'
    hot_github(keyword)