import setuptools

# In python < 2.7.4, a lazy loading of package `pbr` will break
# setuptools if some other modules registered functions in `atexit`.
# solution from: http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing  # noqa # pylint:disable=unused-import
except ImportError:
    pass

setuptools.setup(
    setup_requires=['pbr>=2.0.0'],
    pbr=True)
