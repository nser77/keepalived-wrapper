import subprocess
from subprocess import Popen, PIPE

class LinuxInterface():
  @staticmethod
  def _readSubprocess(command):
      with Popen(command, shell=True, stdout=PIPE) as p:
          p.wait()
          return p.communicate()[0]

  @staticmethod
  def _runSubprocess(command):
      with Popen(command, shell=True) as p:
          p.wait()
          return p

  @staticmethod
  def getIpv4NonLocalBind():
    r = LinuxInterface._readSubprocess('cat /proc/sys/net/ipv4/ip_nonlocal_bind').split(b"\n")
    return(int(r[0]))

class SystemdInterface():
  pass
