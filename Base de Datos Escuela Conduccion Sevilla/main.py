from Packages.Login import login
from Packages.SeleccionarEscuela import seleccionarEscuela


def main():
    nombreSecretaria = login()
    seleccionarEscuela( nombreSecretaria )

main()