# SQL - More queries
## General

Ce projet couvre des concepts SQL avancés en utilisant MySQL.

### Comment créer un nouvel utilisateur MySQL

Pour creer un nouvel utilisateur dans MySQL :

```SQL
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
```

Pour autoriser la connexion depuis n'importe quelle machine :

```SQL
CREATE USER 'username'@'%' IDENTIFIED BY 'password';
```

#### Comment gérer les privilèges pour un utilisateur sur une base ou une table

Donner tous les privilèges sur une base :

```SQL
GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';
```

Donner des privilèges sur une table spécifique :

```SQL
GRANT SELECT, INSERT ON database_name.table_name TO 'username'@'localhost';
```

Appliquer les changements :

```SQL
FLUSH PRIVILEGES;
```

Retirer des privileges :

```SQL
REVOKE privilege_type ON database_name.table_name FROM 'username'@'localhost';
```

### Qu'est ce qu'une PRIMARY KEY
Une PRIMARY KEY :

- Identifie de maniere unique chaque - enregistrement
- Ne peut pas etre NULL
- Doit etre unique
- Il ne peut y avoir qu une seule primary key par table

Exemple :

```SQL
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
```

### Qu'est ce qu'une **FOREIGN KEY**

Une **FOREIGN KEY** :

- Lie une table a une autre
- Reference la PRIMARY KEY d une autre table
- Assure l integrite referentielle

Exemple :

```SQL
CREATE TABLE orders (
    id INT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

**Comment utiliser les contraintes NOT NULL et UNIQUE**

NOT NULL :

Empoche une colonne de contenir des valeurs NULL.

```SQL
name VARCHAR(100) NOT NULL
```

UNIQUE :

Garantit que toutes les valeurs d'une colonne sont differentes.

```SQL
email VARCHAR(100) UNIQUE
```

#### Comment récupérer des données depuis plusieurs tables en une seule requete

On peut utiliser JOIN :

```SQL
SELECT users.name, orders.id
FROM users
JOIN orders ON users.id = orders.user_id;
```

#### Que sont les sous requetes

Une sous requete est une requete a l interieur d une autre requete.

Exemple :

```SQL
SELECT name
FROM users
WHERE id IN (
    SELECT user_id
    FROM orders
);
```

Les sous requètes peuvent être utilisées dans SELECT, FROM ou WHERE.

#### Que sont JOIN et UNION

JOIN :

Combine les lignes de deux ou plusieurs tables selon une colonne en commun.

Types de JOIN :

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN

Exemple :

```SQL
SELECT users.name, orders.id
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

UNION :

Combine les résultats de deux requêtes SELECT.

Règles :

- Même nombre de colonnes
- Types de données compatibles

Exemple :

```SQL
SELECT name FROM students
UNION
SELECT name FROM teachers;
```

**UNION** supprime les doublons.
Utiliser **UNION ALL** pour conserver les doublons.
