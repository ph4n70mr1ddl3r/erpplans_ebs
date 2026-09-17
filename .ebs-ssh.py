#!/usr/bin/env python3
"""SSH helper for the EBS Vision VM (password auth via the WSL->Windows-host route).

Usage: python3 .ebs-ssh.py 'remote command'
       python3 .ebs-ssh.py --put local remote
       python3 .ebs-ssh.py --get remote local
"""
import sys
import socket
import paramiko
from subprocess import run

VM_USER = "oracle"
VM_PASS = "Samurai1975@!"


def gateway():
    out = run(["ip", "route", "show", "default"], capture_output=True, text=True).stdout
    return out.split()[2]


def connect():
    gw = gateway()
    sock = socket.create_connection((gw, 2222), timeout=30)
    return paramiko.SSHClient(), sock


def main():
    client, sock = connect()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(gateway(), port=2222, username=VM_USER, password=VM_PASS, sock=sock,
                   allow_agent=False, look_for_keys=False)
    args = sys.argv[1:]
    if not args:
        print("no command", file=sys.stderr)
        sys.exit(2)
    if args[0] == "--put":
        sftp = client.open_sftp()
        sftp.put(args[1], args[2])
        print(f"put {args[1]} -> {args[2]}")
    elif args[0] == "--get":
        sftp = client.open_sftp()
        sftp.get(args[1], args[2])
        print(f"get {args[1]} -> {args[2]}")
    else:
        cmd = " ".join(args)
        stdin, stdout, stderr = client.exec_command(cmd, timeout=1800)
        out = stdout.read().decode("utf-8", "replace")
        err = stderr.read().decode("utf-8", "replace")
        rc = stdout.channel.recv_exit_status()
        if out:
            print(out)
        if err:
            print(err, file=sys.stderr)
        sys.exit(rc)
    client.close()


if __name__ == "__main__":
    main()
