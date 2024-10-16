from setuptools import setup, find_packages
import pkg_resources

def get_installed_packages():
    """
    Get a list of installed packages and their versions.
    Returns a list of formatted strings that can be used in a setup.py dependencies list.
    """
    installed_packages = pkg_resources.working_set
    dependencies = []
    
    for package in installed_packages:
        package_name = package.key
        version = package.version
        dependencies.append(f"{package_name}=={version}")
    
    return dependencies

dependencies = get_installed_packages()
    



setup(
    name="LLMOps",  # The name of your package
    version="0.1.0",  # Initial version
    packages=find_packages(),  # Automatically find all the packages in the directory
    install_requires=dependencies,
    include_package_data=True,  # To include any non-Python files specified in MANIFEST.in
    description="A package for LLMOps related tasks",  # Short description
    author="keshav Kumar",  # Your name or the team's name
    author_email="keshavkmr076@gmail.com",  # Your contact email
    url="https://github.com/keshavkmr48/LLMOps",  # URL of the project repository
    classifiers=[
        "Programming Language :: Python :: 3",  # Specify Python versions supported
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',  # Python version compatibility
)
