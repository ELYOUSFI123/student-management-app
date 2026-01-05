🎓 Facial Attendance – Système de Gestion des Présences

🏥 Solution Intelligente de Suivi Étudiant par Reconnaissance Faciale

📘 Projet de Fin d'Études (PFE) – Licence Sciences et Techniques

Cette application de bureau développée en Python automatise la gestion des présences des étudiants. Elle remplace l’appel manuel traditionnel par une authentification biométrique en temps réel, éliminant ainsi les fraudes et les erreurs de saisie.

✅ Fonctionnalités Principales
👤 Espace Étudiant

📝 Inscription Biométrique : Enregistrement des informations personnelles (CNE, Nom, Prénom, Email, Tel) avec capture automatique des caractéristiques faciales.

📸 Pointage Temps Réel : Marquage instantané de la présence grâce à la détection et l’identification du visage via la caméra.

👔 Espace Administration

🔐 Accès Sécurisé : Authentification par login pour les administrateurs.

👥 Gestion des Étudiants : Interface CRUD complète pour ajouter, modifier, supprimer ou rechercher des étudiants.

📊 Reporting Automatisé : Génération dynamique des listes de présence et d’absence avec horodatage.

🧱 Technologies et Outils Utilisés

🐍 Langage : Python 3.x

👁️ Vision par Ordinateur :

OpenCV : traitement d’images et flux vidéo

Dlib (HOG & ResNet-50) : détection faciale et extraction de caractéristiques 128D

🗄️ Base de Données : MySQL (stockage relationnel sécurisé)

💻 Interface Graphique (GUI) : Tkinter & CustomTkinter

📈 Traitement de Données : Pandas & NumPy

⚙️ Architecture du Système

Le système est développé selon le modèle de cycle de vie en V, garantissant une structure rigoureuse.

Pipeline de Reconnaissance Faciale :

Prétraitement : Conversion en niveaux de gris et réduction du bruit.

Détection (HOG) : Localisation du visage basée sur l’orientation des gradients.

Repères Faciaux : Identification de 68 points de repère (yeux, nez, bouche) pour aligner le visage.

Reconnaissance : Calcul de la distance euclidienne entre le visage capturé et les profils enregistrés dans le fichier CSV.

🚀 Installation et Utilisation
Prérequis

Python 3.10+

Serveur MySQL (ex : XAMPP)

Étapes

Cloner le dépôt :

git clone https://github.com/votre-username/facial-attendance.git


Installer les bibliothèques nécessaires :

pip install opencv-python dlib numpy pandas mysql-connector-python customtkinter


Configurer la base de données :

Importer le schéma SQL fourni

Vérifier les identifiants dans Application.py

Lancer l’application :

python Application.py

✅ Conclusion

Ce projet démontre l’importance des technologies de reconnaissance faciale appliquées à la gestion des présences, en offrant :

Une solution sécurisée et fiable pour le suivi des étudiants

Une interface utilisateur intuitive et moderne

Une gestion complète des données avec reporting automatique

Une application évolutive et modulable pour tout établissement éducatif
