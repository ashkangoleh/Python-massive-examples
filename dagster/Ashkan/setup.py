from setuptools import find_packages, setup

setup(
    name="Ashkan",
    packages=find_packages(exclude=["Ashkan_tests"]),
    install_requires=[
        "dagster",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
