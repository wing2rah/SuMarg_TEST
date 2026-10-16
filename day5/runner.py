import os
import sys

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")

import traci

def run_simulation():
    step = 0
    
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()  
        
        vehicle_ids = traci.vehicle.getIDList()
        
        for veh_id in vehicle_ids:
            speed_mps = traci.vehicle.getSpeed(veh_id)
            
            if veh_id == "car2":
                
                if step == 2:
                    print(f"\n---> Step 2: {veh_id} ki speed badhakar 20 m/s kar di gayi")
                    traci.vehicle.setSpeedMode(veh_id, 0)
                    traci.vehicle.setSpeed(veh_id, 20.0) 
                    
                elif step == 5:
                    print(f"\n---> Step 5: {veh_id} ko slow kiya ja raha hai (2 m/s)")
                    traci.vehicle.slowDown(veh_id, 2.0, 2)

                elif step == 8:
                    print(f"\n---> Step 8: {veh_id} ab normal AI control mein hai")
                    traci.vehicle.setSpeedMode(veh_id, 31)
                    traci.vehicle.setSpeed(veh_id, -1.0)
            
            speed_kmph = speed_mps * 3.6
            print(f"Step {step} | Vehicle ID: {veh_id} | Speed: {speed_kmph:.2f} km/h")
        
        step += 1

    traci.close()
    print("Simulation finished.")

if __name__ == "__main__":
    sumo_cfg_file = "test1.sumocfg"
    sumo_binary = "sumo-gui" 
    sumo_cmd = [sumo_binary, "-c", sumo_cfg_file]
    traci.start(sumo_cmd)
    run_simulation()