from flask import Flask, jsonify, request
# from flask_cors import CORS
from blockchain import Blockchain
from argparse import ArgumentParser

app = Flask(__name__)
# CORS(app)


@app.route('/', methods=['GET'])
def chian():
    chain = test.chain 
    dictChain = [block.__dict__.copy() for block in chain]
    for dictBlock in dictChain:
        dictBlock['transactions'] = [tx.__dict__ for tx in dictBlock['transactions']]
    return jsonify(dictChain), 200


@app.route('/mine', methods=['POST'])
def mine():

  
    blockk = test.addBlcok() 
    if blockk != None:
        dictBlockk = [block.__dict__.copy() for block in block]
        for dictBlock in dictBlockk:
          dictBlock['transactions'] = [tx.__dict__ for tx in dictBlock['transactions']]
        return jsonify(blockk), 200
    else:
        res={
            'Message':'There is a issue with the Block can not MINE'
        }   
        return jsonify(res), 500
        
    pass

@app.route('/opentxs', methods=['GET'])
def opentxs():
    """ get the unconfirmed transactions or any transaction has not been included in a block """
    txs=test.unconfirmed
    if txs != None:
        dicTx= [tx.__dict__ for tx in txs]
        res={
            'Transation':dicTx
        }
        return jsonify(res), 200
    else:
        res={
            'Message':'There are no Transations'
        }   
        return jsonify(res), 500

@app.route('/sendtx', methods=['POST'])
def sendtx():
    """ send a transaction"""
    values=request.get_json()
    if not values:
        res={
            'Message':'There is no input'
        }
        return jsonify(res), 400
    reqkey=['sender', 'receiver', 'amount']
    if not all (key in values for key in reqkey):
        res={
            'Message':'There is a missing value'
        }
        return jsonify(res), 400
    sender=values['sender']
    receiver=values['receiver']
    amount=values['amount']
    addtex=test.addTransaction(sender, receiver, amount)
    if addtex != None:
        res={
            'Transations':{
              'sender':values['sender'],
              'receiver':values['receiver'],
              'amount':values['amount']  
            }
        }
        return jsonify(res), 200
    else:
        res={
            'Message':'The Transations does not pass'
        }   
        return jsonify(res), 500

if __name__ == '__main__':
    ser = ArgumentParser()
    ser.add_argument('-p', '--port', default=8020)
    args = ser.parse_args()
    port = args.port
    test = Blockchain()
    app.run(debug=True, port=port)
