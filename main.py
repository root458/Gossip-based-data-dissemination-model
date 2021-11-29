from process_model import *



if __name__ == "__main__":
    # Instantiate processes
    processdff = ProcessDFF('A')

    lst = ['B', 'C', 'D', 'E']
    processes = []
    for i in lst:
        processes.append(ProcessDFP(i))

    # Make processes know other processes
    processdff.know_processes([processes[0], processes[1]])
    processes[0].know_processes([processes[2], processes[1]])
    processes[2].know_processes([processes[3]])
    processes[1].know_processes([processes[3]])


    # Print the initial data
    print(processdff)
    for i in processes:
        print(i)

    # Start processes
    processdff.start()
    sleep(2)
    for i in processes:
        sleep(1)
        i.start()


    sleep(30)
    # Print the data they have in the end
    print('\n')
    print(processdff)
    for i in processes:
        print(i)
    