"""Every Point: runs the whale tracker in a continous loop"""

import time

from  config import Scan_Interval_Seconds
from tracker import  scan_once

def main():
     print("Solana Whale Tracker Bot initiazed")
     while True:
          try:
               scan_once()
          except Exception as loop_error:
               print(f"Loop error caught to prevent crash:{loop_error}")

          time.sleep(Scan_Interval_Seconds)

if __name__=="__main__":
     main()