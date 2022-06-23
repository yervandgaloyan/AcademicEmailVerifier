from distutils.core import setup
setup(
  name = 'AcademicEmailVerifier',
  packages = ['AcademicEmailVerifier'],
  version = '0.1',
  license='Apache',
  description = 'Identifies email addresses or domains names that belong to colleges or universities.',
  author = 'Yervand Galoyan',
  author_email = 'yervandgaloyan26@gmail.com',
  url = 'https://github.com/yervandgaloyan/AcademicEmailVerifier/',
  download_url = 'https://github.com/yervandgaloyan/AcademicEmailVerifier/archive/refs/tags/v_01.tar.gz',
  keywords = ['EMAIL', 'ACADEMIC', 'VERIFIER'],
  install_requires=[
          're',
          'os',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)