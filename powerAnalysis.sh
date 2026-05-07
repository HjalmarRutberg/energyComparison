#!/bin/bash

ALGORITHM="$1"
ARGS_INPUT="$2"
N_LOOPS="$3"

# Create results directory if it doesn't exist
mkdir -p results

for i in {1..5}
do
    echo "--------------------------------------"
    echo "Starting Run $i of 5..."
    
    RESULT_FILE="results/energy_$(basename "$ALGORITHM")_$(basename "$ARGS_INPUT")_run_$i.txt"

    sudo powermetrics -i 300 --samplers tasks,cpu_power -o "$RESULT_FILE" & 
    POWER_PID=$! 

    echo powermetrics started with PID $POWER_PID
    
    sleep 0.5
    if ! ps -p $POWER_PID > /dev/null; then
        echo "ERROR: powermetrics failed to start! Check $RESULT_FILE"
        exit 1
    fi

    sleep 2; 
    
    # Runs the chosen algorithm, chosen input and 
    # number of loops in one run.
    $ALGORITHM "$ARGS_INPUT" "$N_LOOPS"
    
    sleep 0.5;
    sudo kill -2 $POWER_PID
    echo "Run $i complete. Data: $RESULT_FILE"
    
    # Wait 5 sec before running next test
    if [ $i -lt 5 ]; then
        echo "Cooling down for 5 seconds..."
        sleep 5
    fi
done

echo "--------------------------------------"
echo "All 5 runs complete!"