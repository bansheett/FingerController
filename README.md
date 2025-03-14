# 🖐️ FingerController - Controllo del Mouse con la Mano 🖱️

FingerController è un sistema che permette di **controllare il mouse tramite gesture della mano**, utilizzando **OpenCV, MediaPipe e PyAutoGUI**.  
Il progetto sfrutta la **computer vision** per rilevare i movimenti delle dita e trasformarli in azioni sullo schermo, come spostare il cursore o simulare un clic.

## 🚀 Funzionalità
- **Controllo del mouse** in tempo reale tramite movimenti della mano.
- **Rilevamento delle mani** con **MediaPipe**.
- **Simulazione di click e movimenti del mouse** con **PyAutoGUI**.
- **Interfaccia fluida e reattiva**, con ottimizzazione del riconoscimento delle gesture.

---

## 🛠️ **Tecnologie Utilizzate**
- **Python 3.x**
- **OpenCV** (Computer Vision)
- **MediaPipe** (Rilevamento delle mani)
- **PyAutoGUI** (Controllo del mouse)

---

## 📦 **Installazione**
Segui questi passaggi per installare e avviare il progetto:

1. **Clonare il repository**  
   ```bash
   git clone https://github.com/bansheett/FingerController.git
   cd FingerController
   ```
2. **Installare le dipendenze**
   ```bash
   pip install -r requirements.txt
   ```
3. **Eseguire lo script**
   ```bash
   python finger_controller.py
   ```

## 🎮 **Come Funziona**
- Muovere il cursore: Muovi la mano davanti alla webcam.
- Click sinistro: Tocca con il pollice e l'indice.
- Click destro: Tocca con il pollice e il medio.
- Scroll: Muovi la mano su e giù con le dita estese.
- Uscire: Chiudi la mano in un pugno.

## 📖 **Struttura del Codice**
```bash
FingerController/
│── finger_controller.py   # Script principale
│── utils.py               # Funzioni di supporto
│── requirements.txt       # Dipendenze del progetto
│── README.md              # Documentazione
│── demo.gif               # (Opzionale) GIF dimostrativa
```

## 🛠 **Possibili Miglioramenti**
- Implementare il supporto per gesture personalizzate.
- Aggiungere una GUI per personalizzare le impostazioni.
- Ottimizzare il tracciamento per un minore consumo di CPU.

## 📜 **Licenza**
Questo progetto è distribuito sotto licenza MIT, quindi puoi modificarlo e utilizzarlo liberamente.
