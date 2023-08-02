try:
    import MySQLdb
    print("MySQLdb est présent et installé.")
except ImportError:
    print("MySQLdb n'est pas installé.")
