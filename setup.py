from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='fio-mbxgl',
      version='0.1.0',
      description=u"Preview GeoJSON with Mapbox GL JS",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Damon Burgett",
      author_email='nomad.damon@gmail.com',
      url='https://github.com/dnomadb/fio-mbxgl',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click', 'cligj>=0.5', 'flask', 'Fiona'
      ],
      extras_require={
          'test': ['pytest', 'black'],
      },
      entry_points="""
      [fiona.fio_commands]
      mbxgl=fio_mbxgl.scripts.cli:cli
      """
      )
