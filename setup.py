import setuptools
with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()
    
setuptools.setup(
    name = "cbmc",
    version = "0.0.2",
    author = "Hans",
    author_email="ccoccc14@gmail.com",
    description="麥塊匿名發文平台 api for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HansHans135/cbmc",                                         
    packages=setuptools.find_packages(),     
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
    )
