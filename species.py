# !/usr/bin/python
# coding:utf-8
species = [1, 2, 2, 3, 5, 6, 8, 9, 10, 15]  # 種族編號
# 列出種族個數
for i in set(species):
    print('種族：%s,個數：%s' % (i, species.count(i)))
# 列出種族數量
total = list(set(species))
print('在第6部曲總共出現多少種族: %s 種' % len(total))
