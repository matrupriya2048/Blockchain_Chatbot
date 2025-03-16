# BlockIntelAI

BlockIntelAI is a decentralized AI-powered chatbot that integrates Ethereum Blockchain (Ganache) and OpenAI GPT-4o to ensure immutable and transparent message logging. This chatbot securely logs all user-bot interactions on the blockchain using a Solidity smart contract, making it tamper-proof and verifiable.

Features

Logs chat messages on the Ethereum blockchain for transparency and immutability.

Uses OpenAI's GPT-4o for intelligent chatbot responses.

Connects to a local Ethereum network (Ganache) for smart contract deployment.

Interacts with the blockchain using Web3.py.

Fully decentralized and secure.

Prerequisites

Ensure you have the following installed before running the project:

Python (>=3.8) - Install from python.org

Node.js & NPM (for Ganache) - Install from nodejs.org

Ganache (Ethereum blockchain simulator) - Install from trufflesuite.com/ganache

MetaMask Wallet (Optional, for interacting with the contract)

Solidity Compiler (solcx) - Installed via Python.

Web3.py - Python library for interacting with Ethereum.

Setup Instructions

1. Clone the Repository

 git clone https://github.com/yourusername/BlockGPT.git
 cd BlockGPT

2. Install Dependencies

 pip install -r requirements.txt

3. Setup Environment Variables

Create a .env file in the project root and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here

4. Start Ganache

Open Ganache, select Quickstart Ethereum, and ensure it's running on http://127.0.0.1:7545.

5. Run the Blockchain Chatbot

 python main.py

How It Works

The chatbot takes user input.

The message is logged on the blockchain.

The chatbot sends the message to OpenAI GPT-4o for processing.

GPT-4o responds, and the bot logs the response on the blockchain.

The conversation remains immutable and verifiable.

Smart Contract

The chatbot logs all conversations using this Solidity contract:

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract Chatlog {
    event MessageLogged(address indexed sender, string message, uint256 timestamp);
    function LogMessage(string calldata message) public {
        emit MessageLogged(msg.sender, message, block.timestamp);
    }
}

Contributing

Pull requests are welcome. For significant changes, please open an issue first.

License

This project is licensed under the MIT License.
