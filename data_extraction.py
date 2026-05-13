import os
from statistics import mean
import sys
import re
import glob

def parse_powermetrics(filename, process_name):
    total_joules = 0.0

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

                    process_seen_in_block = False 

    return total_joules, total_ms

if __name__ == "__main__":
    measured_energy = []
    measured_time = []
    if len(sys.argv) != 4:
        print("Usage: python3 data_extraction.py <file_prefix> <process_name> <n_loops>")
        sys.exit(1)

    prefix = sys.argv[1]       # T.ex. results/raw/energy_sumofsquares
    process_name = sys.argv[2] # T.ex. python3
    n_loops = int(sys.argv[3]) # T.ex. 100

    output_filename = os.path.basename(prefix) + "_summary.txt"
    output_path = os.path.join("results/processed", output_filename)
    os.makedirs("results/processed", exist_ok=True)

    file_pattern = f"{prefix}_run_*.txt"
    matching_files = sorted(glob.glob(file_pattern))

    with open(output_path, "w") as summary_file:
        summary_file.write(f"--- Analysis for {process_name} ({n_loops} iterations) ---\n")

        for i, filename in enumerate(matching_files, 1):
            j, elapsed_ms = parse_powermetrics(filename, process_name)

            if j is not None:
                measured_energy.append(j)
                measured_time.append(elapsed_ms)
                summary_file.write(f"Run {i}: Total Energy = {j:.4f} J, Total Time = {elapsed_ms:.2f} ms\n")

        n_loops = int(sys.argv[3])

        avg_energy_per_iter = mean(measured_energy) / n_loops
        avg_time_per_iter = mean(measured_time) / n_loops

        summary_file.write(f"Mean Energy (J) of 5 runs: {mean(measured_energy):.6f} J\n")
        summary_file.write(f"Mean Time (ms) of 5 runs: {mean(measured_time):.3f} ms\n")
        summary_file.write(f"Energy per iteration: {avg_energy_per_iter:.6f} J\n")
        summary_file.write(f"Time per iteration: {avg_time_per_iter:.3f} ms\n")
        print("Mean Energy (J) of 5 runs:", f"{mean(measured_energy):.6f} J")
        print("Mean Time (ms) of 5 runs:", f"{mean(measured_time):.3f} ms")
        print(f"Energy per iteration: {avg_energy_per_iter:.6f} J")
        print(f"Time per iteration: {avg_time_per_iter:.3f} ms")
