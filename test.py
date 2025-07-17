import mouse, keyboard, time
while True:
    while keyboard.is_pressed("caps lock"):
        mouse.click()
        time.sleep(0.001)
