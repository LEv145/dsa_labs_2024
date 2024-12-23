from pathlib import Path
import heapq


BASE_PATH = Path("data/12")
RUN_SIZE = 10
INPUT_FILE = BASE_PATH / "input.txt"
A_FILE = BASE_PATH / "a.txt"
B_FILE = BASE_PATH / "b.txt"
C_FILE = BASE_PATH / "c.txt"
D_FILE = BASE_PATH / "d.txt"


def create_runs(input_file, run_size, run_files):
    run_counter = 0
    with open(input_file) as fp:
        while True:
            lines = [fp.readline().strip() for _ in range(run_size)]
            lines = [line for line in lines if line]
            if not lines:
                break
            lines.sort(key=int)

            run_file = run_files[run_counter % 2]
            with open(run_file, "a") as output_fp:
                output_fp.write("\n".join(lines) + "\n")

            run_counter += 1


def polyphase_merge(run_size):
    size = run_size
    input_files = [A_FILE, B_FILE]
    output_files = [C_FILE, D_FILE]

    current_input = input_files.copy()
    current_output = output_files.copy()

    while True:
        runs_merged = 0

        for file in current_output:
            file.unlink(missing_ok=True)

        with open(current_input[0]) as fp_1, \
            open(current_input[1]) as fp_2, \
            open(current_output[0], "a") as out_1, \
            open(current_output[1], "a") as out_2:
            while True:
                run_1 = [fp_1.readline().strip() for _ in range(size)]
                run_2 = [fp_2.readline().strip() for _ in range(size)]
                run_1 = [line for line in run_1 if line]
                run_2 = [line for line in run_2 if line]

                if not run_1 and not run_2:
                    break

                if run_1 and run_2:
                    merged_run = list(heapq.merge(run_1, run_2, key=int))
                elif run_1:
                    merged_run = run_1
                else:
                    merged_run = run_2

                if runs_merged % 2 == 0:
                    out_fp = out_1
                else:
                    out_fp = out_2

                out_fp.write("\n".join(merged_run) + "\n")
                runs_merged += 1

        if runs_merged <= 1:
            final_output = current_output[0] if runs_merged == 1 else current_input[0]
            return final_output

        size *= 2
        current_input, current_output = current_output, current_input


def main():
    A_FILE.unlink(missing_ok=True)
    B_FILE.unlink(missing_ok=True)
    C_FILE.unlink(missing_ok=True)
    D_FILE.unlink(missing_ok=True)

    create_runs(INPUT_FILE, RUN_SIZE, [A_FILE, B_FILE])
    result = polyphase_merge(RUN_SIZE)

    print(result)


if __name__ == "__main__":
    main()
