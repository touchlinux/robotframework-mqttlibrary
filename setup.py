from setuptools import setup

from os.path import abspath, dirname, join

here = dirname(abspath(__file__))
version_file = join(here, 'src', 'MQTTLibrary', 'version.py')


# Get version
exec(compile(open(version_file).read(), version_file, 'exec'))

# Get the long description
with open(join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name              = 'robotframework-mqttlibrary',
    version           = VERSION,
    description       = 'MQTT Keyword Library Robot Framework',
    long_description  = long_description,
    url               = 'https://github.com/randomsync/robotframework-mqttlibrary',
    author            = 'Gaurav Gupta',
    author_email      = 'gaurav@randomsync.net',
    license           = 'Apache License 2.0',
    classifiers       = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Testing',
    ],
    keywords          = 'robotframework testing testautomation mqtt',
    package_dir       = {'': 'src'},
    packages          = ['MQTTLibrary'],
    install_requires  = ['robotframework', 'paho-mqtt'],
)
