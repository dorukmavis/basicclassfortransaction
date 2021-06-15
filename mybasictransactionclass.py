import hashlib

class MavisCoinBlock:

    def __init__(self, previousblockhash,transactionlist,wallet) :
        self.previousblockhash = previousblockhash
        self.transactionlist = transactionlist
        self.blockdata = "-".join(transactionlist)+"\n"+previousblockhash
        self.blockhash = hashlib.sha256(self.blockdata.encode()).hexdigest()
        self.wallet = wallet


tr1 = "Doruk send 2.3 MC to Özgür"
tr2 = "Özgür send 2.9 MC to Melisa"
tr3 = "Çağlar send 2.1 MC to Sare"
tr4 = "Melisa send 4.3 MC to Doruk"
tr5 = "Sare send 3.2 MC to Eylül"
tr6 = "Eylül send 8.8 MC to Doruk"

initialblock = MavisCoinBlock("Transaction List",[tr1,tr2])

print(initialblock.blockdata)
print(initialblock.blockhash)

second_block = MavisCoinBlock(initialblock.blockhash,[tr3,tr4])

print(second_block.blockdata)
print(second_block.blockhash)

third_block = MavisCoinBlock(second_block.blockhash,[tr5,tr6])

print(third_block.blockdata)
print(third_block.blockhash)