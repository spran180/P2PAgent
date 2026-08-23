# P2PAgent

A distributed agentic AI application that combines peer-to-peer networking with AI task processing and real-time collaboration through EtherCalc spreadsheet integration.

## Overview

P2PAgent is a decentralized system designed to process AI-driven tasks across multiple peer nodes using libp2p for networking. The application leverages:

- **SeaLion AI Model** (via LiteLLM) for task processing
- **libp2p** for peer-to-peer communication and message publishing
- **GossipSub Protocol** for distributed pub/sub messaging
- **EtherCalc** for collaborative spreadsheet-based monitoring and status tracking

## Features

- **Distributed Task Processing**: Process AI tasks across multiple worker peers
- **P2P Networking**: Direct peer-to-peer communication using libp2p
- **Pub/Sub Messaging**: Publish tasks and receive responses via GossipSub protocol
- **Real-time Collaboration**: Track worker status and task responses in collaborative spreadsheets
- **Async/Await Architecture**: Built on Trio for efficient concurrent operations
- **Flexible AI Models**: Uses LiteLLM for multi-model support

## Technologies

- **Python 3.8+**
- **py-libp2p**: Peer-to-peer networking library
- **LiteLLM**: LLM interface supporting multiple AI providers
- **SeaLion**: Southeast Asian language model
- **EtherCalc**: Open-source collaborative spreadsheet platform
- **Trio**: Async concurrency library

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd AI-App
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure EtherCalc is running (default: http://localhost:8000)

## Configuration

Configure the application using environment variables:

```bash
# SeaLion API configuration
export SEALION_API_KEY="your-api-key-here"

# EtherCalc configuration
export ETHERCALC_URL="http://localhost:8000"
export SHEET_NAME="agent-status"
```

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `SEALION_API_KEY` | - | API key for SeaLion model (required) |
| `ETHERCALC_URL` | `http://localhost:8000` | EtherCalc server URL |
| `SHEET_NAME` | - | EtherCalc spreadsheet name for status tracking |

## Usage

### Create EtherCalc Spreadsheet

Initialize the shared spreadsheet for monitoring:

```bash
python ethercalc/table.py
```

This creates a table with columns: `Peer`, `Message`, `Status`

### Run Worker Node

Start a worker that listens for tasks:

```bash
python p2p_connection.py --worker-id worker1
```

### Run Dispatcher Node

Start a dispatcher that sends tasks and receives responses:

```bash
python p2p_connection.py --dispatcher
```

## Project Structure

```
AI-App/
├── agent.py              # AI task processing logic using SeaLion
├── p2p_connection.py     # P2P networking and worker/dispatcher implementation
├── ethercalc/
│   └── table.py          # EtherCalc spreadsheet management
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

### Module Descriptions

- **agent.py**: Handles AI inference using LiteLLM with SeaLion model
- **p2p_connection.py**: Manages peer discovery, pub/sub messaging, and task distribution
- **ethercalc/table.py**: Creates and manages collaborative spreadsheets for status tracking

## How It Works

1. **Task Submission**: Dispatcher publishes tasks to the `agent/tasks/v1` topic
2. **Task Processing**: Worker nodes subscribe to tasks and process them using the SeaLion AI model
3. **Response Publishing**: Workers publish results to the `agent/responses/v1` topic
4. **Status Tracking**: All activity is logged to an EtherCalc spreadsheet in real-time

## Topics

- **Task Topic**: `agent/tasks/v1` - Incoming tasks for workers
- **Response Topic**: `agent/responses/v1` - Task results from workers

## Requirements

See `requirements.txt` for complete dependencies:
- litellm
- libp2p
- requests

## License

[Add your license here]
