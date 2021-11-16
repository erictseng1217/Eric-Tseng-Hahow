# !/usr/bin/python
# coding:utf-8
# 定義函式
class Score:
    def __init__(self, episode, title):
        self.episode = episode
        self.title = title

    def __repr__(self):
        return repr((self.episode, self.title))


scores_obj = [
    Score('4', 'A New Hope'),
    Score('5', 'The Empire Strikes Back'),
    Score('6', 'Return of the Jedi'),
    Score('1', 'The Phantom Menace'),
    Score('2', 'Attack of the Clones'),
    Score('3', 'Revenge of the Sith')
]
print(sorted(scores_obj, key=lambda s: s.episode))  # 按照episode排序
