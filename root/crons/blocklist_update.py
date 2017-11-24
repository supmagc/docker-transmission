import common

client = common.getTransmissionClient('blocklist-update')
print('Blocklist will be updated')
client.blocklist_update()
