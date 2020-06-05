import time

lastTime = time.time()
FPS = 10

def game_logic(delta):
    print(delta);

while True:
    currentTime = time.time()
    sleepTime = 1./FPS - (currentTime - lastTime)
    if sleepTime > 0:
        time.sleep(sleepTime)
    dt = currentTime - lastTime
    lastTime = currentTime
    game_logic(dt)

