
## Build for WASM
```shell
rustup target add wasm32-unknown-unknown
cargo build --target wasm32-unknown-unknown
```

## Development Workflow
1. Start local HTTP server on `$PORT` (LiveServer in VSCode, for instance)
2. Open the browser to `localhost:$PORT/docs/`
3. From the project root, run the following shell command
```shell
python3 script/run.py (release)
```
