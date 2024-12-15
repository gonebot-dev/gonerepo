import os
import shutil
import argparse
import subprocess


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("current_sha", help="Current git sha", type=str)
    parser.add_argument("before_sha", help="Previous git sha", type=str)
    args = parser.parse_args()

    subprocess.run(["echo 'Changed JSON files:'"], shell=True)
    output = subprocess.run(
        [f"git diff --diff-filter=AM --name-only {args.before_sha} {args.current_sha} | grep '\\.json$'"],
        shell=True,
        capture_output=True,
        text=True
    )
    if output.returncode == 1:
        subprocess.run(["echo 'No JSON files changed'"], shell=True)
        exit(0)
    files = output.stdout.splitlines()
    for file in files:
        subprocess.run([f"echo '{file}'"], shell=True)
    for file in files:
        subprocess.run([f"echo 'Testing {file}...'"], shell=True)
        exit_code = subprocess.run([f"python scripts/generate_test.py {file}"], shell=True).returncode
        if exit_code != 0:
            continue
        os.chdir("test")
        subprocess.run(["go mod init main"], shell=True)
        subprocess.run(["go fmt"], shell=True)
        exit_code = subprocess.run(["go mod tidy"], shell=True).returncode
        if exit_code != 0:
            subprocess.run(["echo 'go mod tidy failed!'"], shell=True)
            exit(1)
        exit_code = subprocess.run(["timeout --foreground 30 go run main"], shell=True).returncode
        if exit_code == 124 or exit_code == 0:
            subprocess.run([f"echo 'Test passed for {file}!'"], shell=True)
        else:
            subprocess.run([f"echo 'Test failed for {file}!'"], shell=True)
            os.chdir("..")
            shutil.rmtree("test")
            exit(1)
        os.chdir("..")
        shutil.rmtree("test")
