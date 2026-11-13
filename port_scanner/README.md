# TCP Port Scanner

Scans a range of TCP ports on a host and prints the open ones.

## Usage

```bash
python scanner.py 127.0.0.1 -s 1 -e 1000
```

| Option | Meaning | Default |
|--------|---------|---------|
| `host` | Target host | required |
| `-s`, `--start` | First port | 1 |
| `-e`, `--end` | Last port | 1024 |
| `-t`, `--timeout` | Timeout per port (seconds) | 0.5 |

## How it works

Tries a TCP connection to each port using `socket.create_connection`.
A successful connection means the port is open. Uses a thread pool
so many ports are checked at the same time.

## What I learned

- Socket programming basics
- Threading with `ThreadPoolExecutor`
- Command-line arguments with `argparse`