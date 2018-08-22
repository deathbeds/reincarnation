def load_ipython_extension(ip):
    with __import__("importnb").Notebook():
        from . import extensions
