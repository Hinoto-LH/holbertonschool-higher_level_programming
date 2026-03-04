# Fondamentaux SQL - README
## Introduction

Ce projet couvre les concepts fondamentaux des bases de donnees et du SQL, en mettant l'accent sur les bases de donnees relationnelles et MySQL. Il inclut la theorie et l'utilisation pratique des principales commandes SQL.

### Qu'est-ce qu'une base de donnees ?

Une base de donnees est une collection organisee d'informations structurees stockees de maniere electronique.

Elle permet de stocker, recuperer, modifier et gerer efficacement des donnees.

Les bases de donnees sont utilisees dans presque toutes les applications : sites web, systemes bancaires, applications mobiles, etc.

### Qu'est-ce qu'une base de donnees relationnelle ?

Une base de donnees relationnelle stocke les donnees dans des tables composees de lignes et de colonnes.

Chaque table represente une entite.

Chaque ligne represente un enregistrement.

Chaque colonne represente un attribut.

Les tables peuvent etre reliees entre elles grace aux relations, generalement via des cles primaires et etrangeres.

Exemples de systemes de bases relationnelles :

- MySQL
- PostgreSQL
- Oracle
- SQL Server

### Que signifie SQL ?

SQL signifie Structured Query Language (Langage de Requete Structure).

C'est un langage standard utilise pour communiquer avec les bases de donnees relationnelles.

### Qu'est-ce que MySQL ?

MySQL est un systeme de gestion de base de donnees relationnelle open source (RDBMS).

Il utilise SQL pour gerer les donnees et est tres utilise dans le developpement web et les systemes en production.

### Comment creer une base de donnees dans MySQL

Pour creer une base de donnees :

```SQL
CREATE DATABASE nom_de_la_base;
```

Pour utiliser une base de donnees :

```SQL
USE nom_de_la_base;
```

#### Que signifient DDL et DML ?

DDL - Data Definition Language
Langage de definition des donnees.

Il sert a definir ou modifier la structure de la base de donnees.

Exemples :

- CREATE
- ALTER
- DROP
- TRUNCATE

DML - Data Manipulation Language
Langage de manipulation des donnees.

Il sert a gerer les donnees contenues dans les tables.

Exemples :

- SELECT
- INSERT
- UPDATE
- DELETE

##### Comment CREATE ou ALTER une table

Creer une table :

```SQL
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100)
);
```

Modifier une table :

```SQL
ALTER TABLE users
ADD age INT;
```

#### Comment SELECT des donnees depuis une table

Recuperer tous les enregistrements :

```SQL
SELECT * FROM users;
```

Recuperer certaines colonnes :

```SQL
SELECT name, email FROM users;
```

Avec une condition :

```SQL
SELECT * FROM users
WHERE age > 18;
```

#### Comment INSERT, UPDATE ou DELETE des donnees

Inserer des donnees :

```SQL
INSERT INTO users (name, email)
VALUES ('John Doe', 'john@example.com');
```

Mettre a jour des donnees :

```SQL
UPDATE users
SET name = 'Jane Doe'
WHERE id = 1;
```

Supprimer des donnees :

```SQL
DELETE FROM users
WHERE id = 1;
```

##### Qu'est-ce qu'une sous-requete ?

Une sous-requete est une requete imbriquee dans une autre requete.

Exemple :

```SQL
SELECT name
FROM users
WHERE id IN (
    SELECT user_id
    FROM orders
);
```

Les sous-requetes permettent de filtrer ou calculer des resultats dynamiquement.

#### Comment utiliser les fonctions MySQL

MySQL propose des fonctions integrees pour effectuer des calculs ou manipuler les donnees.

Fonctions d'agregation :

```SQL
SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users;
```

Fonctions sur les chaines de caracteres :

```SQL
SELECT UPPER(name) FROM users;
```

Fonctions de date :

```SQL
SELECT NOW();
```
```SQL
DESCRIBE -- : Pour l'humain (clair et lisible).
```

```SQL
SHOW CREATE TABLE -- : Pour la machine (complet et technique).
```

### Conclusion

Comprendre les bases de donnees et SQL est essentiel pour le developpement backend, l'analyse de donnees et l'ingenierie logicielle.

Maitriser :

- La structure des bases de donnees
- Les requetes SQL
- La manipulation des donnees
- Les sous-requetes
- Les fonctions integrees

est indispensable pour construire des systemes fiables et evolutifs.
