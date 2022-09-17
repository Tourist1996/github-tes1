from setuptools import setup, find_namespace_packages

setup(name='useful',
      version='1',
      description='clean and sort folders',
      url='https://github.com/Tourist1996/github-tes1',
      author='Bohdan Yolkin',
      author_email='Tourist1996@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires=['markdown'],
      entry_points={'console_scripts': ['clean-folder=clean_folder.sort:main']}
      )
