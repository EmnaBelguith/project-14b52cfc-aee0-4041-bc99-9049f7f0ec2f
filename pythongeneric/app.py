# app.py

# Ceci est une application WSGI (Web Server Gateway Interface) simple.
# Elle est conçue pour être servie par un serveur WSGI comme Gunicorn.

def application(environ, start_response):
    """
    Fonction principale de l'application WSGI.
    Elle prend deux arguments :
    - environ: un dictionnaire contenant les variables d'environnement WSGI.
    - start_response: une fonction callable pour envoyer le statut HTTP et les en-têtes.
    """
    status = '200 OK'  # Statut HTTP de la réponse
    headers = [('Content-type', 'text/plain')]  # En-têtes de la réponse

    # Appelle la fonction start_response pour envoyer le statut et les en-têtes
    start_response(status, headers)

    # Retourne le corps de la réponse sous forme de liste d'octets
    return [b"Bonjour depuis l'application web Python generique!"]

# Cette partie est pour le développement local et le test direct sans Gunicorn.
# Dans un environnement Docker, Gunicorn lancera la fonction 'application'.
if __name__ == '__main__':
    # Importe le serveur simple de wsgiref pour le test local
    from wsgiref.simple_server import make_server
    
    # Crée un serveur HTTP qui écoute sur toutes les interfaces (0.0.0.0) sur le port 8000
    # et sert notre fonction 'application'.
    httpd = make_server('0.0.0.0', 8000, application)
    print("Serveur WSGI générique démarré sur http://0.0.0.0:8000/")
    
    # Lance le serveur indéfiniment
    httpd.serve_forever()
