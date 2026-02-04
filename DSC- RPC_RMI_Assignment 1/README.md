# Assignment 1: RPC and RMI in a Cloud Environment

## Overview
This assignment demonstrates the implementation of distributed applications using **Remote Procedure Call (RPC)** and **Remote Method Invocation (RMI)**. Both services are hosted on a cloud virtual machine and accessed remotely by client programs.

The objective is to show successful client–server communication, remote invocation of services, and correct result retrieval from a cloud-hosted server.

---

## Technologies Used
- **RPC:** Python (XML-RPC)
- **RMI:** Java
- **Cloud Platform:** Linux-based Cloud VM (Ubuntu)
- **Networking:** Client–Server Architecture

---

## RPC Implementation (Python)

### Description
A **Course Performance Service** is implemented using XML-RPC.  
The server maintains course score records and evaluates student performance.

### Features
- Register course scores remotely
- Retrieve course records
- Evaluate performance status (Excellent / Satisfactory / Fail)

### Files
- `rpc_server.py` – RPC server hosted on the cloud VM
- `rpc_client.py` – RPC client invoking remote procedures

### Outcome
The client successfully connects to the cloud server and receives evaluated results for course performance.

---

## RMI Implementation (Java)

### Description
An **Academic Progress Service** is implemented using Java RMI.  
The remote object evaluates academic status based on examination scores.

### Features
- Register examination results
- Fetch result summaries
- Determine academic status

### Files
- `StudentService.java` – Remote interface
- `StudentServiceImpl.java` – Remote object implementation
- `RMIClient.java` – Client invoking remote methods

### Outcome
The RMI client successfully invokes remote methods and retrieves evaluation results from the cloud-hosted service.

---

## Execution Environment
- Server applications run on a cloud VM with a public IP
- Clients connect remotely using the VM’s public IP
- All executions are verified through terminal outputs

---

## Conclusion
This assignment successfully demonstrates:
- Remote communication using RPC and RMI
- Cloud-based deployment of distributed services
- Correct client–server interaction and result retrieval

All requirements of Assignment 1 are satisfied.
