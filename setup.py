from setuptools import setup

setup(name='pypework',
      version='0.7',
      description='Functional pipeline library for Python',
      url='http://github.com/andybrice/pypework',
      author='Andy Brice',
      author_email='andybrice@users.noreply.github.com',
      license='MIT',
      packages=['pypework'],
      zip_safe=False,
      long_description=
      """
      A library to add a neat, readable, functional pipeline syntax to Python.

      It allows you to rewrite messy nested function calls such as this:

      .. code:: python

         title_sanitized =
           replace(replace(replace(lowercase("Lorem Ipsum Dolor 2018/02/18"), " ", "_"), "/", "-"), "@", "at")

         title_sanitized # -> "lorem_ipsum_dolor_2018-02-18"

      In a far more readable format like this:

      .. code:: python

         title_sanitized = (
           "Lorem Ipsum Dolor 2018/02/18"
             >> f.lowercase
             >> f.replace("/", "-")
             >> f.replace(" ", "_")
             >> f.replace("@", "at")
         )

         title_sanitized # -> "lorem_ipsum_dolor_2018-02-18"
      """
      )
