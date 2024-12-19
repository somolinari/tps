def descomponer_email(email):
    partes = email.split('@')
    if len(partes) != 2:
        return ()
    
    usuario, dominio = partes
    dominio_partes = dominio.split('.')
    
    if len(dominio_partes) < 2:
        return ()
    
    return (usuario,) + tuple(dominio_partes)

def main ():
    email = "alguien@uade.edu.ar"
    print(descomponer_email(email))
if __name__ == "__main__":
    main()