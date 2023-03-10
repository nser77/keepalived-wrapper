# keepalived-wrapper
Python [keepalived](https://github.com/acassen/keepalived) wrapper.

If [keepalived](https://github.com/acassen/keepalived) is compiled with ```--enable-json``` option, this wrapper will get JSON data from runnings VRRP instance(s).

Starting from commit [```e1593ef```](https://github.com/acassen/keepalived/commit/e1593effaf4395e208947897d9fb0adaee484eae), [keepalived](https://github.com/acassen/keepalived) added ```json_version``` option in ```global_def``` configuration section.

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

for k in KeepalivedInterface.getVrrp():
    print(k.iname, k.last_transition, k.adver_int)
    
>>> VI_1, '2023-03-08 19:30:57', 1
>>> VI_n, ...
```
