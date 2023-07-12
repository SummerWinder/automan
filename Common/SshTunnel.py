from sshtunnel import SSHTunnelForwarder


class sshTunnel:
    def __init__(self):
        self.sshHost = None
        self.sshPort = None
        self.sshUsername = None
        self.sshPassword = None
        self.sshPrivateKey = None
        self.remoteAddress = None
        self.remotePort = None
        self.localAddress = "127.0.0.1"
        self.localPort = None
        self.server = None

    def connWithPassword(self):
        self.server = SSHTunnelForwarder(
            (self.sshHost, self.sshPort),
            ssh_username=self.sshUsername,
            ssh_password=self.sshPassword,
            remote_bind_address=(self.remoteAddress, self.remotePort),
            local_bind_address=(self.localAddress, self.localPort)
        )
        self.server.start()

    def connWithPrivateKey(self):
        self.server = SSHTunnelForwarder(
            (self.sshHost, self.sshPort),
            ssh_username=self.sshUsername,
            ssh_pkey=self.sshPrivateKey,
            remote_bind_address=(self.remoteAddress, self.remotePort),
            local_bind_address=(self.localAddress, self.localPort)
        )
        self.server.start()

    def closeConn(self):
        self.server.close()


if __name__ == '__main__':
    sshTunnel().conn()
