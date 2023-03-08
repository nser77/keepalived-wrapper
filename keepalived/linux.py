from os import kill

import subprocess
from subprocess import Popen, PIPE

from time import sleep

class LinuxInterface():
  signals = [36]

  @staticmethod
  def _killProcess(pid_file, signal):
    # TODO: check if pid file exists
    if signal in LinuxInterface.signals:
      if kill(pid_file, signal):
        sleep(0.001)
        return True

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
