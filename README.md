# Finger Control

**Finger Control** è un progetto Python che utilizza le librerie **OpenCV**, **MediaPipe** e **PyAutoGUI** per rilevare il gesto di allargare l'indice e il pollice tramite la webcam e simulare la pressione della barra spaziatrice. Questo permette di controllare giochi come Geometry Dash eseguendo un semplice gesto manuale.

---

## Indice

- [Introduzione](#introduzione)
- [Requisiti](#requisiti)
- [Installazione](#installazione)
- [Configurazione dell'Ambiente di Sviluppo](#configurazione-dellambiente-di-sviluppo)
- [Utilizzo](#utilizzo)
- [Spiegazione del Codice](#spiegazione-del-codice)
- [Troubleshooting](#troubleshooting)
- [Contributi](#contributi)
- [Licenza](#licenza)

---

## Introduzione

Il progetto **Finger Control** consente di utilizzare il gesto di allargare indice e pollice per dare input al gioco Geometry Dash. Quando il gesto viene riconosciuto, il programma simula la pressione della barra spaziatrice, facendo saltare il personaggio nel gioco.

---

## Requisiti

- **Python:** Versione 3.7 - 3.10 (consigliato)  
  *Nota: MediaPipe attualmente non supporta Python 3.13 o versioni successive.*
- **Librerie Python:**  
  - [OpenCV](https://pypi.org/project/opencv-python/)  
  - [MediaPipe](https://pypi.org/project/mediapipe/)  
  - [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)

---

## Installazione

### 1. Creazione dell'Ambiente Virtuale

È consigliato utilizzare un ambiente virtuale per isolare le dipendenze. Esempio su Windows:

```bash
py -3.10 -m venv finger_control_env
finger_control_env\Scripts\activate
```


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
Seleziona New Project e scegli Python come tipo di progetto. Durante la creazione, specifica di utilizzare un nuovo ambiente virtuale (virtualenv) basato su Python 3.10.
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
Spiegazione del Codice
Il file finger_control.py contiene il seguente flusso logico:

Importazione delle Librerie:
Vengono importate le librerie necessarie: cv2 per l'elaborazione video, mediapipe per il tracciamento dei landmark della mano, pyautogui per simulare input tastiera, e moduli standard come math e time.

Inizializzazione di MediaPipe Hands:
Viene creato un oggetto per il rilevamento della mano, limitato a una mano per volta e con una soglia di confidenza impostata.

Acquisizione del Feed Video:
La webcam viene aperta con OpenCV e ad ogni frame viene convertita l'immagine in RGB per essere processata da MediaPipe.

Elaborazione dei Landmark:
Per ogni mano rilevata, il programma calcola le coordinate in pixel dei landmark. In particolare, estrae la punta del pollice (landmark 4) e quella dell'indice (landmark 8).

Calcolo della Distanza e Input:
Viene calcolata la distanza euclidea tra i due punti. Se la distanza supera una soglia definita (ad esempio, 40 pixel) e trascorre un intervallo minimo di tempo per evitare input multipli, il programma simula la pressione della barra spaziatrice.

Visualizzazione:
Il frame video viene mostrato in una finestra con una linea tracciata tra i due punti e, se il gesto viene riconosciuto, viene visualizzato il messaggio "Jump!".

Troubleshooting
Errore MediaPipe:
Se ricevi errori relativi a MediaPipe, verifica che la versione di Python sia compatibile (3.7-3.10) e che l'ambiente virtuale sia attivo durante l'installazione.

Problemi con l'interprete in IntelliJ:
Assicurati che il progetto sia riconosciuto come progetto Python e che l'interprete configurato punti all'ambiente virtuale creato.

Webcam non funzionante:
Controlla che la webcam sia collegata e che nessun'altra applicazione la stia utilizzando.

Contributi
Se desideri contribuire a questo progetto, segui questi passaggi:

Fork del Repository
Crea un Branch:
bash
Copia
git checkout -b feature/nuova-funzionalità
Effettua le Modifiche e Committa:
bash
Copia
git commit -am "Aggiunta nuova funzionalità"
Invia una Pull Request
Licenza
Questo progetto è distribuito sotto la licenza MIT.
Consulta il file LICENSE per ulteriori dettagli.

rust
Copia

Salva questo contenut
