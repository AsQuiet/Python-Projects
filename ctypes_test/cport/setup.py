from distutils.core import setup, Extension
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
temp_path = os.path.join(dir_path, "temp.txt")

f = open(temp_path, "r")
file_name = f.read().rstrip("\n")
f.close()

example_module = Extension('_' + file_name, sources=[file_name+'_wrap.c', file_name+'.c'])
setup(name=file_name, ext_modules=[example_module], py_modules=[file_name])
