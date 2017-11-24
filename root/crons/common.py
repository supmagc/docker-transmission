import os.path
import logging
import ConfigParser
import transmissionrpc

def getTransmissionClient(script):
    cfg = ConfigParser.RawConfigParser()
    if os.path.isfile('/config/scripts.cfg'):
        cfg.read('/config/scripts.cfg')
    elif os.path.isfile('config/scripts.cfg'):
        cfg.read('config/scripts.cfg')

    host = cfg.get('common', 'host')
    port = cfg.getint('common', 'port')
    user = cfg.get('common', 'user')
    password = cfg.get('common', 'password')
    enabled = cfg.getboolean(script, 'enabled')

    if not enabled:
        sys.exit(0)

    logging.getLogger('transmissionrpc').setLevel(logging.WARNING)
    client = transmissionrpc.Client(host, port=port, user=user, password=password)

    return client
