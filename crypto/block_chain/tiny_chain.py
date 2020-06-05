import hashlib as h
import datetime as date

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
    
  def __str__(self):
      return 'Block #{}'.format(self.index)
    
  def hash_block(self):
    h.sha256().update((str(self.index) + 
               str(self.timestamp) + 
               str(self.data) + 
               str(self.previous_hash)).encode())
    return h.sha256().hexdigest()

def genesis_block():
  return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = "Chainblock " + str(this_index)
  this_hash = last_block.hash
  return Block(this_index, this_timestamp, this_data, this_hash)

### prog starts

blockchain = [genesis_block()]
previous_block = blockchain[0]
num_of_blocks_to_add = 5

for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add


for i in blockchain:
    print("")
    print("INDEX: " + str(i.index) + "  | STR: " + str(i) + "  | CREATED: " + str(i.timestamp))
    print("Hash:", i.hash)
    print("DATA: " + str(i.data))
    
    
