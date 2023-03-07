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
  @staticmethod
  def systemctlGetPIDFile(service):
    command = "systemctl show {service} -p PIDFile --value".format(service=service)
    r = LinuxInterface._readSubprocess(command).split(b"\n")
    return(str(r[0]))

  @staticmethod
  def systemctlGetMainPID(service):
    command = "systemctl show {service} -p MainPID --value".format(service=service)
    r = LinuxInterface._readSubprocess(command).split(b"\n")
    return(int(r[0]))
