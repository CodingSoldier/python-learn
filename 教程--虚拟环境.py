#####安装virtualenv
pip install virtualenv

virtualenv testvir   # 会新建testvir目录

cd Scripts
activate.bat  # 运行avtivate.bat

deactivate.bat  #退出



#########再安装virtualenvwrapper-win
pip install virtualenvwrapper-win   # linux下是pip install virtualenvwrapper

mkvirtualenv testvir2   # 新建了目录C:\Users\Administrator\Envs\testvir2

deactivate  # 退出


workon  # 查看虚拟环境
workon testvir2  # 进入虚拟环境
pip install requests   # 在虚拟环境中安装模块
pip list  #  查看模块
pip uninstall requests   # 卸载模块


















