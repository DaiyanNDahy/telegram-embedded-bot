# User Manual  
## Telegram-Based Raspberry Pi Device Control System

---

## 1. Introduction
This user manual provides step-by-step instructions on how to use the Telegram-Based Raspberry Pi Device Control System. The system allows users to remotely control and monitor hardware devices connected to a Raspberry Pi using Telegram commands.

The manual is intended for students, instructors, and general users with basic familiarity with smartphones and messaging applications.

---

## 2. System Requirements

### 2.1 Hardware Requirements
- Raspberry Pi (with GPIO support)
- Power supply for Raspberry Pi
- GPIO-connected devices (LED, Relay, Motor, Sensor, etc.)
- Internet connectivity

### 2.2 Software Requirements
- Raspberry Pi OS
- Python 3
- Telegram mobile or desktop application
- Telegram Bot Token (configured by system administrator)

---

## 3. System Overview

### 3.1 High-Level Workflow
1. User sends a command via Telegram (t.me/CSE_3200_bot)
2. Telegram Bot receives the command
3. Raspberry Pi processes the command
4. GPIO devices are controlled accordingly
5. System sends a response back to the user
