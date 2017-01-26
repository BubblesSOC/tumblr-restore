from setuptools import setup

setup(
    name='Tumblr Restore',
    version='0.0.1',
    description='Import Tumblr posts to a specified blog from a JSON backup',
    author='Bubs',
    author_email='bubblessoc@gmail.com',
    url='https://github.com/bubblessoc/tumblr-restore',
    packages=['tumblr_restore'],
    install_requires=['oauth2','pytumblr'],
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points = {
        'console_scripts': ['tumblr-restore=tumblr_restore.command_line:main']
    },
    include_package_data=True
)
