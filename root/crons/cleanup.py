from datetime import datetime, timedelta
import common

client = common.getTransmissionClient('cleanup')
client.blocklist_update()
torrents = client.get_torrents()
for torrent in torrents:
    if torrent.isFinished and not torrent.error and datetime.fromtimestamp(torrent.doneDate) + timedelta(days=1) < datetime.now():
        print('%s is finished and will be removed' % (torrent.name))
        client.remove(torrent.hashString, delete_data=True)
