# HTTP Stream
## Dependencies
`quart`, `quart_cors`

## Run Server
```sh
python3 app.py
```
## Usage
- Run server.
- Open that `index.html` file in your favourite browser.

## How?
Just for usage, it has a single `test.py` file.
File reads `/` directory and waits for 3 sec. Then read `/` directory again and streaming while this command runs.
In `index.html` file read this and put all output to same directory.
