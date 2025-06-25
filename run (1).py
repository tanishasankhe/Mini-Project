import multiprocessing
from main import start  # Import the start function from main
from engine.features import hotword  # Import the hotword function

# To run Eva
def startEva():
    print("Process 1 (Eva) is running.")
    start()  # Start the main application

# To run hotword
def listenHotword():
    print("Process 2 (Hotword Listener) is running.")
    hotword()  # Start the hotword detection

# Start both processes
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=startEva)
    p2 = multiprocessing.Process(target=listenHotword)

    # Start both processes
    p1.start()
    p2.start()

    # Wait for the Eva process to finish
    p1.join()

    # If the hotword listener is still alive, terminate it
    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("System stopped.")  
