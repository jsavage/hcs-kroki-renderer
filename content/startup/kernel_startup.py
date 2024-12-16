def load_ipython_extension(ipython):
    import sys
    sys.path.append('/home/jovyan/content/startup')
    from hcs_magic import hcs
