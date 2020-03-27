import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygglz",
    version="0.0.2",
    author="Cornelius Buschka",
    author_email="cbuschka@gmail.com",
    description="A feature toggle library designed after Java togglz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cbuschka/pygglz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
