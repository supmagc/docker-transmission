import transmissionrpc
import sys
import logging

enabled=False
host='localhost'
port=9091
user=None
password=None

if not enabled:
    sys.exit(0)

logging.getLogger('transmissionrpc').setLevel(logging.WARNING)
client = transmissionrpc.Client(host, port=port, user=user, password=password)
torrents = client.info()
for tid, torrent in torrents.iteritems():
    if torrent.isFinished:
        print('%s is finished and will be removed' % (torrent.name))
        client.remove(torrent.hashString, delete_data=True)
