# _*_ codding:utf-8 _*_
"""
    Function:词云
    Author: yqc
"""

from wordcloud import WordCloud
import jieba
import os
import numpy
import PIL.Image as Image

cur_path = os.path.dirname(__file__) + "/resource"

# 屏蔽关键字
stopwords = {'一潭': 0, '一些': 0}


# 文本中含中文时
def chinese_jieba(text):
    wordcloud_jieba = jieba.cut(text)
    text_jieba = " ".join(wordcloud_jieba)
    return text_jieba


with open(os.path.join(cur_path, 'zbkq.txt'), encoding='UTF-8') as fp:
    text = fp.read()
    text = chinese_jieba(text)
    mask_pic = numpy.array(Image.open(os.path.join(cur_path, 'timg.jpeg')))
    # wordcloud = WordCloud().generate(text)
    # 自定义背景颜色
    wordcloud = WordCloud(background_color='black', max_words=100, max_font_size=45,
                          font_path='STXINGKA.TTF', stopwords=stopwords, mask=mask_pic).generate(text)
    image = wordcloud.to_image()
    image.show()
