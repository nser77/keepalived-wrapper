# keepalived-wrapper
Minimalist pure Python [Keepalived](https://keeaplived.org) wrapper.

If Keepalived is compiled with ```--JSON``` option, this wrapper will get JSON data from runnings VRRP instances.

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

for k in KeepalivedInterface.getKeepalived()
    print(k.iname)
    
>>> VI_1
>>> VI_n
```
