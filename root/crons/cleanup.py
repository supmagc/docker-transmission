from datetime import datetime, timedelta
import common

client = common.getTransmissionClient('cleanup')
print('Running cleanup')
torrents = client.get_torrents()
delay = common.getConfigParser().getint('cleanup', 'delay')
for torrent in torrents:
    if torrent.isFinished and not torrent.error and datetime.fromtimestamp(torrent.doneDate) + timedelta(days=delay) < datetime.now():
        print('%s is finished and will be removed' % (torrent.name))
        client.remove(torrent.hashString, delete_data=True)
