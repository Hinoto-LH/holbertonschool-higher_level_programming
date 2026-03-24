Ce document explique :

### Comment se connecter a une base de donnees MySQL depuis un script Python

- Comment effectuer une requete SELECT dans une table MySQL depuis un script Python
- Comment effectuer une requete INSERT dans une table MySQL depuis un script Python
- Ce que signifie ORM
- Comment mapper une classe Python a une table MySQL

#### 1. Connexion a une base de donnees MySQL depuis Python

Pour se connecter a une base de donnees MySQL en Python, on peut utiliser le module mysql-connector-python.

Installation :

```bash
pip install mysql-connector-python
```

Exemple de connexion :

```
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="votre_utilisateur",
    password="votre_mot_de_passe",
    database="votre_base"
)

cursor = connection.cursor()
print("Connexion reussie")
```

Il est important de fermer la connexion apres utilisation :

```
cursor.close()
connection.close()
```

#### 2. Effectuer une requete SELECT

Pour recuperer des lignes depuis une table, on utilise la commande SELECT.

Exemple :

```
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="votre_utilisateur",
    password="votre_mot_de_passe",
    database="votre_base"
)

cursor = connection.cursor()

query = "SELECT id, nom FROM utilisateurs"
cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
connection.close()
```

La methode fetchall() permet de recuperer toutes les lignes du resultat.

#### 3. Effectuer une requete INSERT

Pour inserer des donnees dans une table, on utilise la commande INSERT.

Exemple :

```
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="votre_utilisateur",
    password="votre_mot_de_passe",
    database="votre_base"
)

cursor = connection.cursor()

query = "INSERT INTO utilisateurs (nom, age) VALUES (%s, %s)"
values = ("Alice", 25)

cursor.execute(query, values)
connection.commit()

print("Insertion reussie")

cursor.close()
connection.close()
```

La methode commit() est necessaire pour valider les modifications dans la base de donnees.

#### 4. Signification de ORM

ORM signifie Object Relational Mapping.

Un ORM est une technique qui permet de manipuler une base de donnees relationnelle en utilisant des objets Python au lieu d ecrire directement des requetes SQL.

L ORM fait le lien entre les tables de la base de donnees et les classes Python.

Exemples d ORM en Python :

- SQLAlchemy
- Django ORM

#### 5. Mapper une classe Python a une table MySQL

Avec un ORM comme SQLAlchemy, il est possible de representer une table par une classe.

Installation :

```bash
pip install sqlalchemy
```

Exemple :

```
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Utilisateur(Base):
    __tablename__ = "utilisateurs"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100))
    age = Column(Integer)

engine = create_engine("mysql+mysqlconnector://utilisateur:mot_de_passe@localhost/votre_base")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

nouvel_utilisateur = Utilisateur(nom="Bob", age=30)
session.add(nouvel_utilisateur)
session.commit()

session.close()
```

Dans cet exemple :

- La classe Utilisateur correspond a la table utilisateurs
- Chaque attribut correspond a une colonne
- L ORM genere automatiquement les requetes SQL necessaires

### Conclusion

Se connecter a MySQL avec Python peut se faire directement avec un connecteur SQL ou via un ORM.

Le connecteur permet d executer des requetes SQL manuellement.

Un ORM permet de manipuler les donnees de facon plus abstraite en utilisant des classes et des objets Python.
