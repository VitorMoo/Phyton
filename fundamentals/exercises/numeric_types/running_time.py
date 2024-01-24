def running_time():
    total_run_time = 0
    number_of_runs = 0

    while True:     #infinite loop that will only break with a brake statement
        one_run = input("Enter 10 km run time: ").strip() #.strip is used to remove white spaces like tab or space

        if not one_run:  #if it is empty then break 
            break

        number_of_runs += 1
        total_run_time += float(one_run) # converts user input to float 

    if number_of_runs > 0:
        average_time = total_run_time / number_of_runs
        print(f'Average of {average_time}, over {number_of_runs} runs')
    else:
        print("No runs entered.")

running_time()
