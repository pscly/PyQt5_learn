import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

#每个应用程序需要一个(且只需要一个)QApplication实例。
#传入sys.argv以允许应用程序的命令行参数。
# sys.argv是传递命令行参数的，当然，我们也可以什么都不传
# 如果您知道不会使用命令行参数，那么QApplication([])就可以了。  # 直接传入空列表



app = QApplication(sys.argv)

window = QWidget()
# window = QMainWindow()

window.resize(300,300)
# window.move(600,10)    # 是在屏幕中心进行的移动位置
window.show() # IMPORTANT!!!!! Windows are hidden by default.  # 重要! ! ! ! !默认情况下窗口是隐藏的。


# Start the event loop.   # 开启事件循环
app.exec_()

# Your application won't reach here until you exit and the event
# loop has stopped.

# ?
# g1


