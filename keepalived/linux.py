from os import kill

import subprocess
from subprocess import Popen, PIPE

from time import sleep

class LinuxInterface():
  signals = [36]

  @staticmethod
  def _killProcess(pid_file, signal):
    # TODO: check if pid_file exists
    if signal in LinuxInterface.signals:
      with open(pid_file, "r") as f:
        pid = int(f.read())
      if pid >= 1:
        kill(pid, signal)
        sleep(0.001)
        return True
    return False

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
      with open("/proc/sys/net/ipv4/ip_nonlocal_bind", "r") as f:
          content = f.read().split("\n")
          return content[0]

class SystemdInterface():
  @staticmethod
  def systemctlShowCommand(service, property):
    command = "systemctl show {service} -p {property} --value".format(service=service, property=property)
    return(str(command))

  @staticmethod
  def getPIDFile(service):
    r = LinuxInterface._readSubprocess(SystemdInterface.systemctlShowCommand(service, 'PIDFile')).split(b"\n")
    return(r[0].decode("utf-8"))

  @staticmethod
  def getMainPID(service):
    r = LinuxInterface._readSubprocess(SystemdInterface.systemctlShowCommand(service, 'MainPID')).split(b"\n")
    return(int(r[0]))
