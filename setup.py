#!/usr/bin/env python3

from distutils.core import setup

setup(name='nbconvert_jekyll',
      description='Adds google analytics and YAML when converting a notebook',
      author='Louis Abraham',
      author_email='louis.abraham@yahoo.fr',
      license='MIT',
      packages=['nbconvert_jekyll'],
      package_data={'nbconvert_jekyll':['templates/*.tpl']},
      entry_points={
          'nbconvert.exporters': [
              'jekyll = nbconvert_jekyll:JekyllExporter'
          ],
      },
      )
