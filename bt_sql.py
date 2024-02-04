import sqlite3

def getAll():
    '''
    Input : None

    Output : res : list of k-tuple

    Return all songs and their informations from DB
    '''
    conn = sqlite3.connect("music.db")
    c = conn.cursor()
    
    #TODO : Récupérer toutes les chansons de la base
    # ...
    # ...


    conn.close()
    return res

def getDateOverd(d):
    '''
    Input : d : string (date)
    MUST BE FORMATED : 'yyyy-mm-dd'

    Output : res : list of k-tuple

    Return all songs and their informations with 'datet > d' from DB
    '''
    conn = sqlite3.connect("music.db")
    c = conn.cursor()

    #TODO : Récupérer toutes les chansons de la base
    # SI la date est supérieure à celle donnée en paramètre (d)
    # ...
    # ...

    conn.close()
    return res

def getType(t):
    '''
    Input : t : string (song type)

    Output : res : list of k-tuple

    Return all songs and their informations with 'songType.label = t' from DB

    Return None if t doesn't exist in DB 
    '''
    conn = sqlite3.connect("music.db")
    c = conn.cursor()

    #TODO : Récupérer toutes les chansons de la base
    # SI le type correspond à celui donné en argument
    # ...
    # ...

    conn.close()
    return res

def create_score(s, u=None):
    '''
    Input : 
        s : int (score)
        u : int (user id)

    Output : res : idScore 

    Create score for current game and return id of the row
    '''
    conn = sqlite3.connect("music.db")
    c = conn.cursor()


    #TODO : Insérer le score dans la base.
    # Si l'utilisateur est enregistré, on associe les données à cet utilisateur
    # Sinon on insère juste le score
    # ...
    # ...
    # ...
    # ...
    # ...
    # ...

    conn.close()
    return res

def update_score(s, u=None):
    '''
    Input : 
        s : (int int) tuple (idScore, value)
        u : int (user id)

    Output : None
    
    Update current score of user
    '''
    conn = sqlite3.connect("music.db")
    c = conn.cursor()

    #TODO : Mettre à jour le score dans la base en fonction d'un identifiant donné.
    # ...
    conn.close()
