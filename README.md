# keepalived-wrapper
Minimalist pure Python [Keepalived](https://keeaplived.org) wrapper.

If Keepalived is compiled with ```--JSON``` option, this wrapper will get JSON data from runnings VRRP instances.

## TO-DO
- [X] Starting from commit [e1593ef](https://github.com/acassen/keepalived/commit/e1593effaf4395e208947897d9fb0adaee484eae), Keepalived changed his JSON format, please update the class Keepalived.
- Starting from commit [e1593ef](https://github.com/acassen/keepalived/commit/e1593effaf4395e208947897d9fb0adaee484eae), Keepalived added VRRP ```track_process``` details as separated object in JSON output.

## Project's goals:
- Pure Python Keepalived wrapper.
- Analize in real-time multiples VRRP instances from multiples hosts.
- Streaming messages to message brokers.
- Simple integration with third-party software.

## Installation
```
pip install git+https://github.com/nser77/keepalived-wrapper.git
```

## Usage
```
from keepalived.wrapper import KeepalivedInterface

for k in KeepalivedInterface.getVrrp()
    print(k.iname)
    
>>> VI_1
>>> VI_n
```
