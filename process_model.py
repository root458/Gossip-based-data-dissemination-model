# from abc import ABC, abstractmethod
from time import sleep
from threading import Thread
from data_model import Data

# Process template

# class Process(ABC):

#     def __init__(self):
#         self.data = Data()

#     @abstractmethod
#     def update_data(self):
#         pass

# class ProcessDFF(Process, Thread):
class ProcessDFF(Thread):
    # Process with DATA FROM FILE
    # This process gets new data from a file
    # It then shares the new data to other processes

    def __init__(self, letter):
        super().__init__()
        self.data = Data()
        # List of processes it is aware of
        self.__known_processes = []
        # susceptible = 0, infected = 1, removed = 2
        self.mode = 0
        self.letter = letter

    def know_processes(self, processes):
        # Make the process aware of existing process
        self.__known_processes = processes

    def update_data(self):

        # Get data from file, update on console
        new_list = []
        with open('data.txt', 'r') as file:
            new_list = list(map(lambda x: int(x), list(file.readline().split(' '))))

        
        # If data is new, update data, change mode, gossip
        if new_list != self.data.get_data():
            self.data.update_data(new_list)
            self.mode = 1
            # Update on console
            print('[*] Process {} has new data. Infected'.format(self.letter))
        else:
            print('[*] No new data for Process {} '.format(self.letter))
        
        

    def probe_and_push_data(self):

        # Iterate through the known processes and update with data

        for process in self.__known_processes:
            # Confirm data version of the process's data
            # If version is earlier, update and notify on console
            if self.data.get_version() > process.data.get_version():
                process.data.update_data(self.data.get_data())
                # Change process mode to infected
                process.mode = 1
                print('[*] Process {} has updated process {}'.format(self.letter, process.letter))
            else:
                # Process has the update, change mode
                self.mode = 2
                print('[*] Process {} already has the update from {}. {} has switched to Removed'.format(process.letter, self.letter, self.letter))
                sleep(3)
                break


            # Delay before moving to next process
            sleep(5) 

    def run(self):
        self.update_data()
        sleep(3)
        self.probe_and_push_data()

    def __str__(self):
        return '[*] Process {}\n[*] Data {}\n\n'.format(self.letter, self.data.get_data())





# class ProcessDFF(Process, Thread):
class ProcessDFP(Thread):
    # Process with DATA FROM OTHER PROCESSES
    # This process gets new data from other processes

    def __init__(self, letter):
        super().__init__()
        self.data = Data()
        # List of processes it is aware of
        self.__known_processes = []
        # susceptible = 0, infected = 1, removed = 2
        self.mode = 0
        self.letter = letter

    def know_processes(self, processes):
        # Make the process aware of existing process
        self.__known_processes = processes

    def update_data(self):
        pass

    def probe_and_push_data(self):
        # Iterate through the processes and update with data, if mode is infected
        sleep(8)
        if self.mode == 1:
            for process in self.__known_processes:
                # Confirm data version of the process's data
                # If version is earlier, update and notify on console
                if self.data.get_version() > process.data.get_version():
                    process.data.update_data(self.data.get_data())
                    # Change process mode to infected
                    process.mode = 1
                    print('[*] Process {} has updated process {}'.format(self.letter, process.letter))
                else:
                    # Process has the update, change mode
                    self.mode = 2
                    print('[*] Process {} already has the update from {}. {} has switched to Removed'.format(process.letter, self.letter, self.letter))
                    sleep(3)
                    break


                # Delay before moving to next process
                sleep(6)

    def run(self):
        self.probe_and_push_data()

    def __str__(self):
        return '[*] Process {}\n[*] Data {}\n\n'.format(self.letter, self.data.get_data())
