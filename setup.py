from setuptools import setup, find_packages

setup(
    name='diself',
    version='0.1',
    license='MIT',
    description='A python module like discord.py but for selfbot',
    long_description=open('README.md').read(),
    install_requires=['websocket-client', 'requests'],
    url='https://github.com/lululepu/diself',
    author='Lululepu',
    author_email='a.no.qsdf@gmail.com'
)
