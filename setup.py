from setuptools import find_packages
from setuptools import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print "warning: pypandoc module not found, could not convert Markdown to RST"
    read_md = lambda f: open(f, 'r').read()

setup(
    name="gmaps-url-parser",
    version="0.1.0",
    description="parse google maps url",
    long_description=read_md('README.md'),
    author="Walid Saad",
    author_email="walid.sa3d@gmail.com",
    url="https://github.com/walidsa3d/gmaps-url-parser",
    packages=find_packages(),
    include_package_data=True,
    test_suite="tests",
    license="MIT",
    zip_safe=False,
    classifiers=[
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        #'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        # 'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        # 'Operating System :: POSIX',
        # 'Operating System :: MacOS',
        # 'Operating System :: Unix',
        # 'Operating System :: Windows',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
