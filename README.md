Distributed Systems Assignments

Course: Distributed Systems
Student: Ratish S A
Assignments:

RPC & RMI in Cloud Environment

Torrent-based Peer-to-Peer File Sharing

Assignment 1: RPC and RMI in a Cloud Environment
Objective

To implement a distributed application using Remote Procedure Call (RPC) and Remote Method Invocation (RMI), where the server is hosted in a cloud environment (AWS EC2) and clients access services remotely.

Technologies Used

RPC: Python (XML-RPC)

RMI: Java

Cloud Platform: AWS EC2 (Ubuntu)

Client OS: Windows

Version Control: Git & GitHub

Project Structure
rpc-rmi-cloud-assignment-1/
│
├── rpc/
│   ├── server/
│   │   └── rpc_server.py
│   └── client/
│       └── rpc_client.py
│
├── rmi/
│   ├── common/
│   │   └── RideService.java
│   ├── server/
│   │   ├── RideServiceImpl.java
│   │   └── RMIServer.java
│   └── client/
│       └── RideClient.java
│
├── screenshots/
│   ├── ec2_instance_running.png
│   ├── rpc_server_running.png
│   ├── rpc_client_output.png
│   ├── rmi_server_output.png
│   └── rmi_client_output.png

RPC Implementation (Python)
Description

A Python XML-RPC server is hosted on an AWS EC2 instance.

The client runs locally and remotely invokes procedures on the server.

Remote Procedures

calculate_fare(distance, time)

assign_driver(location)

estimate_eta(distance)

Output

Successful remote procedure invocation

Correct results returned from the cloud-hosted server

📸 Screenshots included in /screenshots folder.

RMI Implementation (Java)
Description

A Java RMI server is deployed on AWS EC2.

The client runs locally and invokes remote methods using RMI registry.

RMI Components

Remote Interface: RideService

Implementation: RideServiceImpl

Server: RMIServer

Client: RideClient

Output

Successful remote method invocation

Correct responses returned from the cloud server

📸 Screenshots included in /screenshots folder.

Cloud Deployment Details

AWS EC2 instance (Ubuntu)

Required ports opened in Security Group:

RPC: 8000

RMI: 1099

Server accessed via Public IPv4 address

Assignment 2: Torrent-Based Peer-to-Peer File Sharing
Objective

To demonstrate peer-to-peer computing by creating and distributing a torrent file using BitTorrent concepts.

Tools Used

Torrent Client: qBittorrent

Tracker: Public tracker

Environment: Local system (No cloud required)

Project Structure
Torrent_Assignment-2/
│
├── bigfile.bin
├── bigfile.bin.torrent
├── Understanding_Artificial_Intelligence.pdf
├── Outputs/
│   ├── torrentextract.png
│   ├── torrentcomplete.png
│   └── Screenshot_2026-02-02.png
└── README.md

Torrent Creation

Selected a file to share

Generated .torrent file

Configured tracker information

Torrent Distribution

One peer acted as seeder

Another peer downloaded the file

File integrity verified automatically by the torrent client

Output

Successful .torrent creation

Successful file sharing

100% verified download

📸 Screenshots included in /Outputs folder.

Learning Outcomes

Understanding of RPC and RMI concepts

Hands-on experience with cloud deployment

Understanding peer-to-peer systems

Practical knowledge of torrent-based file sharing

Experience using GitHub for assignment submission
