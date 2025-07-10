# Jeu du Cavalier d'Euler ♞

Un jeu interactif résolvant le problème mathématique du parcours du cavalier sur un échiquier.


## Fonctionnalités ✨

- 🎮 **Jeu entièrement interactif** avec déplacement du cavalier
- 📊 Tailles d'échiquier configurables (5x5 à 8x8)
- 💡 Système d'indices visuels
- ⏱️ Chronomètre intégré
- ↩️ Fonction d'annulation (undo)
- 🎉 Animation de victoire avec confettis
- 📱 Interface responsive

## Comment jouer 🕹️

1. Cliquez sur "Nouvelle partie" pour commencer
2. Déplacez le cavalier (case jaune ♞) en cliquant sur les cases bleues
3. Visitez chaque case exactement une fois
4. Le cavalier se déplace en L (2 cases horizontales + 1 verticale ou vice versa)

## Technologies utilisées 💻

- **Frontend** : HTML5, CSS3, JavaScript (vanilla)
- **Backend** : Python (serveur HTTP minimal)
- **Pattern** : Architecture monopage (SPA)

## Installation 🛠️

1. Clonez le dépôt :
git clone https://github.com/diari17/Jeu-Cavalier-d-Euler.git
cd Jeu-Cavalier-d-Euler

2. Lancez le serveur :
python server.py

3. Ouvrez dans votre navigateur :
http://localhost:8000

Structure des fichiers 📂

Jeu-Cavalier-d-Euler/
├── index.html          # Interface principale
├── style.css           # Styles CSS
├── server.py           # Serveur Python
└── README.md           # Ce fichier