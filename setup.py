import os
from collections import OrderedDict
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "requirements.txt")) as f:
    dependencies = f.read().strip().split("\n")

setup(
    name="pentestgpt",
    version="0.13.3",
    description="PentestGPT, a GPT-empowered penetration testing tool",
    long_description="""
    PentestGPT is a penetration testing tool empowered by ChatGPT.
    It is designed to automate the penetration testing process. It
    is prototyped initially on top of ChatGPT and operate in an
    interactive mode to guide penetration testers in both overall
    progress and specific operations.
    """,
    author="Ali Vafaev, Tomás Bastante",
    author_email="ali.vafaev@soprasteria.com, tomas.bastante@soprasteria.com",
    maintainer="Ali Vafaev, Tomás Bastante",
    maintainer_email="ali.vafaev@soprasteria.com, tomas.bastante@soprasteria.com",
    url="https://github.com/TomasBastanteFlor/PGPT",
    project_urls=OrderedDict(
        (
            ("Code", "https://github.com/TomasBastanteFlor/PGPT"),
            ("Issue tracker", "https://github.com/TomasBastanteFlor/PGPT"),
        )
    ),
    license="MIT License",
    packages=["pentestgpt"] + find_packages(),
    # packages=find_packages(),
    # scripts=['pentestgpt/main.py'],
    install_requires=dependencies,
    entry_points={
        "console_scripts": [
            "pentestgpt=pentestgpt.main:main",
            "pentestgpt-cookie=pentestgpt.extract_cookie:main",
            "pentestgpt-connection=pentestgpt.test_connection:main",
        ]
    },
)
