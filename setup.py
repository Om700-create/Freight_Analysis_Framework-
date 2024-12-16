from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    Reads requirements file and returns a list of requirements,
    excluding '-e .'.
    '''
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='freight_analysis_project',
    version='0.1.0',
    author='Omkar',
    author_email='om.data07@gmail.com',
    description='A package for predicting stroke occurrences using advanced machine learning techniques.',
    url='https://github.com/yourusername/freight_analysis_project',
    license='MIT',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)