from setuptools import setup, find_packages


def get_requirements(filename):
    
    requirements = []
    with open(filename, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        if "-e ." in requirements:
            requirements.remove("-e .")
            
    return requirements



setup(
    name="MLProject",
    version="0.0.1",
    author="Parthiv Akilesh",
    author_email="parthivakileshas@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)