import cv2
import mediapipe as mp
import pyautogui
import math
import time

# Inizializza MediaPipe Hands
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Apri la webcam
cap = cv2.VideoCapture(0)

# Variabili per gestire il tempo ed evitare pressioni multiple in rapida successione
gesture_delay = 1.0  # secondi
last_gesture_time = 0

while True:
    success, img = cap.read()
    if not success:
        break

    # Converte l'immagine in RGB per MediaPipe
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            h, w, c = img.shape
            # Estrae le coordinate di ciascun punto di riferimento della mano
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))

            # Estrae la punta del pollice (id 4) e dell'indice (id 8)
            thumb_tip = next((item for item in lmList if item[0] == 4), None)
            index_tip = next((item for item in lmList if item[0] == 8), None)

            if thumb_tip and index_tip:
                x1, y1 = thumb_tip[1], thumb_tip[2]
                x2, y2 = index_tip[1], index_tip[2]
                # Calcola la distanza euclidea tra le due punte
                distance = math.hypot(x2 - x1, y2 - y1)

                # Visualizza la linea che unisce i due punti e la distanza
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(img, f'{int(distance)}', (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                # Imposta una soglia in pixel: se la distanza supera il valore, attiva l'input
                threshold = 40  # Regola questo valore in base al tuo setup
                current_time = time.time()
                if distance > threshold and (current_time - last_gesture_time > gesture_delay):
                    pyautogui.press('space')
                    last_gesture_time = current_time
                    cv2.putText(img, 'Jump!', (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Disegna i landmark e le connessioni sulla mano
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # Visualizza il video in una finestra
    cv2.imshow("Finger Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()