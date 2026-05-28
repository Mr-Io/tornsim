README.rst
==========

**The Readme should be the single most important document in your codebase,
writing it first is the proper thing to do.**

It must contain:

    * title
    * screenshots logo/demo etc..
    * shields (status bars (travis), code style, tech/framework used, license, version, test coverage...)
    * what the project is about
    * motivation, why the project exist
    * why the project stand out
    * code example showing how the project solves a problem
    * hot wo configure and install it
    * api reference
    * how to contribute to it and credits

Template:

.. code-block:: rest

    Package: A brief description
    ============================
    .. ini-badges

    |generic shield| |Version| |License| |Contributors| |Coverage|

    .. |generic shield| image:: https://img.shields.io/badge/<leftname>-<rigthname>-<rightcolor>.svg
        :target: <url>

    .. |Version| image:: https://img.shields.io/pypi/v/:packageName.svg
        :target: https://pypi.org/project/:packageName/

    .. |License| image:: https://img.shields.io/github/license/:user/:repo.svg
        :target: https://pypi.org/project/:packageName/

    .. |Python| image:: https://img.shields.io/pypi/pyversions/:packageName.svg
        :target: https://pypi.org/project/:packageName/

    .. |Contributors| image:: https://img.shields.io/github/:which(contributors|contributors-anon)/:user/:repo.svg
        :target: https://pypi.org/project/:packageName/

    .. |Coverage| image:: https://codecov.io/gh/:user/:repo/branch/master/graph/badge.svg?token=:token
      :target: https://codecov.io/gh/:user/:repo

    .. end-badges

    1-2 paragraph descrition.

    **1 paragraph in bold with an important Hyperlink_**


    Installation
    ------------
    The source code can be downloaded from GitHub, where the code is `always available`_.
    It can also be installed from PyPI running::

        $ pip install packagename


    Usage
    -----
    Description


    Documentation
    -------------
    An extensive documentation of the project is available at `documentation_web`_.


    How to contribute
    -----------------
    Description



    .. _`always available`: https://github.com/:user/:repo.git
    .. _Hyperlink: <url>
    .. _`documentation_web`: <url>
