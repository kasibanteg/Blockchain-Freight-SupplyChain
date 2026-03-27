# Team10_2026SpringB_CSE540_Freight_Supply_Chain_Provenance_System
Blockchain-based freight supply chain system with Django backend, Ethereum smart contracts, Stripe payments, Ganache, Remix, MetaMask, PostgreeDB and real-time shipment tracking

## Overview
This project tracks freight shipments, booking confirmations, and payments using a hybrid architecture:
- **Django backend** for authentication, quotes, bookings, and system configuration (PostgreSQL DB)
- **Ethereum blockchain** for immutable storage of payments, shipment records, and status reports
- **Stripe** for fiat payments (credit/debit)
- **MetaMask + Remix** for Ethereum testnet interactions (optional ETH payments)

## Dependencies
- Python 3.11+
- Django 4.x
- PostgreSQL
- Web3.py
- Stripe API
- Remix IDE
- MetaMask Wallet
- Ganache local blockchain (for testing)

## Setup Instructions
1. Clone the repository
   ```bash
   git clone <repository_url>
