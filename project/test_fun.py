import sys
sys.path.append('..') #必须要, 设置project为源程序的包顶

'''
功能测试脚本
'''

from project.Scrawl.QQMusic import QQMusic
app1 = QQMusic.QQMusic()
print(app1.search_by_keyword('纸短情长'))

from project.Scrawl.NeteasyMusic import NeteasyMusic
app2 = NeteasyMusic.Netmusic()
print(app2.pre_response_neteasymusic('大鱼'))

from project.Scrawl.XiamiMusic.XiamiMusic import Search_xiami
app3 = Search_xiami()
print(app3.search_xiami('纸短情长'))