from distutils.core import setup, Extension
#python setup.py build --compiler=mingw32
#python setup.py install

module1 = Extension('hello', sources = ['hello.c'])
module2 = Extension('fib', sources = ['fibmodule.c'])
 
setup (name = 'PackageName',version = '1.0',
        description = 'This is a demo package',
		author='evanokeeffe@gmail.com',
        ext_modules = [module1])
 
setup (name = 'PackageName',
        version = '1.0',
        description = 'demo fibonacci numbers package',
        ext_modules = [module2])