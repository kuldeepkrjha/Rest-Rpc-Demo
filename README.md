# REST & gRPC API Demo Project
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.9%2B-green)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-yellow)
![gRPC](https://img.shields.io/badge/gRPC-1.56%2B-orange)
A complete demo project showcasing how to implement the same service using both REST and gRPC APIs. Perfect for learning API design patterns and comparing the two approaches.
> **Note**: We welcome feedback and contributions! If you encounter any issues, please report them in the [issues section](https://github.com/yourusername/rest-grpc-demo/issues).
## Table of Contents
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [Running the Services](#running-the-services)
- [Testing the APIs](#testing-the-apis)
- [Understanding the Differences](#understanding-the-differences)
- [Extending the Project](#extending-the-project)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
## Project Overview
This project demonstrates how to implement the same service using two different API paradigms:
- **REST API**: Using Flask with JSON over HTTP/1.1
- **gRPC API**: Using gRPC with Protocol Buffers over HTTP/2
Both APIs provide access to user data with the same functionality, allowing you to compare the implementations side-by-side.
Key Features:
- Simple user data model with ID, name, and email
- REST endpoint: `GET /user/{user_id}`
- gRPC method: `GetUser(UserRequest) returns (UserResponse)`
- Complete separation of concerns between API implementations
- Minimal dependencies for easy setup
## Prerequisites
Before you begin, ensure you have the following installed:
1. **Python 3.9 or higher**:
   - Download from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version` or `python3 --version`
2. **Git** (optional but recommended):
   - Download from [git-scm.com](https://git-scm.com/downloads)
   - Verify installation: `git --version`
## Setup Instructions
### 1. Clone the Repository (Recommended)
```bash
git clone https://github.com/yourusername/rest-grpc-demo.git
cd rest-grpc-demo
```
### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate
# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install flask grpcio grpcio-tools
```
### 4. Generate gRPC Protocol Buffer Files
```bash
# Windows
python -m grpc_tools.protoc -I proto --python_out=rpc_api --grpc_python_out=rpc_api proto\service.proto
# macOS/Linux
python -m grpc_tools.protoc -I proto --python_out=rpc_api --grpc_python_out=rpc_api proto/service.proto
```
This will generate two files in the `rpc_api` directory:
- `service_pb2.py`: Protocol buffer message classes
- `service_pb2_grpc.py`: gRPC server and client stubs
## Project Structure
```
rest-grpc-demo/
├── proto/                   # Protocol Buffer definitions
│   └── service.proto        # Service interface definition
│
├── rest_api/                # REST API implementation
│   └── app.py               # Flask REST server
│
├── rpc_api/                 # gRPC API implementation
│   ├── server.py            # gRPC server
│   ├── client.py            # gRPC client (for testing)
│   ├── service_pb2.py       # Generated protocol buffer code
│   └── service_pb2_grpc.py  # Generated gRPC code
│
└── README.md                # This documentation
```
## Running the Services
You need to run the REST API and gRPC API in separate terminal sessions.
### Terminal 1: REST API Server
```bash
# Activate virtual environment (if not already active)
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
# Start REST server
python rest_api/app.py
```
You should see output similar to:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```
### Terminal 2: gRPC API Server
```bash
# Activate virtual environment (if not already active)
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
# Start gRPC server
python rpc_api/server.py
```
You should see output similar to:
```
gRPC server running on port 50051
```
## Testing the APIs
### Testing REST API
#### Option 1: Using cURL
```bash
curl http://localhost:5000/user/1
```
Expected response:
```json
{
  "user_id": "1",
  "name": "Windows User",
  "email": "user@windows.com"
}
```
#### Option 2: Using Web Browser
Visit `http://localhost:5000/user/1` in your browser.
#### Option 3: Using Python Requests
```python
import requests
response = requests.get("http://localhost:5000/user/1")
print(response.json())
```
### Testing gRPC API
#### Option 1: Using the Included Client
```bash
python rpc_api/client.py
```
Expected output:
```
Received: ID=1, Name=Windows User, Email=user@windows.com
```
#### Option 2: Using grpcurl (Recommended for Advanced Testing)
1. Install grpcurl:
   ```bash
   # macOS
   brew install grpcurl
   
   # Windows (using Scoop)
   scoop install grpcurl
   
   # Linux (Debian/Ubuntu)
   sudo apt install grpcurl
   ```
2. Run query:
   ```bash
   grpcurl -plaintext -proto proto/service.proto -d '{"user_id": "1"}' localhost:50051 user.UserService/GetUser
   ```
Expected response:
```json
{
  "user_id": "1",
  "name": "Windows User",
  "email": "user@windows.com"
}
```
## Understanding the Differences
### REST API Implementation (Flask)
- **Protocol**: HTTP/1.1
- **Data Format**: JSON
- **Endpoint**: `GET /user/<user_id>`
- **Advantages**:
  - Human-readable
  - Browser-friendly
  - Simple to implement
  - Wide client support
- **Disadvantages**:
  - No strict schema
  - Text-based (less efficient)
  - Limited to request/response model
### gRPC API Implementation
- **Protocol**: HTTP/2
- **Data Format**: Protocol Buffers (binary)
- **Method**: `GetUser(UserRequest) returns (UserResponse)`
- **Advantages**:
  - Strong typing
  - Efficient binary format
  - Supports streaming
  - Automatic code generation
- **Disadvantages**:
  - Requires special tools for testing
  - More complex setup
  - Limited browser support
## Extending the Project
### Adding a New Field
1. Edit `proto/service.proto`:
   ```proto
   message UserResponse {
     string user_id = 1;
     string name = 2;
     string email = 3;
     string phone = 4;  // Add new field
   }
   ```
2. Regenerate gRPC code:
   ```bash
   python -m grpc_tools.protoc -I proto --python_out=rpc_api --grpc_python_out=rpc_api proto/service.proto
   ```
3. Update server implementations:
   - In `rpc_api/server.py`: Add phone number to user data
   - In `rest_api/app.py`: Add phone number to user dictionary
### Adding a New Method
1. Edit `proto/service.proto`:
   ```proto
   service UserService {
     rpc GetUser (UserRequest) returns (UserResponse);
     rpc CreateUser (CreateUserRequest) returns (UserResponse);  // New method
   }
   
   message CreateUserRequest {
     string name = 1;
     string email = 2;
   }
   ```
2. Regenerate gRPC code (same command as above)
3. Implement the new method in:
   - `rpc_api/server.py`
   - `rest_api/app.py` (as a new POST endpoint)
## Troubleshooting
### Common Issues and Solutions
1. **Python not recognized**:
   - Ensure Python is installed and added to PATH
   - Try `python3` instead of `python` on Linux/macOS
2. **Virtual environment activation fails (Windows)**:
   ```cmd
   # Run in PowerShell instead of CMD
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
3. **gRPC generation errors**:
   - Verify protobuf file location: `proto/service.proto`
   - Ensure you're in the project root directory
   - Check for typos in the command
4. **Port conflicts**:
   - Check for other services using ports 5000 or 50051
   - Change ports in:
     - REST: `rest_api/app.py` (modify `app.run(port=...)`)
     - gRPC: `rpc_api/server.py` (modify `server.add_insecure_port('...')`)
5. **gRPC client not connecting**:
   - Ensure gRPC server is running
   - Verify port number matches server configuration
   - Check firewall settings if using remote connections
## Contributing
Contributions are welcome! Here's how to contribute:
1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/yourusername/rest-grpc-demo.git`
3. Create a **new branch**: `git checkout -b feature-name`
4. Make your changes
5. **Commit** your changes: `git commit -m "Add feature"`
6. **Push** to your branch: `git push origin feature-name`
7. Create a **Pull Request**
Please ensure your code follows PEP 8 style guidelines and includes appropriate tests.
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```text
MIT License
Copyright (c) [year] [fullname]
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS O
