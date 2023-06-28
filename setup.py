from setuptools import setup, find_packages

setup(
    name='diself',
    version='1.0.5',
    license='MIT',
    description='A python module like discord.py but for selfbot',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['websocket-client', 'requests'],
    url='https://github.com/lululepu/diself',
    author='Lululepu',
    author_email='a.no.qsdf@gmail.com'
)  
