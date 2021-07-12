from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive 


from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
# Create local webserver and auto handles authentication.
gauth.LocalWebserverAuth()