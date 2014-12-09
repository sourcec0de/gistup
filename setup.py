from distutils.core import setup

desc = ('A command line utility for publishing a directory and '
        'updating gists on your github account.')

setup(name='gist-up',
      packages=['gist-up'],
      version='0.2',
      description=desc,
      author='James R. Qualls',
      author_email='qualls.james@gmail.com',
      url='https://github.com/sourcec0de/gistup',
      download_url='https://github.com/sourcec0de/gistup/tarball/0.1',
      keywords=['gist', 'blogging', 'command line', 'github', 'publish'],
      scripts=['bin/gistup'],
      classifiers=[])
