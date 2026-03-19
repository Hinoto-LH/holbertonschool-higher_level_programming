# JavaScript — Guide de référence

## Pourquoi JavaScript est incroyable

JavaScript est l'un des langages de programmation les plus populaires au monde, et pour de bonnes raisons :

- **Universel** : il tourne dans le navigateur ET côté serveur (Node.js)
- **Polyvalent** : web, mobile, API, scripts, jeux, IA…
- **Dynamique** : pas besoin de compilation, le code s'exécute directement
- **Écosystème immense** : npm compte plus d'un million de paquets
- **Communauté active** : documentation abondante, support facile à trouver
- **Asynchrone par nature** : gestion fluide des événements et des requêtes réseau

---

## Exécuter un script JavaScript

### Dans le navigateur
Ouvrez la console développeur (`F12`) et tapez votre code directement.

### Avec Node.js
```bash
node mon_script.js
```

---

## Variables et constantes

```javascript
var   age = 25;       // ancienne syntaxe
let   nom = "Alice";  // variable réassignable
const PI  = 3.14159;  // constante (non réassignable)
```

---

## Différences entre `var`, `let` et `const`

| Caractéristique     | `var`         | `let`         | `const`       |
|---------------------|---------------|---------------|---------------|
| Portée              | fonction      | bloc `{}`     | bloc `{}`     |
| Réassignable        | ✅            | ✅            | ❌            |
| Hoisting            | ✅ (undefined)| ✅ (TDZ)      | ✅ (TDZ)      |
| Redéclarable        | ✅            | ❌            | ❌            |

> **Bonne pratique** : utilisez `const` par défaut, `let` si la valeur doit changer, et évitez `var`.

---

## Types de données

JavaScript possède 8 types de données :

```javascript
// Primitifs
let chaine    = "Bonjour";          // String
let nombre    = 42;                 // Number
let grand     = 9007199254740991n;  // BigInt
let booleen   = true;               // Boolean
let indefini  = undefined;          // Undefined
let nul       = null;               // Null
let symbole   = Symbol("id");       // Symbol

// Non-primitif
let objet     = { nom: "Alice" };   // Object (inclut Array, Function, etc.)
```

---

## Instructions `if` et `if...else`

```javascript
const score = 75;

// if simple
if (score >= 50) {
  console.log("Réussi");
}

// if...else
if (score >= 90) {
  console.log("Excellent");
} else if (score >= 50) {
  console.log("Bien");
} else {
  console.log("Insuffisant");
}
```

---

## Commentaires

```javascript
// Commentaire sur une seule ligne

/*
  Commentaire
  sur plusieurs lignes
*/

/**
 * Commentaire JSDoc (documentation)
 * @param {string} nom - Le nom de l'utilisateur
 */
```

---

## Affecter des valeurs à des variables

```javascript
let x = 10;        // affectation initiale
x = 20;            // réaffectation

let a, b, c;
a = b = c = 0;     // affectation en chaîne

// Affectation par déstructuration
let [premier, second] = [1, 2];
let { nom, age } = { nom: "Alice", age: 30 };
```

---

## Boucles `while` et `for`

### Boucle `while`
```javascript
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}
```

### Boucle `for`
```javascript
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

### Boucle `for...of` (tableaux)
```javascript
const fruits = ["pomme", "banane", "cerise"];
for (const fruit of fruits) {
  console.log(fruit);
}
```

### Boucle `for...in` (objets)
```javascript
const personne = { nom: "Alice", age: 30 };
for (const cle in personne) {
  console.log(cle, personne[cle]);
}
```

---

## Instructions `break` et `continue`

```javascript
// break — interrompt la boucle
for (let i = 0; i < 10; i++) {
  if (i === 5) break;
  console.log(i); // affiche 0 à 4
}

// continue — passe à l'itération suivante
for (let i = 0; i < 10; i++) {
  if (i % 2 === 0) continue;
  console.log(i); // affiche uniquement les nombres impairs
}
```

---

## Fonctions

```javascript
// Déclaration de fonction
function additionner(a, b) {
  return a + b;
}

// Expression de fonction
const multiplier = function(a, b) {
  return a * b;
};

// Fonction fléchée
const diviser = (a, b) => a / b;

// Appel
console.log(additionner(3, 4));  // 7
console.log(multiplier(3, 4));   // 12
console.log(diviser(10, 2));     // 5
```

---

## Valeur de retour sans `return`

Une fonction sans instruction `return` retourne automatiquement `undefined`.

```javascript
function direBonjour() {
  console.log("Bonjour !");
  // pas de return
}

const resultat = direBonjour();
console.log(resultat); // undefined
```

---

## Portée des variables (Scope)

```javascript
let global = "je suis global";

function maFonction() {
  let local = "je suis local";
  console.log(global); // ✅ accessible
  console.log(local);  // ✅ accessible

  if (true) {
    let bloc = "je suis dans un bloc";
    console.log(bloc); // ✅ accessible
  }
  // console.log(bloc); // ❌ ReferenceError
}

// console.log(local); // ❌ ReferenceError
```

---

## Opérateurs arithmétiques

```javascript
let a = 10, b = 3;

console.log(a + b);   // 13  — addition
console.log(a - b);   // 7   — soustraction
console.log(a * b);   // 30  — multiplication
console.log(a / b);   // 3.3 — division
console.log(a % b);   // 1   — modulo (reste)
console.log(a ** b);  // 1000 — exponentiation

// Opérateurs d'affectation combinés
a += 5;  // a = a + 5
a -= 2;  // a = a - 2
a *= 3;  // a = a * 3
a /= 4;  // a = a / 4
a++;     // incrémentation
a--;     // décrémentation
```

---

## Manipuler un objet (dictionnaire)

En JavaScript, les objets jouent le rôle de dictionnaires.

```javascript
// Créer un objet
const personne = {
  nom: "Alice",
  age: 30,
  ville: "Paris"
};

// Lire une valeur
console.log(personne.nom);         // Alice
console.log(personne["age"]);      // 30

// Ajouter / modifier
personne.email = "alice@example.com";
personne.age = 31;

// Supprimer
delete personne.ville;

// Vérifier l'existence d'une clé
console.log("nom" in personne);           // true
console.log(personne.hasOwnProperty("email")); // true

// Itérer sur les clés
for (const cle in personne) {
  console.log(`${cle}: ${personne[cle]}`);
}

// Méthodes utiles
console.log(Object.keys(personne));    // ["nom", "age", "email"]
console.log(Object.values(personne));  // ["Alice", 31, "alice@example.com"]
console.log(Object.entries(personne)); // [["nom", "Alice"], ...]
```

---

## Importer un fichier

### CommonJS (Node.js)
```javascript
// Exporter
// utils.js
const additionner = (a, b) => a + b;
module.exports = { additionner };

// Importer
const { additionner } = require('./utils');
console.log(additionner(2, 3)); // 5
```

### ES Modules (modern)
```javascript
// Exporter
// utils.js
export const additionner = (a, b) => a + b;
export default function direBonjour() {
  console.log("Bonjour !");
}

// Importer
import direBonjour, { additionner } from './utils.js';
direBonjour();
console.log(additionner(2, 3)); // 5
```

> Pour utiliser les ES Modules avec Node.js, nommez vos fichiers `.mjs` ou ajoutez `"type": "module"` dans votre `package.json`.

---

## Auteur

Projet réalisé dans le cadre d'un apprentissage JavaScript.
