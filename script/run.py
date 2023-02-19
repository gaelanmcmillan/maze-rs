import os
import sys

if len(sys.argv) != 1:
  buildmode = sys.argv[1]
  if buildmode not in ['release']:
    print("Invalid buildmode")
    exit(1)
else:
  buildmode = 'debug'

buildstr = '--release' if buildmode == 'release' else ''

os.chdir("/Users/dogzone/dev/2023/maze-rs/")
def do(cmd):
  print(f"Running {cmd}")
  if os.system(cmd) != 0:
    print("\tBad exit code, breaking")
    exit(1)

list(map(do, 
  [
    f"cargo build {buildstr} --target wasm32-unknown-unknown",
    f"cp target/wasm32-unknown-unknown/{buildmode}/maze-rs.wasm docs/"
  ]
))