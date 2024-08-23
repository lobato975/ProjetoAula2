import pandas as pd

def analisarCampanha():
    #Ler o arquivo
    cli = pd.read_csv('./files/cliente.csv')
    cam = pd.read_csv('./files/campanha.csv')

    list_cli = cli.values.tolist()[0]
    list_cam = cam.values.tolist()[0]

    return list_cli == list_cam

print(analisarCampanha())