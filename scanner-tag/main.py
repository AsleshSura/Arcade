import time
import machine
import network
import urequests

# --- CONFIGURATION & GAME STATE ---
GAME_DURATION_SECS = 120  # 2 minutes
start_time = time.time()
player_score = 0

# Point mapping for body parts
"""
Key:
- Same 4 numbers = single hit place

-- 11XX = Arm
-- 22XX = Leg

-- XXX1 - Left
-- XXX2 - Right

- Player = Alphabet
"""


key = {"0000": "forehead", 
       "1101": "left arm", 
       "1102": "right arm", 
       "2201": "left leg",
       "2202": "right leg",
       "3333": "back",
       "4444": "chest"}

# --- HARDWARE SETUP ---

def init_display():
    # Placeholder for your screen setup (e.g., SSD1306 OLED)
    print("Display Initialized")

def update_display(score, time_left):
    # Replace prints with your actual LCD/OLED draw commands
    print(f"--- SCREEN ---")
    print(f"Score: {score}")
    print(f"Time Left: {time_left}s")
    print(f"--------------")

def send_score_to_database(player_id, part, points):
    """Wireless data sync (Placeholder for Wi-Fi/HTTP POST or MQTT)"""
    print(f"[SYNCING] Sent to server: Player {player_id} hit in {part} for {points} pts.")
    # Example: 
    # url = "http://192.168.1.100:5000/score"
    # data = {'player': player_id, 'part': part, 'points': points}
    # urequests.post(url, json=data)

# --- MAIN GAME LOOP ---
init_display()
print("Game Started!")

while True:
    # 1. Calculate Time Remaining
    elapsed = time.time() - start_time
    time_remaining = max(0, GAME_DURATION_SECS - elapsed)
    
    if time_remaining <= 0:
        print("GAME OVER!")
        update_display(player_score, 0)
        break

    # 2. Update Display periodically
    update_display(player_score, time_remaining)

    # 3. Check for Barcode Scans (Non-blocking)
    if scanner_uart.any():
        # Read the barcode string and clean it up
        raw_data = scanner_uart.readline()
        try:
            barcode_str = raw_data.decode('utf-8').strip()
            print(f"Scanned: {barcode_str}")
            
            # Parse the barcode (Expected format: "PlayerID-BodyPart")
            if "-" in barcode_str:
                player_id, body_part = barcode_str.split("-")
                body_part = body_part.upper()
                
                if body_part in POINT_VALUES:
                    points_earned = POINT_VALUES[body_part]
                    player_score += points_earned
                    
                    print(f"Hit Player {player_id} on {body_part}! +{points_earned} pts")
                    
                    # 4. Wireless Sync
                    send_score_to_database(player_id, body_part, points_earned)
                else:
                    print("Unknown body part scanned.")
            else:
                print("Invalid barcode format.")
                
        except Exception as e:
            print("Error parsing scan:", e)

    time.sleep(0.1) # Small delay to prevent CPU melting