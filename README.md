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

## Keepalived VRRP JSON output:
```
[
  {
    "data": {
      "iname": "VI_1",
      "dont_track_primary": 0,
      "skip_check_adv_addr": 0,
      "strict_mode": 1,
      "vmac_ifname": "",
      "ifp_ifname": "eth0",
      "master_priority": 0,
      "last_transition": 1677963907.144095,
      "garp_delay": 5,
      "garp_refresh": 0,
      "garp_rep": 5,
      "garp_refresh_rep": 1,
      "garp_lower_prio_delay": 0,
      "garp_lower_prio_rep": 0,
      "lower_prio_no_advert": 1,
      "higher_prio_send_advert": 0,
      "vrid": 99,
      "base_priority": 233,
      "effective_priority": 233,
      "vipset": false,
      "promote_secondaries": false,
      "adver_int": 1,
      "master_adver_int": 1,
      "accept": 1,
      "nopreempt": true,
      "preempt_delay": 0,
      "state": 3,
      "wantstate": 3,
      "version": 3,
      "smtp_alert": false,
      "notify_deleted": false,
      "vips": [
        "192.168.1.250 dev eth0 scope global"
      ],
      "track_process": [
        "asterisk",
        "gunicorn"
      ]
    },
    "stats": {
      "advert_rcvd": 0,
      "advert_sent": 0,
      "become_master": 0,
      "release_master": 0,
      "packet_len_err": 0,
      "advert_interval_err": 0,
      "ip_ttl_err": 0,
      "invalid_type_rcvd": 0,
      "addr_list_err": 0,
      "invalid_authtype": 0,
      "pri_zero_rcvd": 0,
      "pri_zero_sent": 0
    }
  }
]

```
