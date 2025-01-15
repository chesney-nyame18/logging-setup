import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="logging_setup",
    version="0.0.4",
    author="Chesney Nyame",
    author_email="ches_tech_cloud@outlook.com",
    description="Package to standardise logging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chesney-nyame18/logging-setup",
    packages=setuptools.find_packages(),
    install_requires=[
          'json_log_formatter',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Proprietary",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)