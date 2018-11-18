
# Loading a Bloom Filter

## Do the following:

* Connect to a testnet node
* Load a filter for your testnet address
* Send a request for transactions from the block which had your previous testnet transaction
* Receive the merkleblock and tx messages.


```python
# Exercise 2.2

from bloomfilter import BloomFilter

block_hash = bytes.fromhex('<fill this in>')
passphrase = b'<fill this in>'  # FILL THIS IN
secret = little_endian_to_int(hash256(passphrase))
private_key = PrivateKey(secret=secret)
addr = private_key.point.address(testnet=True)
print(addr)
filter_size = 30
filter_num_functions = 5
filter_tweak = -1  # FILL THIS IN

# get the hash160 of the address using decode_base58
# create a bloom filter using the filter_size, filter_num_functions and filter_tweak above
# add the h160 to the bloom filter

# connect to tbtc.programmingblockchain.com in testnet mode, logging True
# complete the handshake
# send the filterload command with bf.filterload() as the payload
# create a getdata message
# add_data (FILTERED_BLOCK_DATA_TYPE, block_hash) to request the block
# send the getdata message
# wait for the merkleblock command
# wait for the tx command
# print the envelope payload in hex
```
