# BlockIntelAI

BlockIntelAI is a decentralized AI-powered chatbot that integrates **Ethereum Blockchain (Ganache) and OpenAI GPT-4o** to ensure immutable and transparent message logging. This chatbot securely logs all user-bot interactions on the blockchain using a **Solidity smart contract**, making it tamper-proof and verifiable.

## Features
- Logs chat messages on the Ethereum blockchain for transparency and immutability.
- Uses OpenAI's GPT-4o for intelligent chatbot responses.
- Connects to a local Ethereum network (Ganache) for smart contract deployment.
- Interacts with the blockchain using Web3.py.
- Fully decentralized and secure.

## Prerequisites
Ensure you have the following installed before running the project:

1. **Python (>=3.8)** - Install from [python.org](https://www.python.org/)
2. **Node.js & NPM** (for Ganache) - Install from [nodejs.org](https://nodejs.org/)
3. **Ganache** (Ethereum blockchain simulator) - Install from [trufflesuite.com/ganache](https://trufflesuite.com/ganache/)
4. **MetaMask Wallet** (Optional, for interacting with the contract)
5. **Solidity Compiler (solcx)** - Installed via Python.
6. **Web3.py** - Python library for interacting with Ethereum.

## Setup Instructions

### 1. Clone the Repository
```sh
 git clone https://github.com/yourusername/BlockGPT.git
 cd BlockGPT
```

### 2. Install Dependencies
```sh
 pip install -r requirements.txt
```

### 3. Setup Environment Variables
Create a `.env` file in the project root and add your OpenAI API key:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Start Ganache
Open **Ganache**, select **Quickstart Ethereum**, and ensure it's running on `http://127.0.0.1:7545`.

### 5. Run the Blockchain Chatbot
```sh
 python main.py
```

## How It Works
1. The chatbot takes user input.
2. The message is logged on the blockchain.
3. The chatbot sends the message to OpenAI GPT-4o for processing.
4. GPT-4o responds, and the bot logs the response on the blockchain.
5. The conversation remains immutable and verifiable.

## Smart Contract
The chatbot logs all conversations using this Solidity contract:
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract Chatlog {
    event MessageLogged(address indexed sender, string message, uint256 timestamp);
    function LogMessage(string calldata message) public {
        emit MessageLogged(msg.sender, message, block.timestamp);
    }
}
```

## Contributing
Pull requests are welcome. For significant changes, please open an issue first.

## License
This project is licensed under the MIT License.

