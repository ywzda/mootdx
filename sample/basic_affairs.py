from mootdx.affair import Affair

# Affairs.parse(downdir='tmp') # 解析全部
# Affairs.parse(downdir='tmp', filename='gpcw19960630.zip') # 解析文件
# Affairs.parse(downdir='tmp', filename='gpcw19960630.zip').to_csv('gpcw19960630.csv') # 转存文件

Affair.files() # 显示列表
# Affairs.fetch(filelist=True) # 显示列表
# Affairs.fetch(downdir='tmp') # 下载全部
# Affairs.fetch(downdir='tmp', filename='gpcw19960630.zip') # 下载文件

# affairs = Affairs(downdir='tmp')
# affairs.fetch()