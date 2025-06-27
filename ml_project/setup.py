from setuptools import setup, find_packages

setup(
    name='Kaggle Competition Project',
    version='0.1.0',
    author='Chandan Chaudhari',
    author_email='chaudhari.chandan22@example.com',
    description='Multivariate Analysis: Prediction Model',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chandanc5525/EnE_Kaggle_Competition_MLModel',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'xgboost',
        'joblib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
