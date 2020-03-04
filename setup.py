from setuptools import setup, find_packages

base_packages = [
    "numpy>=1.15.4",
    "scipy>=1.2.0",
    "pandas==0.24.2",
    "tqdm==4.32.2",
    "click==7.0",
    "click-pathlib==2019.6.13.1"
]


setup(
    name='anomaly_detection',
    keywords='',
    version='0.1',
    author='Niels Hoogeveen',
    packages=find_packages(exclude=['data', 'notebooks']),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'run=anomaly_detection.models.models_utils:run',
        ]
    }
)