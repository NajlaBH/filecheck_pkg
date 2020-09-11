import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="poetpack_tmpl", # Replace with your own username
    version="0.1.0",
    author="NajlaBH",
    author_email="bhndevtools@gmail.com",
    description="A poetry python package template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NajlaBH/poetpack_tmpl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
