🎓 Facial Attendance - Système de Gestion des Présences
🏥 Solution Intelligente de Suivi Etudiant par Reconnaissance Faciale

📘 Projet de Fin d'Études (PFE) - Licence Sciences et Techniques 


Ce projet est une application de bureau conçue en Python pour automatiser la gestion de la présence des étudiants. Elle remplace l'appel manuel traditionnel par une authentification biométrique sécurisée en temps réel, éliminant ainsi les fraudes et les erreurs de saisie.




✅ Fonctionnalités Principales
👤 Espace Étudiant
📝 Inscription Biométrique : Enregistrement des informations personnelles (CNE, Nom, Prénom, Email, Tel) avec capture automatique des caractéristiques faciales.



📸 Pointage Temps Réel : Marquage instantané de la présence par détection et identification du visage via la caméra.



👔 Espace Administration
🔐 Accès Sécurisé : Authentification par login pour les administrateurs.


👥 Gestion des Effectifs : Interface CRUD complète pour ajouter, modifier, supprimer ou rechercher des étudiants.


📊 Reporting Automatisé : Génération et consultation dynamique des listes de présence et d'absence avec horodatage.



🧱 Technologies et Outils Utilisés
🐍 Langage : Python 3.x (simple, polyvalent et puissant).





👁️ Vision par Ordinateur :


OpenCV : Traitement d'images et flux vidéo.


Dlib (HOG & ResNet-50) : Détection faciale et extraction de caractéristiques 128D.


🗄️ Base de Données : MySQL pour le stockage relationnel sécurisé des données.



💻 Interface Graphique (GUI) : Tkinter & CustomTkinter pour une interface utilisateur moderne.


📈 Traitement de Données : Pandas & NumPy.



⚙️ Architecture du Système
Le développement repose sur le modèle de cycle de vie en V, garantissant une structure rigoureuse. Le pipeline de reconnaissance faciale suit ces étapes clés :



Prétraitement : Conversion en niveaux de gris et réduction du bruit.



Détection (HOG) : Localisation du visage basée sur l'orientation des gradients.



Repères Faciaux : Identification de 68 points de repère (yeux, nez, bouche) pour aligner le visage.


Reconnaissance : Calcul de la distance euclidienne entre le visage capturé et les profils enregistrés dans le fichier CSV.



🚀 Installation et Utilisation
Prérequis
Python 3.10+

Serveur MySQL (ex: XAMPP) 

Étapes
Cloner le dépôt :

Bash

git clone https://github.com/votre-username/facial-attendance.git
Installer les bibliothèques nécessaires :

Bash

pip install opencv-python dlib numpy pandas mysql-connector-python customtkinter
``` [cite: 1210, 1230, 1264, 1285]
Configurer la base de données : Importer le schéma SQL et vérifier les identifiants dans Application.py.

Lancer l'application :

Bash

python Application.py



 



Institution : Faculté des Sciences et Techniques d'Al-Hoceima (FSTH)
