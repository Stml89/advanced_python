from distutils.core import setup

setup(
    name='Lock types',
    version='0.1',
    description='Examples of various types of lock shared'
                ' value between threads',
    author='Siarhei Stamal',
    author_email='siarhei_stamal@epam.com',
    url='http://www.epam.com',
    scripts=['start_app.py'],
    packages=['lock_types'],
)
