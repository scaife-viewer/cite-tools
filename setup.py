from setuptools import find_packages, setup

dev_requires = [
    "black==19.10b0",
    "flake8>=3.7,<4",
    "flake8-quotes>=2.1.1,<3",
    "isort>=4.3.21,<5",
]

setup(
    author="Scaife Viewer Team",
    author_email="jtauber+scaife@jtauber.com",
    description="Python library for the CITE architecture",
    name="cite-tools",
    version="0.1a1",
    url="http://github.com/scaife-viewer/cite-tools/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "cite_tools": []
    },
    test_suite="runtests.runtests",
    install_requires=[
        "lxml>=4.5.2,<5",
    ],
    extras_require={
        "dev": dev_requires,
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)


