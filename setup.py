import re
import setuptools
import subprocess

def get_readme():
    with open("readme.md", "r", encoding='utf-8') as fh:
        readme = fh.read()
        return readme

def get_version():
    proc = subprocess.Popen(['git', 'describe', '--dirty', '--tags'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = proc.communicate()
    result = re.search('^v([^\n]+)\n$', stdout.decode("utf-8"), re.S)
    if not result:
        raise ValueError("Invalid version: '{}'.".format(result))
    return result.group(1)

version = get_version()
long_description = get_readme()

setuptools.setup(
    name="pygglz",
    version=version,
    author="Cornelius Buschka",
    author_email="cbuschka@gmail.com",
    description="A feature toggle library designed after Java togglz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pygglz/pygglz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
