import time

def any_func_with_loop(): 
    """Example of a function using a loading bar.
    """

    list_to_loop = [i for i in range(333)] # Iterable exemple
    t_start = time.perf_counter() # Relative time in seconds
    percentage_counter = 0 # Used to not print the same percentage twice
    loop_counter = 0 
    
    for item in list_to_loop:
        
        # Your code here
        time.sleep(0.3)
        
        # Code to track execution progress
        loop_counter+=1
        percentage = round(100*(loop_counter)/len(list_to_loop),0) # Rounded progress percentage 
        if percentage%10 ==0: # Print from 10% to 10%
            if percentage_counter !=percentage: # Ensures rounded % will not be printed twice
                t_prov = time.perf_counter()
                time_elapsed = t_prov -t_start
                time_estimated = (100*time_elapsed/percentage)-time_elapsed
                print(f'Status: {percentage:.0f}% Completed! -> '
                      f'Elapsed time:{time_elapsed:.2f}s or {time_elapsed/60:.2f}min. | '
                      f'Estimated time: {time_estimated:.2f}s or {time_estimated/60:.2f}min')
                percentage_counter = percentage # Save last percentage printed
                
any_func_with_loop()