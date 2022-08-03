import setuptools
  
with open("README.md", "r") as fh:
    description = fh.read()
  
setuptools.setup(
    name="robloxFunctions",
    version="1.0.0",
    author="PandaGamerYT",
    author_email="zachgameryt08@gmail.com",
    packages=["basicModules"],
    description="A python package gives basic modules.",
    long_description=description,
    long_description_content_type="text/markdown",
    license='MIT',
    python_requires='>=3.8',
    install_requires=['urllib', 'requests']
)
