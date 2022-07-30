# IoT

Table of Contents
1. [What is IoT?](#what-is-iot) <br>
2. [Node Constraints](#node-constraints) <br>
3. [Network Constraints](#network-constraints) <br>
4. [IoT VS Traditional Internet](#iot-vs-traditional-internet) <br>
5. [IoT Three Layer Architecture](#iot-three-layer-architecture) <br>
    5.1 [Perception Layer](#perception-layer-sensor-layer) <br>
    5.2 [Network Layer](#network-layer-transmission-layer) <br>
    5.3 [Application Layer](#application-layer-business-layer) <br>
6. [Lessons Learned](#lessons-learned)
---

# TL:DR
Perception Layer: 
    Targeting Availbility, eavesdropping, data capture false & manipulating

Network Layer:
    Targeting Routing Table, Authentication, Impersonation, forcing data to go through malicious network

Application Layer:
    Phishing attacks

---

## What is IoT?

* IoT (Internet of Things) are devices that are connected to the Internet, collecting and sharing data

* Connecting different objects and add sensors, gives a level of intelligence to devices. Enabling them to communicate real-time data without humans

* Types(Heterogeneity) of IoT:
    1. High-end: Laptop, Smartphone
    2. Low-end: Sensors, Actuators
    3. Passive: Barcode, QR-codes, RFID

* Heterogeneity of networks:
    1. Wireless
    2. Wired

<br>

---

<br>

## Node Constraints

* Constrained Nodes have the following properties (RFC7228): 
    1. Maximum code complexity (ROM/Flash)
    2. Size of state and buffers (RAM)
    3. Amount of computation feasible in period of time (CPU)
    4. Available power (Power Supply)
    5. UI and accessibility (Software update, set keys)

<br>

---

<br>

## Network Constraints

* Low bitrate/throughput (limits on duty cycle)
* High packet loss and high variablity of packet loss (delivery rate)
* Highly asymmetric link characteristics (delay, jitter, loss)
* Severe penalties for larger packets (high packet loss due to link-layer fragmentation)
* Limits on reachability over time (Devices going to sleep, wake up to communicate for short period of time)
* Lack of advanced services (IP multicast)

<br>

---

<br>

## IoT VS Traditional Internet

|                     | IoT                                                        | Traditional Internet        |
|---------------------|------------------------------------------------------------|-----------------------------|
| Data Creation       | Create data about individual's behaviours and analyse them | Humans create internet      |
| Content Consumption | Pushing information and triggering actions                 | Sending requests            |
| Content Combining   | By explicitly defined operations (Event-Driven Patterns)   | By explicitly defined links |
| Value               | Action and Timely information                              | Right answers for queries   |

<br>

---

<br>

## IoT Three Layer Architecture

<br>

### Perception Layer (Sensor Layer)

* Bottom layer
* Contains sensors and actuators
* Connect things into IoT network
* Measure, collect and process information from sensors
* Send data into upper layer via layer interfaces

* Enabling Technologies:
    1. RFID
        * Identify and track objects and exchange data 
        
        1. RFID tags 
            * Attached in an object with unique ID
        2. RFID readers
            * Identify object and obtain information by querying tags via signal
        3. Antennas
            * Transmit signals between RFID tags and RFID readers

        * Benefits:
            1. Fast scanning
            2. Durability
            3. Reusability
            4. Large storage
            5. Noncontact reading
            6. Small size
            7. Low cost
    
    <br>

    2. Wireless Sensor Networks (WSN)
        * Monitor and track status of devices, transmit status data to control center via multiple hops

        * Bridge between real world and cyber world

        * Benefits:
            1. Scalability
            2. Dynamic reconfiguratoin
            3. Reliability
            4. Small size
            5. Low cost
            6. Low energy consumption

    <br>

    * RFID: Mainly for objection identification
    * WSN: Perception of real-world physical parameters within surrounding environment

<br>

* Threats:
    1. Node capture:
        * Capture and control of nodes by physically replacing node or tampering with hardware of node
        * Communication key, radio key, matching key can be exposed to attacker
        * Can copy important information with captured node to malicious node
        * Serious impact on network

        * Defense:
            * Effective schemes to monitor and detect malicious nodes

    <br>

    2. Code Injection:
        * Code injection into memory of node
        * Can grant full access to attacker into IoT system

        * Defense:
            * Effective code authentication schemes
        
    <br>

    3. False data injection:
        * Inject false data instead of real data into captured node
        * IoT application will provide wrong services, affecting IoT system

        * Defense:
            * False data filtering schemes, detect and drop false data before sending to IoT application (Recall: Stuxnet)

    <br>

    4. Cryptanalysis & side channel:
        * Use obtained ciphertext/plaintext to infer encrpytion key in encryption algorithm

        * Side channel to assist attacker

        * Defense:
            * Efficient and secure encryption algorithms and key management schemes 
    
    <br>

    5. Eavesdropping & Interferences:
        & Information delivered in wirelesslink can be eavesdropped
        * Attacker send noise data/signal to intefere with information delivered in wireless link

        * Defense:
            * Secure encryption algorithm and key management schemes
            * Efficient secure noise filtering schemes
    
    <br>

    6. Sleep deprivations:
        * Nodes are programmed to follow sleep cycle to reduce power consumption
        * Attacker breaked programmed sleep routines and keep devices awake till shut down

        * Defense:
            * Energy harvest schemes (E.g. Solar panels)
            * Secured duty-cycle mechanisms
       
<br>

---

<br>

### Network Layer (Transmission Layer)

* Middle layer (Important layer, devices and communication technologies are integrated into this layer)
* Receive data from [Perception Layer](#perception-layer-sensor-layer)
* Determine routes to transmit data and information to [Application Layer](#application-layer-business-layer) via integegrated network
* Send data to and fro through interfaces/gateways among heterogeneous networks, using various communication technologies and protocols


* Enabling Technologies:
    * IEEE 802.15.4
        * Protocol for physical layer and MAC layer in wireless personal area networks (WPANs)

        * Focus on low rate WPANs, providing low rate connection of all things in personal area with low energy consumption, low cost and low rate transmission

    1. 6LoWPAN
        * Transmit IPv6 packets over IEEE 802.15.4 networks

        * Benefits:
            1. Great connectivity & compatibility with legacy architectures
            2. Low energy consumption
            3. Ad-hoc self-organization
    
    <br>

    2. ZigBee
        * Designed for short-term communication with low-energy consumption
        * Supports multiple topologies
            1. Star Tree
            2. Mesh 

        * Benefits:
            1. Low energy consumption
            2. Low cost
            3. Low data rate
            4. Low complexity
            5. Reliablity and security
    
    <br>
    
    3. 5G Network
        * eMBB (Enhanced Mobile Broadband): 
            * Extreme fast data speeds, 20x faster than 4G

        * mMTC (Massive machine-type communications):
            * Up to 100x more connected device/unit area than 4G

        * URLLC (Ultra-reliable low latency communications):
            * Latency of 1ms

        * Benefits:
            1. IoT friendly ecosystem, with vast improvements over 4G
            2. 90% reduction in network energy usage, up to 10 years worth of battery life for low power IoT devices
        
        * Design:
            1. Flexibility:
                * Wide rage of carrier frequencies
                * Different deployment types
                * Diverse use case

            2. Forward compatibility:
                * 3GPP taking phased approach of New Radio (NR) standardization
            
            3. Ultra-lean design:
                1. Minimising "always on" transmission. 
                2. Transmit signals only when needed

<br>

* Threats:
    1. DoS:
        * Common attacks 
        * Ping of Death, TearDrop, UDP Flood, SYN Flood, Land Attack

        * Defense:
            * Investigating attack schemes carefully to design efficient defense schemes

    2. Sinkhole/Wormhole:
        * Sinkhole:
            * Compromised node claims exceptional capabilities of power, computation and communication
            * Cause neighboring nodes to select compromised node as forwarding node in data routing

        * Wormhole:
            * 2 or more compromised nodes claim special capabilities of power, computation and communication
            * In different location
            * Cause exchange routing information with private links to acheieve false reduce hop transmission
            * Compromised node can increase data obtain before reaching IoT application
            * Breaks confidentiality of data

        * Defense:
            * Modify routing protocols to enhance route selection process
            * Deploy secure hardware

    3. MITM:
        * Malicious device controlled by adversary located between 2 devices
        * Stealing identity of 2 normal devices, malicious device act as middle man to store and forward data
        * Breaks confidentiality, integrity and privacy of restricted data

        * Defense:
            * Use secure communication protocols & key management schemes (TLS)

    4. Sybil:
        * 1 device with multiple identities
        * False data send by sybil device can be easily accepted by benign neighbouring device
        * Routes that uses sybil device as forwarding node think there are several different path but only have 1 path
        * All transmitted data goes through sybil, jamming and DoS can be used

        * Defense:
            * Secure identifcation and authentication

<br>

---

<br>

### Application Layer (Business Layer)

* Top layer
* Receives data transmitted from [Network Layer](#network-layer-transmission-layer)
* Uses data to provide services or operations
* E.g.:
    1. Provide storage services to backup receive data into database
    2. Provide anaylsis service by evaluating received data

<br>

* Enabling Technologies:
    1. CoAP (Constrained Application Protocol)
        * Messaging protocol in Application Layer
        * Modified verion of HTTP to suit IoT
        * Group communication and push notification supported (Except broadcast)

    2. MQTT (Message Queuing Telemetry Transport)
        * Lightweight protocol, low bandwidth and power consumption
        * Publish-Subscribe paradigm
        * Subscriber subscribes to topic
        * Publisher publishes message with a topic, subscriber receives message

<br>

* Threats:
    1. Phishing:
        * Attacker tries to steal identity of user via infected emails and phishing sites

        * Defense:
            * Secure authrorisation access, identification and authentication
            * Ensure users stay vigilant while surfing web, IoT may make this impossible
<br>

---

<br>

## Lessons Learned

* Missing Key Management
    * Same global AES key shared among bulbs to encrypt traffic
    * Capture 1 node to reveal global key

<br>

* Insecure Default Settings and Passwords
    * Webcome from Foscam, Linksys and Panasonic cameras 
        * Insecure default credentials: `admin`, `root`
        * Default password: `1234<blank>`

    * Foscam used hard-coded credentials/password in firmware

<br>

* Missing Communication Security
    * Vulnerablities found in networked traffic signal system in US
    * Wireless communication not encrypted
    * Radio uses default username/password
    * Settings can be configured remotely
    * FTP connection to write config files

<br>

* Physical Attacks
    * Attack vectors
        * Extract keys, config data, firmware images
        * Use of debug/test interfaces and sniffing on inter-bus communication interfaces like Serial Peripheral Interface (SPI) or Inter-Integrated Circuit (I2C)
        * Key extraction with in a trusted execution environment using power analysis or fault injection attacks

<br>

* DOS Attack
    * Malware that targets IP Camera, home routers, turning them into bots
    * Infected devices used to launch DDoS

<br>

* Reccomended Practices
    * Encrypt communications to avoid pervasive monitoring and eavesdropping
    * Use TLS/DTLS for secure communication channel
    * Use authentication and authorisation solution
    * Follow key length reccomendation (112-bit symmetric key)
    * Support automatic key management
    * Automatic software update mechanism
    * Reduce physical attack surface
        1. Crypto implmentation that consider side channel attacks
        2. Disable debug facilities before launching product
        3. Hardware-based crypto support
        4. Memory Protection Unit (MPU) integration

