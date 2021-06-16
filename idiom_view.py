# -*- coding: utf-8 -*-
"""
Created on Sun Jun 6 00:52:22 2021

@author: 86181
"""
#导入整个窗体框架文件
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from idiom_ui import Ui_Form
from idiom_game import *  
#一次性的将所有python 调用函数方法导入

#自己建的类，继承QtWidgets.Qwidget类方法和Ui_Form界面类
class IdiomView(QMainWindow,Ui_Form):
    def __init__(self,*args,**kwargs):
        #*args是将函数多余的参数以 元组 的方式传入；
        #**kwargs是将多余的赋值参数（或者说带名字的参数）以 字典 的形式传入
        #*args就是传递一个可变参数列表给函数实参，这个参数列表的数目未知，甚至长度可以为0
        super(IdiomView, self).__init__(*args,**kwargs)
        #就是继承父类的init方法，同样可以使用super()点 其他方法名，去继承其他方法。
        self.setupUi(self)
        self.pushButton.clicked.connect(self.user_answer)
        self.cancelButton.clicked.connect(self.user_cancel)
        self.init_game()

    def init_game(self):
        readall() #读入整个文件的内容
        self.pc_ask()

    def pc_ask(self):
        t = pc_question()
        if t:
            memory.add(t)
            self.set_info("NPC出题:%s"%t)
            self.set_pc_question(t)
            self.pushButton.setEnabled(True)
            self.lineEdit.setText("")
        else:
            self.set_warning("题库已空")
            self.pushButton.setEnabled(False)

    def pc_reply(self,idiom):
        p = pc_answer(idiom)
        if p:
            memory.add(p)
            self.set_info("NPC接龙:%s"%p)
            self.set_pc_question(p)
            self.pushButton.setEnabled(True)
            self.lineEdit.setText("")
        else:
            self.set_result("你真是人间小机智！") #NPC未接上
            self.pushButton.setEnabled(False)
            self.pc_ask()

    def pc_think(self,idiom):
        p = pc_answer(idiom)
        if p:
            memory.add(p)
            self.set_info("NPC自问自答: %s"%p)
            self.set_pc_question(p)
            self.pushButton.setEnabled(True)
            #setEnabled():设置成true时，相当于激活了按钮
            #会对触摸或者点击产生反应，并且可以响应一些触发事件
            self.lineEdit.setText("")
        else:
            self.set_result("NPC:嘿嘿，我也不会")
            self.pushButton.setEnabled(False)
            self.pc_ask()

    def set_pc_question(self,idiom):
        self.lblIdiom.setText(idiom)  #在qt设计的对象中选入成语
        #setText()用于设置文本信息

    def set_info(self,text):
        self.textBrowser.append('<font color="green">%s</font>'%text)

    def set_result(self,text):
        self.textBrowser.append('<font color="blue">%s</font>'%text)

    def set_warning(self,text):
        self.textBrowser.append('<font color="red">%s</font>'%text)

    def set_answer(self,text):
        self.textBrowser.append('<font color="black">%s</font>'%text)

    def user_answer(self):
        p = self.lineEdit.text()
        if idiom_exists(p) == False:
            self.set_warning("get不到，学会了再告诉你")
            return

        if p in memory:
            self.set_warning("该成语已被使用过啦")
            return

        t = self.lblIdiom.text()
        if idiom_test(t, p) == False:
            self.set_warning("哦吼，接龙错误，再想想")
            return

        memory.add(p)
        self.set_answer(p)
        self.pc_reply(p)

    def user_cancel(self):
        t = self.lblIdiom.text()
        self.pc_think(t)

if __name__=='__main__':
    app = QApplication(sys.argv)
    #pyqt 窗口必须在QApplication方法中使用
    widget = IdiomView() #生成widget类的实例idiomView
    widget.show()
    sys.exit(app.exec_())
    ##消息结束的时候，结束进程，并返回0，接着调用sys.exit(0)退出程序
