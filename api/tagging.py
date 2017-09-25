#-*- encoding:utf-8 -*-
from __future__ import print_function

import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

import pandas as pd
import jieba.analyse


class Tagging(object):
    def post(self, article=dict):
        return self.get_tags(article)

    # TODO move logic to lib
    def get_tags(self, article):
        article_tags = []
        content = str(article['content'])
        # print('url: ', article['url'])
        # print()
        print('正文长度：', len(content))
        print()
        print('标题摘要长度：', len(description))
        print()
        text = '。\n'.join(
            [description * (len(content) / len(description)), content])
        # text = description

        print('标题摘要：')
        print(description)
        print()

        print('原文：')
        print(text)
        print()

        print('结巴关键词提取：')
        jieba.analyse.set_stop_words('static/bad_words.txt')
        tags = jieba.analyse.extract_tags(text, topK=10, withWeight=True)
        # allowPOS=('ns', 'n', 'vn', 'v')
        for word, weight in tags:
            article_tags.append(word.lower())
            print(word, weight)
        print()
        # TextRank 算法效果不好，暂时省去
        # tr4w = TextRank4Keyword(stop_words_file='../test/doc/bad_words.txt')
        #
        # tr4w.analyze(
        #     text=text, lower=True, window=2
        # )  # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象
        #
        # print('TextRank 关键词：')
        # for item in tr4w.get_keywords(10, word_min_len=2):
        #     article_tags.append(item.word.lower())
        #     print(item.word, item.weight)
        #
        # 短语和摘要，暂时不需要
        # print()
        # print('TextRank 关键短语：')
        # for phrase in tr4w.get_keyphrases(keywords_num=10, min_occur_num=2):
        #     print(phrase)
        #
        # tr4s = TextRank4Sentence()
        # tr4s.analyze(text=text, lower=True, source='no_stop_words')
        #
        # print()
        # print('摘要：')
        # for item in tr4s.get_key_sentences(num=3):
        #     print(item.index, item.weight, item.sentence)

        # text = codecs.open('../test/doc/01.txt', 'r', 'utf-8').read()
        print(','.join(list(set(article_tags))))
        print()
        return list(set(article_tags))


class_instance = Tagging()
