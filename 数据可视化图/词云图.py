from pyecharts import WordCloud

language = ['Python', 'C++', 'C', 'Java', 'C#', 'PHP', 'R', 'JavaScript', 'Go', 'Assembly']
rank = [100, 98.4, 98.2, 97.5, 89.8, 85.4, 83.3, 82.8, 76.7, 74.5]
wordcloud = WordCloud(width=1500, height=700)
wordcloud.add('', language, rank, word_size_range=[20, 100])
wordcloud.render('D:\\pye\\wc.html')    # 在指定目录下生成文件
