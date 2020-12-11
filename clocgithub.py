import subprocess
import sys
url = sys.argv[1]
subprocess.run(["mkdir", ".clocOnGitHubtmp"])
subprocess.run(["git", "clone", url, ".clocOnGitHubtmp"])
subprocess.run(["cloc", ".clocOnGitHubtmp"])
subprocess.run(["rm", "-rf", ".clocOnGitHubtmp"])
