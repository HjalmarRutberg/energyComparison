#!/bin/bash

ALGORITHM="$1"
ARGS_INPUT="$2"
N_LOOPS="$3"

RESULT_FILE="results/energy_$(basename "$ALGORITHM")_$(basename "$ARGS_INPUT")"

sudo powermetrics -i "100" --samplers tasks,cpu_power -o "$RESULT_FILE" & POWER_PID=$! 
sleep 1; 
$ALGORITHM "$ARGS_INPUT" "$N_LOOPS"; 
sudo kill $POWER_PID

echo "Measurement complete. Data saved to $RESULT_FILE"