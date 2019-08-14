# Pandas ecosystem

Increasingly, packages are being built on top of pandas to address specific needs
in data preparation, analysis and visualization.
This is encouraging because it means pandas is not only helping users to handle
their data tasks but also that it provides a better starting point for developers to
build powerful and more focused data tools.
The creation of libraries that complement pandas' functionality also allows pandas
development to remain focused around it's original requirements.

This is an inexhaustive list of projects that build on pandas in order to provide
tools in the PyData space. For a list of projects that depend on pandas,
see the
[libraries.io usage page for pandas](https://libraries.io/pypi/pandas/usage)
or [search pypi for pandas](https://pypi.org/search/?q=pandas).

We'd like to make it easier for users to find these projects, if you know of other
substantial projects that you feel should be on this list, please let us know.


## Statistics and machine learning
-------------------------------

### [Statsmodels](https://www.statsmodels.org/)

Statsmodels is the prominent Python "statistics and econometrics library" and it has
a long-standing special relationship with pandas. Statsmodels provides powerful statistics,
econometrics, analysis and modeling functionality that is out of pandas' scope.
Statsmodels leverages pandas objects as the underlying data container for computation.

### [sklearn-pandas](https://github.com/paulgb/sklearn-pandas)

Use pandas DataFrames in your [scikit-learn](https://scikit-learn.org/)

### Ray

```python
# import pandas as pd
import ray.dataframe as pd
```
