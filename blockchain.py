import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update((str(self.index) + 
                    str(self.timestamp) + 
                    str(self.data) + 
                    str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

# Example usage
blockchain = Blockchain()
blockchain.add_block(Block(1, time.time(), "Amount $1000", ""))
blockchain.add_block(Block(2, time.time(), "Amount $500", ""))

for block in blockchain.chain:
    print("Block Index:", block.index)
    print("Block Timestamp:", block.timestamp)
    print("Block Data:", block.data)
    print("Block Hash:", block.hash)
    print("Previous Hash:", block.previous_hash)
    print("-----------------------------")
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

