# SUMO & TraCI Python Integration

A minimal reference guide for controlling SUMO (Simulation of Urban MObility) traffic simulations using Python and the TraCI library.

## 📌 Prerequisites
- SUMO installed on your system.
- `SUMO_HOME` environment variable must be set.
- A valid SUMO configuration file (e.g., `my_network.sumocfg`).

## 🚀 Basic Setup & Connection
To connect your Python script to a running SUMO simulation:

```python
import os, sys, traci

# Setup SUMO_HOME path
tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
sys.path.append(tools)

# Start TraCI
traci.start(["sumo-gui", "-c", "my_network.sumocfg"])
```

## ⏱️ Understanding Steps
- **1 Step = 1 Second** (by default in simulation time).
- `traci.simulationStep()` advances the simulation by one step.

## 🚗 Core TraCI Commands Learned

### 1. Get Vehicle Information
Fetch live data from the simulation.
```python
vehicles = traci.vehicle.getIDList()         # Get IDs of all vehicles currently in network
speed = traci.vehicle.getSpeed("car2")       # Returns speed in m/s
edge = traci.vehicle.getRoadID("car2")       # Get current road (edge) ID
lane = traci.vehicle.getLaneID("car2")       # Get current lane ID
```

### 2. Vehicle Speed Control
Control vehicle behavior dynamically.
```python
# Set exact speed immediately (m/s)
traci.vehicle.setSpeed("car2", 20.0) 

# Smoothly slow down to target speed over X seconds
traci.vehicle.slowDown("car2", target_speed=5.0, duration=5) 

# Return control to normal AI behavior
traci.vehicle.setSpeed("car2", -1.0) 
```

### 3. Bypass Safety & Constant Speed
SUMO vehicles naturally fluctuate speed due to AI safety checks and human imperfection (`sigma`). To force a strict constant speed:
```python
# Mode 0: Ignore all safety checks (forced speed)
# Mode 32: Ignore random behavior (acts like a robot at exact speed)
# Mode 31: Default AI safety mode
traci.vehicle.setSpeedMode("car2", 32)
traci.vehicle.setSpeed("car2", 10.0)
```

## 📝 Minimalist Run Loop Example
```python
def run():
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        
        for veh_id in traci.vehicle.getIDList():
            # Example: Force constant speed at step 2
            if veh_id == "car2" and step == 2:
                traci.vehicle.setSpeedMode(veh_id, 32)
                traci.vehicle.setSpeed(veh_id, 15.0) # 15 m/s
                
        step += 1
    traci.close()
```