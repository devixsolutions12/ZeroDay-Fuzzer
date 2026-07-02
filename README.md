# ZeroDay Fuzzer

An aggressive, automated API and endpoint fuzzing framework designed to map out unexpected behaviors and trigger 500 internal server errors indicative of poor memory management or unhandled exceptions.

## Features
- Dynamic alphanumeric + special character payload generation.
- Automated rate-limit evasion (jitter/sleeps).
- Crash logging for detailed payload reproduction.

## Usage
```bash
pip install requests
python3 fuzzer.py
```