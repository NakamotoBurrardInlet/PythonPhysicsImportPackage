from setuptools import setup, find_packages

setup(
    name="Phys_Eval_Sol",
    version="1.0.0",
    author="EricMMichael",
    description="An advanced computational physics evaluation suite.",
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'numpy>=1.20.0',
    ],
)