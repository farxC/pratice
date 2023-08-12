try:
    from mysql import connector
except ModuleNotFoundError:
    print('My SQL connector não instalado!')
else: 
    print('MySQL connector instalado e pronto!')

