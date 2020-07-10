import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_pastebin",
    version="0.1.0",
    description="Simple pastebin unofficial wrapper based on web automations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/boardens/simple-pastebin",
    packages=setuptools.find_packages(),
    install_requires=[
        "mechanize",
        "bs4"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)