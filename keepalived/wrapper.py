from .linux import LinuxInterface, SystemdInterface
from datetime import datetime
from json import load

class KeepalivedBase(object):
    errors = []
    warnings = []
    human_data_convertion = '%Y-%m-%d %H:%M:%S'

    def timestampToHuman(self, timestamp):
        human = datetime.fromtimestamp(timestamp).strftime(self.human_data_convertion)
        return human

class KeepalivedData(KeepalivedBase):
    def data(self, data):
        self.iname =                   data['iname']
        self.dont_track_primary =      data['dont_track_primary']
        self.skip_check_adv_addr =     data['skip_check_adv_addr']
        self.strict_mode =             data['strict_mode']
        self.vmac_ifname =             data['vmac_ifname']
        self.ifp_ifname =              data['ifp_ifname']
        self.master_priority =         data['master_priority']
        self.setLastTransition(        data['last_transition'])
        self.garp_delay =              data['garp_delay']
        self.garp_refresh =            data['garp_refresh']
        self.garp_rep =                data['garp_rep']
        self.garp_refresh_rep =        data['garp_refresh_rep']
        self.garp_lower_prio_delay =   data['garp_refresh_rep']
        self.garp_lower_prio_rep =     data['garp_lower_prio_rep']
        self.lower_prio_no_advert =    data['lower_prio_no_advert']
        self.higher_prio_send_advert = data['higher_prio_send_advert']
        self.vrid =                    data['vrid']
        self.base_priority =           data['base_priority']
        self.effective_priority =      data['effective_priority']
        self.vipset =                  data['vipset']
        self.promote_secondaries =     data['promote_secondaries']
        self.adver_int =               data['adver_int']
        self.master_adver_int =        data['master_adver_int']
        self.accept =                  data['accept']
        self.nopreempt =               data['nopreempt']
        self.preempt_delay =           data['preempt_delay']
        self.state =                   data['state']
        self.wantstate =               data['wantstate']
        self.version =                 data['version']
        self.smtp_alert =              data['smtp_alert']
        self.notify_deleted =          data['notify_deleted']
        self.vips =                    data['vips']
        try:
            self.track_process =           data['track_process']
        except:
            pass

    def setLastTransition(self, last_transition):
        if last_transition:
            self.last_transition = self.timestampToHuman(last_transition)

class KeepalivedStats(KeepalivedBase):
    def stats(self, stats):
        self.advert_rcvd =            stats['advert_rcvd']
        self.advert_sent =            stats['advert_sent']
        self.become_master =          stats['become_master']
        self.release_master =         stats['release_master']
        self.packet_len_err =         stats['packet_len_err']
        self.advert_interval_err =    stats['advert_interval_err']
        self.ip_ttl_err =             stats['ip_ttl_err']
        self.invalid_type_rcvd =      stats['invalid_type_rcvd']
        self.addr_list_err =          stats['addr_list_err']
        self.invalid_authtype =       stats['invalid_authtype']
        self.pri_zero_rcvd =          stats['pri_zero_rcvd']
        self.pri_zero_sent =          stats['pri_zero_sent']

class Keepalived(KeepalivedData, KeepalivedStats):
    def __init__(self, data, stats):
        self.data(data)
        self.stats(stats)

class KeepalivedInterface():
    @staticmethod
    def isKeepalivedRunning():
        if SystemdInterface.getMainPID("keepalived") == 0:
            return False
        return True

    @staticmethod
    def getKeepalivedData():
        if not LinuxInterface._killProcess(SystemdInterface.getPIDFile("keepalived"), 36):
            return False
        return True

    @staticmethod
    def getKeepalivedJsonTmpFile():
        p = LinuxInterface._readSubprocess('ls /tmp | grep -i keepalived').split(b"\n")
        return "/tmp/{}/tmp/keepalived.json".format(p[0].decode("utf-8"))

    @staticmethod
    def getVrrp():
        if not KeepalivedInterface.isKeepalivedRunning():
            return False

        if not KeepalivedInterface.getKeepalivedData():
            return False

        with open(KeepalivedInterface.getKeepalivedJsonTmpFile()) as json:
            j=load(json)
            if j:
                try:
                    if j['vrrp']:
                        for instance in j['vrrp']:
                            yield Keepalived(instance['data'], instance['stats'])
                except:
                    for instance in j:
                        yield Keepalived(instance['data'], instance['stats'])
