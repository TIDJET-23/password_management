# Gestionnaire de Mots de Passe Sécurisé

Ce programme est un gestionnaire de mots de passe simple et sécurisé utilisant le chiffrement RSA pour protéger vos données.

## Prérequis

- Python 3.x
- OpenSSL

## Installation

2. Générez vos clés RSA en utilisant OpenSSL :

```
openssl genrsa -out private_key_pass_management.pem 2048
openssl rsa -in private_key_pass_management.pem -pubout -out public_key_pass_management.pem
```

3. Placez les fichiers `private_key_pass_management.pem` et `public_key_pass_management.pem` dans le même répertoire que `pass_management.py`.

## Utilisation

1. Ouvrez un terminal et naviguez vers le répertoire contenant le script.

2. Lancez le programme avec la commande :

```
python3 pass_management.py
```

3. Utilisez le menu pour :
- Ajouter des mots de passe
- Afficher les mots de passe enregistrés
- Supprimer des mots de passe
- Quitter le programme

## Fonctionnalités

- Chiffrement RSA pour sécuriser les mots de passe
- Interface en ligne de commande simple et intuitive
- Options pour ajouter, afficher et supprimer des mots de passe
- Nettoyage de l'écran pour une meilleure lisibilité

## Sécurité

- Gardez votre fichier en lieu sûr. Ne le partagez jamais.
- Le fichier contenant les mots de passe chiffrés (`pass_management.bin`) peut être stocké en toute sécurité, car il est chiffré.

## Avertissement

Ce programme est conçu à des fins éducatives et pour une utilisation personnelle. 
