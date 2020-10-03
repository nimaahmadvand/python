import shutil
import os

#------copy a file------
shutil.copy('C:\\Windows\\System32\\calc.exe', 'C:\\Users\\Nima\\Desktop\\calculatox.exe')

#------move or rename a file------
shutil.move('C:\\Users\\Nima\\Desktop\\calculatox.exe' , 'C:\\Users\\Nima\\Desktop\\calculator.exe')

#------delete a file------
os.unlink('C:\\Users\\Nima\\Desktop\\calculator.exe')

#------copy an entire folder------
shutil.copytree('C:\\bin' , 'C:\\Users\\Nima\\Desktop\\bin_backup')

#------delete an entire folder------
shutil.rmtree('C:\\Users\\Nima\\Desktop\\bin_backup')

#------send a file or a folder to recycle bin------
#pip install send2trash
import send2trash
shutil.copytree('C:\\bin' , 'C:\\Users\\Nima\\Desktop\\bin_backup')
send2trash.send2trash('C:\\Users\\Nima\\Desktop\\bin_backup')