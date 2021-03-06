from distutils.core import setup
setup(
  name = 'AcademicEmailVerifier',
  packages = ['AcademicEmailVerifier'],
  include_package_data=True,
  package_data = {'': ['domains/*.txt','domains/*/*.txt','domains/*/*/*.txt','domains/*/*/*/*.txt']},
  version = '1.1',
  license='MIT',
  description = 'Identifies email addresses or domains names that belong to colleges or universities.',
  author = 'Yervand Galoyan',
  author_email = 'yervandgaloyan26@gmail.com',
  url = 'https://github.com/yervandgaloyan/AcademicEmailVerifier/',
  download_url = 'https://github.com/yervandgaloyan/AcademicEmailVerifier/archive/refs/tags/v_10.tar.gz',
  keywords = ['EMAIL', 'ACADEMIC', 'VERIFIER'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)