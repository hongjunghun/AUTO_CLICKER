import keyboard
import mouse
import time

class Clicking():
    
    
    def click(self, key, sleep_time):
        key = key.lower()
        key_map = {
            "capslock": "caps lock",
            "tab": "tab",
            "shift": "shift",
            "escape": "esc",
            "control": "ctrl"
        }
        key_name = key_map.get(key, key)

        print(f"{key_name} 키를 누르는 동안 우클릭 반복 시작 (ESC로 중단)")

        try:
            while True:
                while keyboard.is_pressed(key_name):
                    mouse.click(button='right')
                    time.sleep(sleep_time)
                if keyboard.is_pressed("esc"):  # ESC키 누르면 중단
                    print("ESC 키 감지 - 클릭 중단")
                    break
                time.sleep(sleep_time)
        except Exception as e:
            print(f"클릭 중 오류 발생: {e}")
