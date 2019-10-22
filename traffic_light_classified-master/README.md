
这是一个图像识别项目，基于tensorflow，现有的CNN网络可以识别三种信号灯的种类。适合新手对使用tensorflow进行一个完整的图像识别过程有一个大致轮廓。项目包括对数据集的处理，从硬盘读取数据，CNN网络的定义，训练过程。
## Require
1. Python3.5+
2. tensorflow
3. wxPython
## Quick start
- git clone这个项目
- 导入你喜欢的IDE如pycharm，或者你喜欢的编辑器如Atom。
- 图像数据集在image中，分为green,red,yellow三类
- 修改train.py中
```
train_dir = ' '  # 训练样本的读入路径
logs_train_dir = ' '  # logs存储路径
```
为你本机的目录。
- 运行train.py开始训练。
- 训练完成后，修改test.py中的`logs_train_dir = ' '`为你的目录。
- 运行test.py查看结果。
