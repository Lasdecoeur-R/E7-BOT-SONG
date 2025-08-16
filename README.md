# E7_Bot_Song - Bot Epic Seven - Mode Surfer sur Rythme

## 🎥 Vidéo de Présentation

[![Vidéo de présentation du bot](https://youtu.be/aPjyCsduU8I)

*Cliquez sur l'image pour voir la vidéo de démonstration*

---

## ✅ Version Française

Bot Epic Seven – Mode Surfer sur Rythme

Ce bot permet d'automatiser le mini-jeu Surfer sur Rythme dans Epic Seven afin d'obtenir toutes les récompenses et Pierres d'Azur facilement.

### 🎯 Prérequis

- Windows uniquement
- Packbot (dépôt Git)
- Bluestacks
- Epic Seven installé dans Bluestacks

### ⚙️ Installation

1. **Télécharger Packbot** puis décompressez-le.
2. **Exécuter `installer.bat`** pour installer Python et les dépendances automatiquement.
3. **Installer Bluestacks** puis Epic Seven.
4. **Dans Bluestacks** :
   - Ouvrir Contrôle de jeu > Éditeur de contrôle
   - Importer le fichier `com.stove.epic7.google`
   - Sélectionner Tout importer
5. **Lancer `lancer_bot.bat`**

### ▶️ Utilisation

1. **Choisir la musique** à jouer dans Epic Seven
2. **Cliquer sur Démarrer BOT**
3. **Laisser le bot jouer** la musique
4. **Quand elle est terminée**, cliquer sur Stopper BOT et passer à la suivante

---

## ✅ English Version

Epic Seven Bot – Rhythm Surfing Mode

This bot automates the Rhythm Surfing mini-game in Epic Seven, allowing you to farm all rewards and Skystones with ease.

### 🎯 Requirements

- Windows only
- Packbot (Git repository)
- Bluestacks
- Epic Seven installed on Bluestacks

### ⚙️ Installation

1. **Download Packbot** and unzip it.
2. **Run `installer.bat`** to install Python and required dependencies.
3. **Install Bluestacks** and then Epic Seven.
4. **In Bluestacks**:
   - Open Game Control > Control Editor
   - Import the file `com.stove.epic7.google`
   - Select Import All
5. **Launch `lancer_bot.bat`**

### ▶️ Usage

1. **Select the song** you want to play in Epic Seven
2. **Click Start BOT**
3. **Let the bot play** the song automatically
4. **Once finished**, click Stop BOT and move to the next song

---

## 🔧 Dépannage / Troubleshooting

### Problème : "python n'est pas reconnu"
**Solution** : Python n'est pas dans le PATH
1. Réinstallez Python en cochant "Add Python to PATH"
2. Ou redémarrez l'invite de commande

### Problème : "pip n'est pas reconnu"
**Solution** : Utilisez cette commande à la place :
```cmd
python -m pip install -r requirements.txt
```

### Problème : Erreur de permissions
**Solution** : Lancez l'invite de commande en tant qu'administrateur

### Problème : Le bot ne fonctionne pas
**Solutions** :
1. Assurez-vous d'être dans la bonne fenêtre/application
2. Vérifiez que l'antivirus ne bloque pas le programme
3. Redémarrez le bot

## ⚠️ Notes importantes

- Le bot utilise `pyautogui` pour simuler les touches
- `pyautogui.FAILSAFE = False` est activé pour éviter les arrêts accidentels
- Le bot fonctionne en arrière-plan même si l'interface n'est pas au premier plan
- Assurez-vous d'être dans la bonne fenêtre/application avant de démarrer le bot

## 📦 Dépendances

- `tkinter` : Interface graphique (inclus avec Python)
- `pyautogui` : Simulation des touches
- `keyboard` : Détection des raccourcis clavier
- `threading` : Exécution en arrière-plan (inclus avec Python)

## 🆘 Support

Si vous rencontrez des problèmes :
1. Vérifiez que Python est bien installé : `python --version`
2. Vérifiez que les dépendances sont installées : `pip list`
3. Relancez l'invite de commande
4. Redémarrez l'ordinateur si nécessaire
