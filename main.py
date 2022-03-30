import time
import os
from src.config import Config
from src.constants import DELAY
from src.loop import Loop

if __name__ == "__main__":
    config = Config()
    users = [Loop(config, u) for u in config.users]
    
    cycle = 0
    while True:
        print(f'[CYCLE] Cycle #{cycle}')
        
        for user in users:
            user.run(cycle)
            
        cycle=cycle+1
        time.sleep(int(os.environ['delay']))
