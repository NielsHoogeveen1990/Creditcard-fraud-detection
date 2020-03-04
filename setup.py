from setuptools import setup, find_packages

setup(
    name='anomaly_detection',
    keywords='',
    version='0.1',
    author='Niels Hoogeveen',
    packages=find_packages(exclude=['data', 'notebooks']),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'creditcard = anomaly_detection.cli:main']
    }
)


