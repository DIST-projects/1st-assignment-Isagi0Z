# Assignment 2: Torrent-Based File Sharing in a Peer-to-Peer Environment

## Overview
This assignment demonstrates **peer-to-peer (P2P) file sharing** using BitTorrent technology. A torrent file is created for an academic document and distributed between peers to showcase decentralized file transfer and integrity verification.

The objective is to understand how torrent-based systems enable efficient file sharing without relying on a centralized server.

---

## Tools and Technologies
- **Torrent Client:** qBittorrent
- **Operating System:** Windows
- **File Shared:** Academic PDF document
- **Network Model:** Peer-to-Peer (P2P)

---

## Torrent Creation

### Description
A torrent file was created for an academic document titled:

**`Distributed_Systems_Unit1_Notes.pdf`**

The torrent contains metadata including file size, piece hashes, and tracker information.

### Output
- Torrent file generated successfully:
  - `DS_Unit1_Notes.torrent`

---

## Torrent Distribution

### Seeding
One peer acts as the **seeder**, making the file available to the network.

### Downloading
Another peer downloads the file using the torrent, establishing a peer-to-peer connection.

### File Integrity Verification
After download completion:
- The torrent client verifies all pieces
- File integrity is confirmed using hash checks
- The downloaded file matches the original source

---

## Observations
- Successful peer discovery and connection
- Stable download and upload speeds
- Complete and verified file transfer
- Seeder remains available after download completion

---

## Conclusion
This assignment successfully demonstrates:
- Torrent file creation
- Peer-to-peer file distribution
- Decentralized data transfer
- File integrity verification in BitTorrent systems

All requirements of Assignment 2 are fulfilled.
