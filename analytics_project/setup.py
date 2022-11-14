from setuptools import find_packages, setup

setup(
    name="analytics_project",
    packages=find_packages(exclude=["analytics_project_tests"]),
    install_requires=[
        "dagster",
        "pandas"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
