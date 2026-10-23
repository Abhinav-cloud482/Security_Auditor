Python Security Scanner

A lightweight Python-based TCP port scanner that checks selected common network ports on a specified IP address or localhost to identify services that may be accepting connections.

The project demonstrates basic network programming using Python's built-in socket module. It is designed for educational purposes, local security assessments, and authorized network troubleshooting.

Table of Contents
Overview
Features
Technology Stack
Project Structure
Prerequisites
Installation
Usage
Ports Scanned
How It Works
Sample Output
Troubleshooting
Security Considerations
Limitations
Future Enhancements
Contributing
License
Overview

Python Security Scanner is a command-line utility that tests a predefined list of TCP ports on a target host.

It attempts to establish a TCP connection to each configured port and reports ports that accept connections. Each connection attempt uses a timeout to limit how long the scanner waits for a response.

The application accepts an IP address or hostname as input. The hostname localhost is explicitly mapped to 127.0.0.1.

The project provides a simple introduction to TCP networking, socket programming, connection timeouts, exception handling, and basic network security assessment.

Features
TCP Port Scanning: Checks a predefined set of common TCP ports.
Open Port Detection: Identifies ports that accept TCP connections.
Hostname Resolution: Supports IP addresses and resolvable hostnames.
Localhost Support: Allows scanning the local machine using localhost.
Connection Timeout: Uses a 0.5-second timeout for individual connection attempts.
Error Handling: Handles hostname resolution errors and socket-related operating system errors.
Timestamped Output: Displays the date and time when the scan begins.
Lightweight Implementation: Uses Python's standard library without requiring third-party packages.
Technology Stack
Technology	Purpose
Python 3	Core application logic
socket	TCP connection testing and hostname resolution
datetime	Recording the scan start time
Project Structure
python-security-scanner/
├── security_auditor.py
├── README.md
├── LICENSE
└── requirements.txt


File descriptions

security_auditor.py — Main script that scans configured TCP ports and displays results.
README.md — Project documentation.
LICENSE — License terms, if an appropriate license has been added.
requirements.txt — Optional dependency documentation; no third-party Python packages are required.
Prerequisites

Before running the scanner, ensure that:

Python 3.8 or later is installed.
You have permission to test the target host.
The target IP address or hostname is valid and reachable where applicable.
Verify Python Installation
python --version


On Linux or macOS, you may need to use:

python3 --version

Installation
1. Clone the Repository

Replace YOUR_USERNAME with your GitHub username and use your actual repository name.

git clone https://github.com/YOUR_USERNAME/python-security-scanner.git

2. Navigate to the Project Directory
cd python-security-scanner

3. Check the Python Installation
python --version


No third-party packages or virtual environment are required to run the basic scanner.

Usage

Run the script from the project directory.

Windows
python security_auditor.py

Linux and macOS
python3 security_auditor.py


When prompted, enter an IP address or hostname that you own or are authorized to assess.

For example, to scan the local machine:

Enter your own device IP or localhost: localhost


To scan a specific authorized host:

Enter your own device IP or localhost: 192.168.1.10


Replace the example IP address with the address of your own device or an authorized test system.

The scanner tests the configured ports and prints those for which a TCP connection succeeds.

Ports Scanned

The current implementation checks the following ten TCP ports.

Port	Common Association
22	SSH
53	DNS
80	HTTP
135	Microsoft RPC
139	NetBIOS Session Service
443	HTTPS
445	SMB
3306	MySQL
3389	Remote Desktop Protocol
8080	Alternative HTTP services

These associations are conventional uses, not definitive service identifications. The scanner does not inspect application banners or verify which service is running on an open port.

The port list is defined in the common_ports variable in security_auditor.py. You can modify it to suit an authorized testing environment.

How It Works

The scanner follows a straightforward sequence:

Target Input: Requests an IP address or hostname from the user.
Localhost Normalization: Converts the input localhost to 127.0.0.1.
Scan Initialization: Prints the target, scan start time, and a separator.
Socket Creation: Creates a TCP socket for each configured port.
Connection Attempt: Calls connect_ex() to test whether a TCP connection can be established.
Open Port Reporting: Prints an [OPEN] message when a connection succeeds.
Error Handling: Reports hostname resolution failures or socket-related operating system errors.
Resource Cleanup: Closes each socket after the connection attempt.
Completion Message: Prints a completion message after the loop finishes.

Each connection attempt has a timeout of 0.5 seconds. Actual scan duration depends on network conditions, connection outcomes, and the operating system.

Sample Output

The following output is illustrative. Actual results depend on the target system and its network configuration.

Enter your own device IP or localhost: localhost

Python Security Scanner
Target: 127.0.0.1
Time: 2026-10-23 15:00:00
----------------------------------------
[OPEN] Port 80
[OPEN] Port 3306

Scan completed.


In this example, ports 80 and 3306 accepted TCP connections at the time of the scan.

If no ports accept connections, no [OPEN] entries are printed. The program still prints Scan completed. if it reaches the end of the loop without encountering an early return.

Understanding the Results
Open Port

An [OPEN] result means that the TCP connection attempt succeeded.

It does not necessarily mean that the service is vulnerable or improperly configured.

No Open Ports Reported

If the scanner does not report any open ports, possible explanations include:

None of the selected ports accept TCP connections.
A firewall or network security rule blocks the connection attempts.
The target is unreachable.
The relevant services are not running.
The response exceeds the configured timeout.

The current implementation does not distinguish all these conditions.

Hostname Resolution Error

If the target hostname cannot be resolved, the scanner prints an error message and stops the scan.

Other Socket Errors

If a socket-related operating system error occurs, the scanner displays an error message and stops processing the remaining ports.

Troubleshooting
Python Is Not Recognized

Cause: Python may not be installed or may not be included in the system PATH.

Resolution: Install Python from the official website and ensure the executable is available from your terminal.

https://www.python.org/downloads/

Invalid or Unresolvable Hostname

Cause: The hostname may be incorrect or DNS resolution may be unavailable.

Resolution: Verify the hostname or use the correct IP address of the authorized target.

No Open Ports Are Detected

Cause: The selected ports may be closed, filtered, unreachable, or not accepting connections.

Resolution: Verify that the target is correct and that the relevant services are expected to be listening. Use an authorized test environment to validate the scanner's behavior.

Scan Takes Longer Than Expected

Cause: Connection attempts may be waiting for the configured timeout.

Resolution: Review the socket timeout and the number of configured ports. Reducing the timeout may speed up scanning but can also cause responsive services on slow networks to be missed.

Security Considerations

This project is intended for educational use and authorized network diagnostics.

Scan only systems you own or have explicit permission to test.
Use the tool on localhost, personal lab machines, or approved test networks.
An open port is not proof of a security vulnerability.
Do not use scan results alone to determine whether a system is secure.
Follow applicable organizational policies and network testing rules.
Limitations

The current implementation has the following limitations:

Scans only a predefined list of ten TCP ports.
Does not support UDP scanning.
Does not identify services through banner grabbing or protocol inspection.
Does not perform vulnerability detection or exploitation.
Uses a fixed connection timeout of 0.5 seconds.
Does not distinguish reliably between filtered ports, unreachable hosts, and closed ports.
Stops the scan when a hostname resolution error or socket operating system error occurs.
Does not save scan results to a file.
Does not perform concurrent scanning.

These limitations reflect the project's current implementation rather than guaranteed features of a more advanced scanner.

Future Enhancements

Potential improvements include:

Configurable port ranges and custom port lists.
Command-line arguments for targets and timeout settings.
Optional concurrent TCP connection checks.
Structured logging and JSON or CSV report export.
Improved error classification and timeout reporting.
Optional service identification for authorized test environments.
Unit tests for socket handling and result processing.
Input validation for hostnames and port numbers.

These enhancements are proposals and are not implemented in the current script.

Contributing

Contributions, bug reports, and suggestions are welcome.

Fork the repository.
Create a feature branch.
Implement and test your changes.
Commit your changes with a descriptive message.
Submit a pull request describing the proposed improvements.

Please keep contributions focused on authorized network diagnostics and educational use.

License

This project is licensed under the MIT License, provided that a valid LICENSE file containing the MIT License text is included in the repository.

If no license file has been added, the project's license has not yet been formally specified.

Disclaimer

This project is provided for educational purposes and authorized network security assessment. It is a basic TCP connectivity scanner, not a comprehensive security auditing platform.

The author is not responsible for misuse of the software or for unauthorized scanning activities. Users are responsible for obtaining appropriate permission before testing any target system.