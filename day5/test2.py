import traci as t


def run_sim():
    step=0
    while t.simulation.getMinExpectedNumber()>0:
        t.simulationStep()
        vehicle=t.vehicle.getIDList()
        for vid in vehicle:
            print(vid)
            speed=t.vehicle.getSpeed(vid)
            print(speed*3.6)
            print("\n")
        
        step+=1
    t.close()

if __name__ == "__main__":
    t.start(["sumo","-c","test2.sumocfg"])
    run_sim()