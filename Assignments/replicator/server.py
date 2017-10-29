# Slave: Periodically (every 3 seconds) wake up and call master with latest SQN.
# Expect master to hold the request for 2 seconds until reply comes back
# Note the slave side replicate request timeout value has to be larger than the waiting timeout used by the master.


request_timeout = 60 * 2  # 2 seconds timeout.
request_frequency = 60 * 3 #