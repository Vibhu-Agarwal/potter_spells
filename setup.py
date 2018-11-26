import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.readlines()

setuptools.setup(
    name="potter_spells",
    version="1.0.1",
    author="Vibhu Agarwal",
    author_email="vibhu4agarwal@gmail.com",
    description="A python package to list all Harry Potter spells",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vibhu-Agarwal/potter_spells",
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='harry potter harrypotter spells harrypotterspells potterspells expelliarmus',
    install_requires=requirements
)
