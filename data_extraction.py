from statistics import mean
import sys
import re

def parse_powermetrics(filename, process_name):
    total_joules = 0.0
    total_samples_found = 0

    current_elapsed_ms = 0.0
    total_ms = 0.0
    process_seen_in_block = False

    # Regular expressions to extract elapsed time and power
    elapsed_re = re.compile(r"\((\d+\.\d+)ms elapsed\)")
    power_re = re.compile(r"Combined Power \(CPU \+ GPU \+ ANE\): (\d+) mW")

    with open(filename, 'r') as f:
        for line in f:
            if "*** Sampled system activity" in line:
                match = elapsed_re.search(line)
                if match:
                    current_elapsed_ms = float(match.group(1))
                    process_seen_in_block = False 

            if process_name in line:
                process_seen_in_block = True

            if "Combined Power" in line:
                power_match = power_re.search(line)
                if power_match and process_seen_in_block:
                    power_mw = float(power_match.group(1))
                    total_ms += current_elapsed_ms
                    joules = (power_mw / 1000.0) * (current_elapsed_ms / 1000.0)

                    total_joules += joules
                    total_samples_found += 1

                    process_seen_in_block = False 

    return total_joules, total_samples_found, total_ms

if __name__ == "__main__":
    measured_energy = []
    measured_time = []
    if len(sys.argv) < 3:
        print("Usage: python3 parse_energy.py <logfile> <process_name>")
    else:
        for i in range(1, 6):
            j, s, elapsed_ms = parse_powermetrics(sys.argv[1]+"_run_"+str(i)+".txt", sys.argv[2])
            measured_energy.append(j)
            measured_time.append(elapsed_ms)
    print("Mean Energy (J) of 5 runs:", mean(measured_energy))
    print("Mean Time (ms) of 5 runs:", mean(measured_time))