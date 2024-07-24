'''
 @Author: manoj kr
   @Date: 2024-07-20 2:15
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-20 2:30
   @Title : Write a Stopwatch Program for measuring the time that elapses between
            the start and end clicks.
'''
import time
def stop_watch():
    '''
    Description : To measuring the time that elapses between
                  the start and end clicks.
    Return : int(elapsed_time) the time that elapses between
                  the start and end clicks in seconds.
    '''
    input("press Enter to Start StopWatch")
    start=time.time()
    input("press Enter to Stop StopWatch")
    stop=time.time()
    elapsed_time=stop-start
    print(f"Elapsed Time :{elapsed_time} seconds")

if __name__=="__main__":
     stop_watch()

