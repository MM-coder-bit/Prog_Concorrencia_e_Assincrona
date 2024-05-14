from distutils.core import setup  # Importa a função setup do módulo distutils.core, usada para configurar extensões.
from Cython.Build import cythonize  # Importa a função cythonize do módulo Cython.Build, que compila arquivos .pyx para .c.

setup(
    # A função setup é chamada com um argumento nomeado 'ext_modules'.
    ext_modules=cythonize(['cumprimenta.pyx', 'computa.pyx'])
    # A função cythonize compila os arquivos Cython listados ('cumprimenta.pyx' e 'computa.pyx') em extensões Python.
)
