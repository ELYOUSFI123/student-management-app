# 🎓 FACIAL ATTENDANCE – SYSTÈME DE GESTION DES PRÉSENCES  

🏥 **Solution Intelligente de Suivi Étudiant par Reconnaissance Faciale**  
📘 **Projet de Fin d'Études (PFE) – Licence Sciences et Techniques**  

Cette application de bureau développée en **Python** automatise la gestion des présences des étudiants. Elle remplace l’appel manuel par une **authentification biométrique en temps réel**, éliminant fraudes et erreurs de saisie.  

---

## ✅ FONCTIONNALITÉS PRINCIPALES  

### 👤 ESPACE ÉTUDIANT
- 📝 **Inscription Biométrique** : Enregistrement des informations personnelles (CNE, Nom, Prénom, Email, Tel) avec capture automatique des caractéristiques faciales.  
- 📸 **Pointage Temps Réel** : Marquage instantané de la présence grâce à la détection et à l’identification du visage via la caméra.  

### 👔 ESPACE ADMINISTRATION
- 🔐 **Accès Sécurisé** : Authentification par login pour les administrateurs.  
- 👥 **Gestion des Étudiants** : Interface CRUD complète pour ajouter, modifier, supprimer ou rechercher des étudiants.  
- 📊 **Reporting Automatisé** : Génération dynamique des listes de présence et d’absence avec horodatage.  

---

## 🧱 TECHNOLOGIES ET OUTILS UTILISÉS

- 🐍 **Langage** : Python 3.x  
- 👁️ **Vision par Ordinateur** :  
  - OpenCV : traitement d’images et flux vidéo  
  - Dlib (HOG & ResNet-50) : détection faciale et extraction de caractéristiques 128D  
- 🗄️ **Base de Données** : MySQL (stockage relationnel sécurisé)  
- 💻 **Interface Graphique (GUI)** : Tkinter & CustomTkinter  
- 📈 **Traitement de Données** : Pandas & NumPy  

---

## ⚙️ ARCHITECTURE DU SYSTÈME

Le système est développé selon le **modèle de cycle de vie en V**, garantissant une structure rigoureuse.  

### 🔹 Pipeline de Reconnaissance Faciale :
1. **Prétraitement** : Conversion en niveaux de gris et réduction du bruit.  
2. **Détection (HOG)** : Localisation du visage basée sur l’orientation des gradients.  
3. **Repères Faciaux** : Identification de 68 points de repère (yeux, nez, bouche) pour aligner le visage.  
4. **Reconnaissance** : Calcul de la distance euclidienne entre le visage capturé et les profils enregistrés dans le fichier CSV.  

---



