#equipment_status = status_system_live_feed      #hypothetical status-feed from monitoring systems
equipment_status = ["ok", "ok", "faulty", "ok", "ok", "ok"]
index = 0
# equipment_status.remove("faulty")    #testing purposes with no system faults
# equipment_status.append("ok")        #testing purposes with no system faults
for status in equipment_status:
    if status != "faulty":
        index += 1
        print(f"\nThe equipment status in postion {index} is: ok")
    else:
        index += 1
        print(f"\nAlert! There is a faulty piece of equipment located at position {index} on the production line.")