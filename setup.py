from setuptools import setup, find_packages

setup(
    name='datasnap',
    version='0.1.0',
    packages=find_packages(),
    description='A tool to generate quick data insights and column recommendations for dataframes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Nicolas Prieur',
    author_email='pu-zle@live.fr',
    url='https://github.com/ShelbyTO/datasnap',
    license='MIT',
    install_requires=[
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
