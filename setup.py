from setuptools import setup, find_packages

setup(
    name='Tumblr Restore',
    version='0.0.1',
    description='Import Tumblr posts to a specified blog from a JSON backup',
    author='Bubs',
    author_email='bubblessoc@gmail.com',
    url='https://github.com/bubblessoc/tumblr-restore',
    packages=find_packages(),
    install_requires=['pytumblr'],
    tests_require=['nose'],
    test_suite='nose.collector',
    entry_points = {
        'console_scripts': ['tumblr-restore=tumblr_restore:main']
    }
)
