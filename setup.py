from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="DXC-Industrialized-AI-Starter",
    version="1.1.0",
    description="Python library which is extensively used for all AI projects",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/dxc-technology/DXC-Industrialized-AI-Starter",
    #download_url = "https://github.com/dxc-technology/DXC-Industrialized-AI-Starter/releases/tag/v1.0.tar.gz",
    author="DXC",
    license="Apache License 2.0",
    platforms='any',
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["dxc"],
    include_package_data=True,
    install_requires=["JIRA","scikit-learn==0.22.2.post1","auto_ml","Algorithmia","gitpython","flatten_json","pyjanitor","ftfy","arrow",
                      "scrubadub","yellowbrick==1.1","datacleaner","missingno","pymongo","IPython","dnspython"],
    entry_points={
        "console_scripts": [
            "dxc=dxc.ai:main",
        ]
    },
)
