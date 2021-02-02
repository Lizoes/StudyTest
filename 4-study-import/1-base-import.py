
'''
导入的代码只会执行一遍，以count

import搜索顺序
1、程序的二主目录
2、PYTHONPATH
3、标准库目录
4、任何.pth文件中的内容
5、第三方扩展应用的主目录：site-packages
'''
import sys

for p in sys.path:
    print(p)
