
# Loading a Bloom Filter

## Do the following:

* Connect to a testnet node
* Load a filter for your testnet address
* Send a request for transactions from the block which had your previous testnet transaction
* Receive the merkleblock and tx messages.


```python
# Exercise 2.2

from bloomfilter import BloomFilter, BIP37_CONSTANT
from helper import (
    bit_field_to_bytes,
    decode_base58,
    hash160,
    hash256,
    little_endian_to_int,
    murmur3,
    run,
    SIGHASH_ALL,
)
from ecc import PrivateKey
from network import (
    GetDataMessage,
    GetHeadersMessage,
    HeadersMessage,
    SimpleNode,
    FILTERED_BLOCK_DATA_TYPE,
    TX_DATA_TYPE,
)

block_hash = bytes.fromhex('0000000053787814ed9dd8c029d0a0a9af4ab8ec0591dc31bdc4ab31fae88ce9')
passphrase = b'Jimmy Song Programming Blockchain'  # FILL THIS IN
secret = little_endian_to_int(hash256(passphrase))
private_key = PrivateKey(secret=secret)
addr = private_key.point.address(testnet=True)
print(addr)
filter_size = 30
filter_num_functions = 5
filter_tweak = 90210  # FILL THIS IN

# get the hash160 of the address using decode_base58
h160 = decode_base58(addr)
# create a bloom filter using the filter_size, filter_num_functions and filter_tweak above
bf = BloomFilter(filter_size, filter_num_functions, filter_tweak)
# add the h160 to the bloom filter
bf.add(h160)

# connect to tbtc.programmingblockchain.com in testnet mode, logging True
node = SimpleNode('tbtc.programmingblockchain.com', testnet=True, logging=True)
# complete the handshake
node.handshake()
# send the filterload command with bf.filterload() as the payload
node.send(b'filterload', bf.filterload())
# create a getdata message
getdata = GetDataMessage()
# add_data (FILTERED_BLOCK_DATA_TYPE, block_hash) to request the block
getdata.add_data(FILTERED_BLOCK_DATA_TYPE, block_hash)
# send the getdata message
node.send(getdata.command, getdata.serialize())
# wait for the merkleblock command
envelope = node.wait_for_commands([b'merkleblock'])
# wait for the tx command
envelope = node.wait_for_commands([b'tx'])
# print the envelope payload in hex
print(envelope.payload.hex())
```
