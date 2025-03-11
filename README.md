# Finger Control
Finger Control è un progetto Python che utilizza le librerie OpenCV, MediaPipe e PyAutoGUI per rilevare il gesto di allargare l'indice e il pollice tramite la webcam e simulare la pressione della barra spaziatrice. Questo permette di controllare giochi come Geometry Dash eseguendo un semplice gesto manuale.

Indice
Introduzione
Requisiti
Installazione
Configurazione dell'Ambiente di Sviluppo
Utilizzo
Spiegazione del Codice
Troubleshooting
Contributi
Licenza
Introduzione
Il progetto Finger Control consente di utilizzare il gesto di allargare indice e pollice per dare input al gioco Geometry Dash. Quando il gesto viene riconosciuto, il programma simula la pressione della barra spaziatrice, facendo saltare il personaggio nel gioco.

Requisiti
Python: Versione 3.7 - 3.10 (consigliato)
Nota: MediaPipe attualmente non supporta Python 3.13 o versioni successive.
Librerie Python:
OpenCV
MediaPipe
PyAutoGUI
Installazione
1. Creazione dell'Ambiente Virtuale
È consigliato utilizzare un ambiente virtuale per isolare le dipendenze. Esempio su Windows:

bash
Copia
py -3.10 -m venv finger_control_env
finger_control_env\Scripts\activate
Su macOS/Linux:

bash
Copia
python3.10 -m venv finger_control_env
source finger_control_env/bin/activate
2. Installazione delle Dipendenze
Con l'ambiente virtuale attivato, esegui:

bash
Copia
pip install mediapipe opencv-python pyautogui
Configurazione dell'Ambiente di Sviluppo
Se utilizzi IntelliJ IDEA (o PyCharm):

Verifica Plugin Python:
Assicurati di avere il plugin Python installato e attivo.
Crea un Nuovo Progetto Python:
Seleziona "New Project" e scegli Python come tipo di progetto. Durante la creazione, specifica di utilizzare un nuovo ambiente virtuale (virtualenv) basato su Python 3.10.
Configura l'Interprete:
Dopo la creazione del progetto, verifica che l'interprete configurato punti al file dell'ambiente virtuale:
Su Windows: finger_control_env\Scripts\python.exe
Su macOS/Linux: finger_control_env/bin/python
Aggiungi il File del Codice:
Crea un file, ad esempio finger_control.py, ed incolla il codice del progetto.
Utilizzo
Avvia il Progetto:
Esegui lo script finger_control.py tramite l'ambiente virtuale (ad es. dal terminale integrato o configurando una run configuration in IntelliJ).
Interazione:
Il programma aprirà la webcam e inizierà a elaborare il feed video.
Quando viene rilevato il gesto (distanza tra la punta dell'indice e quella del pollice superiore a una soglia predefinita), il programma simula la pressione della barra spaziatrice, facendo "saltare" il personaggio nel gioco Geometry Dash.
Terminazione:
Premi il tasto 'q' per chiudere la finestra video e terminare il programma.
