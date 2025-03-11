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
