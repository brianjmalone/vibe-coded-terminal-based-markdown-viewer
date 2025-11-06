from setuptools import setup

setup(
    name='mdview',
    version='0.1.0',
    py_modules=['mdview'],
    install_requires=[
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'mdview=mdview:main',
        ],
    },
)
