import cv2
import mediapipe as mp
import pyautogui
import math
import time
import concurrent.futures

# Inizializza MediaPipe Hands con tracking migliorato
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mpDraw = mp.solutions.drawing_utils

# Crea un ThreadPoolExecutor per gestire le chiamate a pyautogui.press in modo asincrono
executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)

# Apri la webcam e imposta una risoluzione più bassa per migliorare le prestazioni
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# Imposta il threshold per il gesto e il delay minimo tra un salto e l'altro
threshold = 70         # Soglia in pixel per il gesto
gesture_delay = 0.1    # 100 millisecondi di delay minimo
last_gesture_time = 0

while True:
    success, img = cap.read()
    if not success:
        break

    # Converti l'immagine in RGB per MediaPipe
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            h, w, _ = img.shape
            # Estrai i landmark della mano
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))

            # Estrai la punta del pollice (id 4) e dell'indice (id 8)
            thumb_tip = next((item for item in lmList if item[0] == 4), None)
            index_tip = next((item for item in lmList if item[0] == 8), None)

            if thumb_tip and index_tip:
                x1, y1 = thumb_tip[1], thumb_tip[2]
                x2, y2 = index_tip[1], index_tip[2]
                # Calcola la distanza euclidea tra i due punti
                distance = math.hypot(x2 - x1, y2 - y1)

                # Disegna la linea e visualizza la distanza
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(img, f'{int(distance)}', (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

                # Se la distanza supera il threshold e se è passato il delay minimo, esegui il salto
                current_time = time.time()
                if distance > threshold and (current_time - last_gesture_time > gesture_delay):
                    executor.submit(pyautogui.press, 'space')
                    last_gesture_time = current_time
                    cv2.putText(img, 'Jump!', (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            # Disegna i landmark e le connessioni sulla mano
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # Visualizza il feed video
    cv2.imshow("Finger Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
executor.shutdown()