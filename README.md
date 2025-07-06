Real-Time Clock and Temperature Monitoring System

This project simulates a real-time clock and temperature monitoring system using **Cisco Packet Tracer** and embedded Python. The system monitors temperature levels and displays warning messages when it exceeds predefined thresholds.

Aim
To design and simulate a real-time temperature monitoring system with a clock and automatic control system using Cisco Packet Tracer.

Problem Statement
Develop a system that:
- Continuously monitors temperature
- Displays a real-time clock
- Automatically turns ON a Heater or AC based on temperature
- Displays warnings or mode changes on an LCD or serial output.

Scope of the Solution
- Simulates a smart environment (like a smart room)
- Helps in automating temperature regulation
- Can be extended for home automation, IoT, and energy efficiency

Required Component

Software
- Cisco Packet Tracer
- Embedded Python (inside MCU in CPT)

Hardware (Simulated in Packet Tracer)
- Microcontroller (MCU)
- Temperature Sensor
- LEDs (for Heater/AC indicators)
- LCD or Serial Terminal
- Resistors, wires, breadboard

Logic Description
- If temperature ≥ **506** → AC ON
- If temperature ≤ **504** → Heater ON
- Between 504–506 → Normal Mode
- Time is tracked using `millis()` to simulate a clock
- Output is printed with `[hh:mm:ss]` format

Project Structure
real-time-temp-monitor/
├── code/
│ └── main.py # Python logic for MCU
├── circuit/
│ └── simulation.pkt # Cisco Packet Tracer simulation file
│ └── circuit_diagram.png # Screenshot of the simulated circuit
├── assets/
│ └── demo_video.mp4 # Demo video (optional)
├── report.pdf # Project report (optional)
└── README.md # This file


