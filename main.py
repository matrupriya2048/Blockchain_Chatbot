import os
from openai import OpenAI
from web3 import Web3
from solcx import compile_source, install_solc
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise Exception("Error: OPENAI_API_KEY not found in environment variables")

# Connect to Ganache Server
ganache_url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))
print(f"Connection to Ganache: {'Successful' if w3.is_connected() else 'Failed'}")

if not w3.is_connected():
    print("Troubleshooting suggestions:")
    print("1. Make sure Ganache is running")
    print("2. Verify the Ganache URL (default is http://127.0.0.1:7545)")
    print("3. Check if any firewall is blocking the connection")
    raise Exception("Error: Cannot connect to Ganache")

# First ganache account for transactions
w3.eth.default_account = w3.eth.accounts[0]
print(f"Using account: {w3.eth.default_account}")

# Solidity smart contract as a string
contract_source_code = '''
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract Chatlog {
    event MessageLogged(address indexed sender, string message, uint256 timestamp);
    function LogMessage(string calldata message) public {
        emit MessageLogged(msg.sender, message, block.timestamp);
    }
}
'''

# Compile the solidity contract
try:
    install_solc('0.8.0')
    compiled_sol = compile_source(contract_source_code, solc_version='0.8.0')
    contract_id, contract_interface = compiled_sol.popitem()
    
    # Extract the bytecode and ABI
    bytecode = contract_interface['bin']
    abi = contract_interface['abi']
    
    print("Contract compiled successfully")
except Exception as e:
    print(f"Error compiling contract: {e}")
    raise

# Deploy the contract
try:
    Chatlog = w3.eth.contract(abi=abi, bytecode=bytecode)
    print("Deploying the contract...")
    tx_hash = Chatlog.constructor().transact()
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    contract_address = tx_receipt.contractAddress
    print(f"Contract deployed successfully at: {contract_address}")
except Exception as e:
    print(f"Error deploying contract: {e}")
    raise

# Create a contract instance to interact
chatlog_contract = w3.eth.contract(address=contract_address, abi=abi)

# Define the function to log a message
def log_message_on_blockchain(message):
    try:
        tx_hash = chatlog_contract.functions.LogMessage(message).transact()
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Message logged on blockchain: {tx_hash.hex()}")
        return True
    except Exception as e:
        print(f"Error logging message: {e}")
        return False

# Function to get chatbot response
def get_chatbot_response(user_message):
    try:
        # Create OpenAI client with API key
        client = OpenAI(api_key=api_key)
        
        # Make API call
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful chatbot."},
                {"role": "user", "content": user_message},
            ],
            max_tokens=256
        )
        
        # Extract response
        reply = response.choices[0].message.content.strip()
        return reply
    except Exception as e:
        print(f"Error getting chatbot response: {e}")
        return f"I'm having trouble processing your request. Error: {str(e)}"

# Driver Code
def main():
    print("\n=== Blockchain + AI Chatbot ===")
    print("Type 'exit' or 'quit' to end the chat.\n")

    while True:
        user_message = input("You: ")
        if user_message.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        # Log user message
        if log_message_on_blockchain(f"User: {user_message}"):
            print("✓ User message logged on blockchain")
        
        # Get and display bot response
        print("Bot is thinking...")
        bot_response = get_chatbot_response(user_message)
        print(f"Bot: {bot_response}")
        
        # Log bot response
        if log_message_on_blockchain(f"Bot: {bot_response}"):
            print("✓ Bot response logged on blockchain")
        print()

if __name__ == "__main__":
    main()