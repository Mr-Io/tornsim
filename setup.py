"""
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
import setuptools

# Get the long description from the README file
with open('README.rst') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setuptools.setup(
    name='torn_happy',  # Required. Use only non-capital characters.
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install packagename
    #+
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name

    version='0.0.0',  # Required.
    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    use_scm_version=True,               # with this the version is
    setup_requires=['setuptools_scm'],  # obtained from git
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    #
    # The preferred in the semantic versioning based on a MAJOR.MINOR.MAINTENANCE
    # MAJOR version when incompatible API changes are made,
    # MINOR version when new functionality is added with backward-compatible API,
    # MAINTENANCE version when bug are fixed with backward-compatible API.
    # Specifications here:
    # https://semver.org/


    description='happy vs energy in torn',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note)
    # description is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    #
    # long_description is an optional longer description of your project that represents
    # the body of text which users will see when they visit PyPI.
    # Often, this is the same as your README, so you can just read it in from
    # that file directly (as we have already done above)
    #
    # long_description_content_type corresponds to the "Description" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    # Denotes that our long_description is in Markdown; valid values are
    # text/plain, text/x-rst, and text/markdown
    # This is optional if long_description is written in reStructuredText (rst) but
    # required for plain-text or Markdown; if unspecified, "applications should
    # attempt to render [the long_description] as text/x-rst; charset=UTF-8 and
    # fall back to text/plain if it is not valid rst" (see link below)
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional

    url='https://github.com/pypa/happy_torn',  # Optional
    # This should be a valid link to your project's main homepage.
    #
    # This field corresponds to the "Home-Page" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#home-page-optional

    author='The Python Packaging Authority',  # Optional
    author_email='mrio.dev@gmail.com',  # Optional
    # This should be your name or the name of the organization which owns the project.
    # This should be a valid email address corresponding to the author listed above.

    packages=[],  # Required
    # You can just specify a list with all package and subpackages directories manually
    # or you can use find_packages() as bellow:
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # py_modules=["module1", "module2"],
    # If the project contain any singl-file python module that is not part of a package,
    # (you just want to distribute one or more single Python files) use
    # the `py_modules` argument instead as follows, which will expect two files
    # called `module1.py` and `module2.py` to exist:

    package_data={  # Optional
        # If ANY PACKAGE contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include the file data.dat of the package 'package' and all sql files:
        'package': ['data.dat', '*.sql'],
        # And include any *.dat files found in the 'data' subdirectory
        # of the subpackage 'subpackage':
        'package.supbpackage':['data/*.dat']
    },
    # package_data is a dictionary where the keys are packages names (as listed in
    # the `package` keyword and the values are lists of glob patterns of the data files.
    #
    # If there are data files included in your packages that need to be
    # installed, specify them here.

    #data_files=[('my_data', ['data/data_file'])],  # Optional
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    #
    # data_files specifies a list of tuples (directory, list of files) where:
    # directory = installation directory (relative path to sys.prefix/site.USER_BASE)
    # files = files to install there
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'

    #install_requires=['pkg_dep1', 'pkg_dep2'],  # Optional
    # This field lists other packages that your project minimally needs to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html

    python_requires='>=3.7',
    # Specify which Python versions you support. In contrast to the
    # 'Programming Language' classifiers above, 'pip install' will check this
    # and refuse to install the project if the version does not match. If you
    # do not support Python 2, you can simplify this to '>=3.5' or similar, see
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires

    #extras_require={  # Optional
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},
    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.

    entry_points={  # Optional
        'console_scripts': [
            # this would produce a command 'command1' with the `func1` logic
            # from module package.command_line
            'command1=package.command_line:func1',
            # this would produce a command 'command2' with the `func2` logic
            # from module package.command_line
            'command2=package.command_line:func2',
        ],
    },
    # Is is a good practice to use a command_line.py module for the only purpose to
    # define functions used as command line tools. Those functions must not have
    # arguments (instead they should use sys.argv -normal use- and sys.stdin -pipe use-) and
    # they must not have returns (instead they should use print()).
    #
    # To provide executable scripts, use entry points in preference to the
    # `scripts` keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/pypa/sampleproject/',
    },
    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.

    keywords='sample setuptools development',  # Optional
    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a string of words separated by whitespace, not a list.

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires'.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
)