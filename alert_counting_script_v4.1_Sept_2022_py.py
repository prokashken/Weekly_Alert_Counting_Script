import pandas as pd
col_list = ["Message", "Status"]
df = pd.read_csv("finalAlertData.csv", usecols=col_list)
#print(df)
#df.to_string("outfile")


df.to_csv(r'Device', header=None, index=None, sep='\t', mode='a')

listOfM = []
line_count = 0
sentry = 0


        
with open('Device', 'r') as f:  
    for line in f.readlines():
        listOfM.append(line)
        line_count = line_count + 1 
        
for item in listOfM:
    if 'Sentry' in item :
        sentry += 1

#print("Total_Sentry_alerts : ",sentry)
        
print("Total Week alerts : ", len(df)-sentry)

#print(" Total Week alerts : ",line_count)   
#*****************************************Charging_Part_Start_From_Here*****************************************
#print(listOfM)       
# For chargers ****************************************************************
print("                                 Charging_Part ")
offline_charger_count = 0
offline_charger_closed_cout = 0


for item in listOfM:
    if 'Error Charger' in item :
        offline_charger_count += 1

print("Total_Offline_charger : ",offline_charger_count)

for item in listOfM:
    if 'Error Charger' in item and 'closed' in item :
        offline_charger_closed_cout += 1

n = offline_charger_count - offline_charger_closed_cout

print("offline_charger_closed : ",offline_charger_closed_cout)
#print("\n")
print("offline_charger_open : ",n)        
print("\n")
# For connectors *****************************************************************

offline_connector_count = 0
offline_connector_closed_cout = 0


for item in listOfM:
    if 'Error Connector' in item :
        offline_connector_count += 1

print("Total_offline_connector : ",offline_connector_count)

for item in listOfM:
    if 'Error Connector' in item and 'closed' in item :
        offline_connector_closed_cout += 1

l = offline_connector_count - offline_connector_closed_cout

print("offline_connector_closed : ",offline_connector_closed_cout)
#print("\n")
print("offline_connector_open : ",l)     
print("\n")
# For Offline Device ************************************************************

offline_device_count = 0
offline_device_closed_cout = 0

for item in listOfM:
    if 'is offline' in item :
        offline_device_count += 1

print("Total_device_offline : ",offline_device_count)

for item in listOfM:
    if 'is offline' in item and 'closed' in item :
        offline_device_closed_cout += 1

m = offline_device_count - offline_device_closed_cout

print("offline_device_closed : ",offline_device_closed_cout)
print("offline_device_open : ",m)
print("\n")
#total_alert = offline_charger_count + offline_connector_count + offline_device_count
#print("Total_alert : ",total_alert)
#print("\n")

#For Error checking the devices****************************************************************************

error_checking_device_count = 0
error_checking_device_closed_cout = 0

for item in listOfM:
    if 'Error checking the devices' in item :
        error_checking_device_count += 1

print("Total_error_checking_device : ",error_checking_device_count)

for item in listOfM:
    if 'Error checking the devices' in item and 'closed' in item :
        error_checking_device_closed_cout += 1

m = error_checking_device_count - error_checking_device_closed_cout

print("error_checking_device_closed : ",error_checking_device_closed_cout)
print("error_checking_device_open : ",m)
print("\n")

#For Controller Offline Alerts****************************************************************************
controller_offline_alert_count = 0
controller_offline_alert_closed_count = 0

for item in listOfM:
    if 'Controller' in item and 'offline' in item :
        controller_offline_alert_count += 1

print("Total_Controller_Offline_Alert : ",controller_offline_alert_count)

for item in listOfM:
    if 'Controller' in item and 'offline' in item and 'closed' in item :
        controller_offline_alert_closed_count += 1

m = controller_offline_alert_count - controller_offline_alert_closed_count

print("Controller_Offline_Alert_Closed : ",controller_offline_alert_closed_count)
print("Controller_Offline_Alert_Open : ",m)
print("\n")

total_alert = offline_charger_count + offline_connector_count + offline_device_count + controller_offline_alert_count
print("Total_alert : ",total_alert)
print("\n")

#*****************************************Charging_Part_End_From_Here*****************************************


#*****************************************Grid_De_start_From_Here*****************************************
#################GRID COUNT########################################
print("                                 Grid_Part(DE) ")
print("\n"*2)
esspower_response_metrics = 0
esspower_response_metrics_closed = 0
for item in listOfM:
    if 'ESSpower response metrics' in item :
        esspower_response_metrics += 1

print("ESSpower response metrics : ",esspower_response_metrics)

for item in listOfM:
    if 'ESSpower response metrics' in item and 'closed' in item :
        esspower_response_metrics_closed += 1

m = esspower_response_metrics - esspower_response_metrics_closed

print("ESSpower response metrics closed : ",esspower_response_metrics_closed)
print("ESSpower response metrics open : ",m)
print("\n")
###############################
    
#ESS discharging power
ess_discharging_power = 0
ess_discharging_power_closed = 0
for item in listOfM:
    if 'ESS discharging power' in item :
        ess_discharging_power += 1

print("ESS discharging power : ",ess_discharging_power)

for item in listOfM:
    if 'ESS discharging power' in item and 'closed' in item :
        ess_discharging_power_closed += 1

m = ess_discharging_power - ess_discharging_power_closed

print("ESS discharging power closed: ",ess_discharging_power_closed)
print("ESS discharging power open : ",m)
print("\n")
###############################

#ESS charging power
ess_charging_power = 0
ess_charging_power_closed = 0
for item in listOfM:
    if 'ESS charging power' in item :
        ess_charging_power += 1

print("ESS charging power : ",ess_charging_power)

for item in listOfM:
    if 'ESS charging power' in item and 'closed' in item :
        ess_charging_power_closed += 1

m = ess_charging_power - ess_charging_power_closed

print("ESS charging power closed : ",ess_charging_power_closed)
print("ESS charging power open : ",m)
print("\n")
###############################

#TSO:SkynetOffline
tso_SkynetOffline = 0
tso_SkynetOffline_closed = 0
for item in listOfM:
    if 'SkynetOffline' in item :
        tso_SkynetOffline += 1

print("TSO:SkynetOffline : ",tso_SkynetOffline)

for item in listOfM:
    if 'SkynetOffline' in item and 'closed' in item :
        tso_SkynetOffline_closed += 1

m = tso_SkynetOffline - tso_SkynetOffline_closed

print("TSO:SkynetOffline closed : ",tso_SkynetOffline_closed)
print("TSO:SkynetOffline open : ",m)
print("\n")
###############################

#General error safety contact
general_error_safety_contact = 0
general_error_safety_contact_closed = 0
for item in listOfM:
    if 'General error safety contact' in item :
        general_error_safety_contact += 1

print("General error safety contact : ",general_error_safety_contact)

for item in listOfM:
    if 'General error safety contact' in item and 'closed' in item :
        general_error_safety_contact_closed += 1

m = general_error_safety_contact - general_error_safety_contact_closed

print("General error safety contact closed : ",general_error_safety_contact_closed)
print("General error safety contact open : ",m)
print("\n")
###############################

#ESS SOCs 
ess_socs = 0
ess_socs_closed = 0
for item in listOfM:
    if 'ESS SOCs' in item :
        ess_socs += 1

print("ESS SOCs : ",ess_socs)

for item in listOfM:
    if 'ESS SOCs' in item and 'closed' in item :
        ess_socs_closed += 1

m = ess_socs - ess_socs_closed

print("ESS SOCs closed : ",ess_socs_closed)
print("ESS SOCs open : ",m)
print("\n")
###############################

#Requested FCR power is zero for de_amprion
fcr_zero = 0
fcr_zero_closed = 0
for item in listOfM:
    if 'Requested FCR power is zero for de_amprion' in item :
        fcr_zero += 1

print("Requested FCR power is zero for de_amprion : ",fcr_zero)

for item in listOfM:
    if 'Requested FCR power is zero for de_amprion' in item and 'closed' in item :
        fcr_zero_closed += 1

m = fcr_zero - fcr_zero_closed

print("Requested FCR power is zero for de_amprion closed : ",fcr_zero_closed)
print("Requested FCR power is zero for de_amprion open : ",m)
print("\n")
###############################

#Backup for de
backup_de = 0
backup_de_closed = 0
for item in listOfM:
    if 'Backup is active for de_amprion' in item :
        backup_de += 1

print("Backup for de : ",backup_de)

for item in listOfM:
    if 'Backup is active for de_amprion' in item and 'closed' in item :
        backup_de_closed += 1

m = backup_de - backup_de_closed

print("Backup for de closed : ",backup_de_closed)
print("Backup for de open : ",m)
print("\n")
###############################

#AC grid undervoltage shutdown
ac_grid = 0
ac_grid_closed = 0
for item in listOfM:
    if 'grid undervoltage' in item or 'grid overvoltage' in item :
        ac_grid += 1

print("AC grid undervoltage shutdown : ",ac_grid)

for item in listOfM:
    if ('grid undervoltage' in item or 'grid overvoltage' in item) and 'closed' in item :
        ac_grid_closed += 1

m = ac_grid - ac_grid_closed

print("AC grid undervoltage shutdown closed : ",ac_grid_closed)
print("AC grid undervoltage shutdown open : ",m)
print("\n")
####################################

#Fire detection triggered / Facility: Grid- and system protection triggered
fire_detection = 0
fire_detection_closed = 0
for item in listOfM:
    if 'Fire detection triggered' in item or 'Fire detection triggered' in item or 'Grid- and system protection triggered' in item or 'Power failure' in item or 'Emergency Stop triggered for this system' in item or 'Emergency Stop triggered' in item or 'Fire detection system not available' in item :
        fire_detection += 1

print("Fire detection triggered / Facility: Grid- and system protection triggered : ",fire_detection)

for item in listOfM:
    if ('Fire detection triggered' in item or 'Fire detection triggered' in item or 'Grid- and system protection triggered' in item or 'Power failure' in item or 'Emergency Stop triggered for this system' in item or 'Emergency Stop triggered' in item or 'Fire detection system not available' in item) and 'closed' in item :
        fire_detection_closed += 1

m = fire_detection - fire_detection_closed

print("Fire detection triggered / Facility: Grid- and system protection triggered : ",fire_detection_closed)
print("Fire detection triggered / Facility: Grid- and system protection triggered : ",m)
print("\n")
total_alert_de1 = esspower_response_metrics + ess_discharging_power + ess_charging_power + tso_SkynetOffline + tso_SkynetOffline + general_error_safety_contact + ess_socs + fcr_zero + backup_de + ac_grid + fire_detection
#print("Total Grid_DE Alert : ",total_alert_de1)
print("\n")

print("88888888888888888 Critical Storage section start 8888888888888")
#New Alert are add In 6.02.2022

#5.1
new_5_1 = 0
new_5_1_closed = 0
for item in listOfM:
    if 'DC source missing' in item or 'undervoltage intermediate circuit' in item :
        new_5_1 += 1

print(" Total Inverter: DC source missing/ undervoltage intermediate circuit : ",new_5_1)

for item in listOfM:
    if ('DC source missing' in item or 'undervoltage intermediate circuit' in item) and 'closed' in item :
        new_5_1_closed += 1

m = new_5_1 - new_5_1_closed

print("Total Inverter: DC source missing/ undervoltage intermediate circuit closed : ",new_5_1_closed)
print("Total Inverter: DC source missing/ undervoltage intermediate circuit open : ",m)
print("\n")


#5.2

new_5_2 = 0
new_5_2_closed = 0
for item in listOfM:
    if 'kill-switch tripped' in item :
        new_5_2 += 1

print(" Total Inverter: kill-switch tripped : ",new_5_2)

for item in listOfM:
    if 'kill-switch tripped' in item and 'closed' in item :
        new_5_2_closed += 1

m = new_5_2 - new_5_2_closed

print("Total Inverter: kill-switch tripped closed : ",new_5_2_closed)
print("Total Inverter: kill-switch tripped open : ",m)
print("\n")

#5.3

new_5_3 = 0
new_5_3_closed = 0
for item in listOfM:
    if 'Discrepancy error inverter revision' in item :
        new_5_3 += 1

print(" Total Discrepancy error inverter revision: ",new_5_3)

for item in listOfM:
    if 'Discrepancy error inverter revision' in item and 'closed' in item :
        new_5_3_closed += 1

m = new_5_3 - new_5_3_closed

print("Total Discrepancy error inverter revision closed : ",new_5_3_closed)
print("Total Discrepancy error inverter revision open : ",m)
print("\n")


#5.4

new_5_4 = 0
new_5_4_closed = 0
for item in listOfM:
    if 'Master contactor stuck battery unit' in item :
        new_5_4 += 1

print(" Total Master contactor stuck battery unit: ",new_5_4)

for item in listOfM:
    if 'Master contactor stuck battery unit' in item and 'closed' in item :
        new_5_4_closed += 1

m = new_5_4 - new_5_4_closed

print("Total Master contactor stuck battery unit closed : ",new_5_4_closed)
print("Total Master contactor stuck battery unit open : ",m)
print("\n")


#5.5

new_5_5 = 0
new_5_5_closed = 0
for item in listOfM:
    if 'Discrepancy error master contactor' in item :
        new_5_5 += 1

print(" Total Discrepancy error master contactor: ",new_5_5)

for item in listOfM:
    if 'Discrepancy error master contactor' in item and 'closed' in item :
        new_5_5_closed += 1

m = new_5_5 - new_5_5_closed

print("Total Discrepancy error master contactor closed : ",new_5_5_closed)
print("Total Discrepancy error master contactor open : ",m)
print("\n")


#5.6

new_5_6 = 0
new_5_6_closed = 0
for item in listOfM:
    if 'Isolation faulty' in item :
        new_5_6 += 1

print(" Total Isolation faulty: ",new_5_6)

for item in listOfM:
    if 'Isolation faulty' in item and 'closed' in item :
        new_5_6_closed += 1

m = new_5_6 - new_5_6_closed

print("Total Isolation faulty closed : ",new_5_6_closed)
print("Total Isolation faulty open : ",m)
print("\n")


#5.7

new_5_7 = 0
new_5_7_closed = 0
for item in listOfM:
    if 'Isolation critical' in item :
        new_5_7 += 1

print(" Total Isolation critical: ",new_5_7)

for item in listOfM:
    if 'Isolation critical' in item and 'closed' in item :
        new_5_7_closed += 1

m = new_5_7 - new_5_7_closed

print("Total Isolation critical closed : ",new_5_7_closed)
print("Total Isolation critical open : ",m)
print("\n")


#5.8


new_5_8 = 0
new_5_8_closed = 0
for item in listOfM:
    if 'Communication timeout BMC (CAN) <-> BMS' in item :
        new_5_8 += 1

print(" Total Communication timeout BMC (CAN) <-> BMS: ",new_5_8)

for item in listOfM:
    if 'Communication timeout BMC (CAN) <-> BMS' in item and 'closed' in item :
        new_5_8_closed += 1

m = new_5_8 - new_5_8_closed

print("Total Communication timeout BMC (CAN) <-> BMS closed : ",new_5_8_closed)
print("Total Communication timeout BMC (CAN) <-> BMS open : ",m)
print("\n")


#5.9

new_5_9 = 0
new_5_9_closed = 0
for item in listOfM:
    if 'Communication timeout BMC (UDP) <-> BMS' in item :
        new_5_9 += 1

print(" Total Communication timeout BMC (UDP) <-> BMS: ",new_5_9)

for item in listOfM:
    if 'Communication timeout BMC (UDP) <-> BMS' in item and 'closed' in item :
        new_5_9_closed += 1

m = new_5_9 - new_5_9_closed

print("Total Communication timeout BMC (UDP) <-> BMS closed : ",new_5_9_closed)
print("Total Communication timeout BMC (UDP) <-> BMS open : ",m)
print("\n")


#5.10

new_5_10 = 0
new_5_10_closed = 0
for item in listOfM:
    if 'Communication timeout inverter CAN (battery) <-> BMS' in item :
        new_5_10 += 1

print(" Total Communication timeout inverter CAN (battery) <-> BMS: ",new_5_10)

for item in listOfM:
    if 'Communication timeout inverter CAN (battery) <-> BMS' in item and 'closed' in item :
        new_5_10_closed += 1

m = new_5_10 - new_5_10_closed

print("Total Communication timeout inverter CAN (battery) <-> BMS closed : ",new_5_10_closed)
print("Total Communication timeout inverter CAN (battery) <-> BMS open : ",m)
print("\n")

#5.11

new_5_11 = 0
new_5_11_closed = 0
for item in listOfM:
    if 'Communication timeout inverter CAN (bms) <-> BMS' in item :
        new_5_11 += 1

print(" Total Communication timeout inverter CAN (bms) <-> BMS: ",new_5_11)

for item in listOfM:
    if 'Communication timeout inverter CAN (bms) <-> BMS' in item and 'closed' in item :
        new_5_11_closed += 1

m = new_5_11 - new_5_11_closed

print("Total Communication timeout inverter CAN (bms) <-> BMS closed : ",new_5_11_closed)
print("Total Communication timeout inverter CAN (bms) <-> BMS open : ",m)
print("\n")


#5.12


new_5_12 = 0
new_5_12_closed = 0
for item in listOfM:
    if 'Revision switch inverter active' in item :
        new_5_12 += 1

print(" Total Revision switch inverter active: ",new_5_12)

for item in listOfM:
    if 'Revision switch inverter active' in item and 'closed' in item :
        new_5_12_closed += 1

m = new_5_12 - new_5_12_closed

print("Total Revision switch inverter active closed : ",new_5_12_closed)
print("Total Revision switch inverter active open : ",m)
print("\n")



#5.13

new_5_13 = 0
new_5_13_closed = 0
for item in listOfM:
    if 'Converter general error' in item :
        new_5_13 += 1

print(" Total Converter general error: ",new_5_13)

for item in listOfM:
    if 'Converter general error' in item and 'closed' in item :
        new_5_13_closed += 1

m = new_5_13 - new_5_13_closed

print("Total Converter general error closed : ",new_5_13_closed)
print("Total Converter general error open : ",m)
print("\n")

#5.14


new_5_14 = 0
new_5_14_closed = 0
for item in listOfM:
    if 'Max SOC exceeded' in item :
        new_5_14 += 1

print(" Total Max SOC exceeded: ",new_5_14)

for item in listOfM:
    if 'Max SOC exceeded' in item and 'closed' in item :
        new_5_14_closed += 1

m = new_5_14 - new_5_14_closed

print("Total Max SOC exceeded closed : ",new_5_14_closed)
print("Total Max SOC exceeded open : ",m)
print("\n")


#5.15

new_5_15 = 0
new_5_15_closed = 0
for item in listOfM:
    if 'Min SOC fallen below' in item :
        new_5_15 += 1

print(" Total Min SOC fallen below: ",new_5_15)

for item in listOfM:
    if 'Min SOC fallen below' in item and 'closed' in item :
        new_5_15_closed += 1

m = new_5_15 - new_5_15_closed

print("Total Min SOC fallen below closed : ",new_5_15_closed)
print("Total Min SOC fallen below open : ",m)
print("\n")


#5.16

#Communication timeout Inverter <-> BMS


new_5_16 = 0
new_5_16_closed = 0
for item in listOfM:
    if 'Communication timeout Inverter <-> BMS' in item :
        new_5_16 += 1

print(" Total Communication timeout Inverter <-> BMS: ",new_5_16)

for item in listOfM:
    if 'Communication timeout Inverter <-> BMS' in item and 'closed' in item :
        new_5_16_closed += 1

m = new_5_16 - new_5_16_closed

print("Total Communication timeout Inverter <-> BMS closed : ",new_5_16_closed)
print("Total Communication timeout Inverter <-> BMS open : ",m)
print("\n")





#4.1
# Breaker tripped

new_4_1 = 0
new_4_1_closed = 0
for item in listOfM:
    if 'Breaker tripped' in item :
        new_4_1 += 1

print(" Total Breaker tripped: ",new_4_1)

for item in listOfM:
    if 'Breaker tripped' in item and 'closed' in item :
        new_4_1_closed += 1

m = new_4_1 - new_4_1_closed

print("Total Breaker tripped closed : ",new_4_1_closed)
print("Total Breaker tripped open : ",m)
print("\n")


#4.2

# Overvoltage DC

new_4_2 = 0
new_4_2_closed = 0
for item in listOfM:
    if 'Overvoltage DC' in item :
        new_4_2 += 1

print(" Total Overvoltage DC: ",new_4_2)

for item in listOfM:
    if 'Overvoltage DC' in item and 'closed' in item :
        new_4_2_closed += 1

m = new_4_2 - new_4_2_closed

print("Total Overvoltage DC closed : ",new_4_2_closed)
print("Total Overvoltage DC open : ",m)
print("\n")


#4.3

new_4_3 = 0
new_4_3_closed = 0
for item in listOfM:
    if 'Overvoltage intermediate circuit' in item :
        new_4_3 += 1

print(" Total Overvoltage intermediate circuit: ",new_4_3)

for item in listOfM:
    if 'Overvoltage intermediate circuit' in item and 'closed' in item :
        new_4_3_closed += 1

m = new_4_3 - new_4_3_closed

print("Total Overvoltage intermediate circuit closed : ",new_4_3_closed)
print("Total Overvoltage intermediate circuit open : ",m)
print("\n")

#4.4


new_4_4 = 0
new_4_4_closed = 0
for item in listOfM:
    if 'Max charge current exceeded' in item or 'Max discharge current exceeded' in item :
        new_4_4 += 1

print(" Total Max charge current exceeded: ",new_4_4)

for item in listOfM:
    if ('Max charge current exceeded' in item or 'Max discharge current exceeded' in item) and 'closed' in item :
        new_4_4_closed += 1

m = new_4_4 - new_4_4_closed

print("Total Max charge current exceeded closed : ",new_4_4_closed)
print("Total Max charge current exceeded open : ",m)
print("\n")


#4.5


new_4_5 = 0
new_4_5_closed = 0
for item in listOfM:
    if 'Max frequency exceeded' in item :
        new_4_5 += 1

print(" Total Overvoltage DC: ",new_4_5)

for item in listOfM:
    if 'Max frequency exceeded' in item and 'closed' in item :
        new_4_5_closed += 1

m = new_4_5 - new_4_5_closed

print("Total Max frequency exceeded closed : ",new_4_5_closed)
print("Total Max frequency exceeded open : ",m)
print("\n")


#4.6


new_4_6 = 0
new_4_6_closed = 0
for item in listOfM:
    if 'Min Frequency fallen below' in item :
        new_4_6 += 1

print(" Total Min Frequency fallen below: ",new_4_6)

for item in listOfM:
    if 'Min Frequency fallen below' in item and 'closed' in item :
        new_4_6_closed += 1

m = new_4_6 - new_4_6_closed

print("Total Min Frequency fallen below closed : ",new_4_6_closed)
print("Total Min Frequency fallen below open : ",m)
print("\n")


#4.7

new_4_7 = 0
new_4_7_closed = 0
for item in listOfM:
    if 'Temperature sensor fault' in item :
        new_4_7 += 1

print(" Total Temperature sensor fault: ",new_4_7)

for item in listOfM:
    if 'Temperature sensor fault' in item and 'closed' in item :
        new_4_7_closed += 1

m = new_4_7 - new_4_7_closed

print("Total Temperature sensor fault closed : ",new_4_7_closed)
print("Total Temperature sensor fault open : ",m)
print("\n")

#4.8

new_4_8 = 0
new_4_8_closed = 0
for item in listOfM:
    if 'Overtemperature shutdown' in item :
        new_4_8 += 1

print(" Total Overtemperature shutdown: ",new_4_8)

for item in listOfM:
    if 'Overtemperature shutdown' in item and 'closed' in item :
        new_4_8_closed += 1

m = new_4_8 - new_4_8_closed

print("Total Overtemperature shutdown closed : ",new_4_8_closed)
print("Total Overtemperature shutdown open : ",m)
print("\n")

#4.9

new_4_9 = 0
new_4_9_closed = 0
for item in listOfM:
    if 'AC gird overload >125%' in item or 'AC gird overload >110%' in item or 'AC gird overload >100%' in item or 'AC overcurrent shutdown' in item :
        new_4_9 += 1

print(" Total AC gird overload: ",new_4_9)

for item in listOfM:
    if ('AC gird overload >125%' in item or 'AC gird overload >110%' in item or 'AC gird overload >100%' in item or 'AC overcurrent shutdown' in item) and 'closed' in item :
        new_4_9_closed += 1

m = new_4_9 - new_4_9_closed

print("Total AC gird overload closed : ",new_4_9_closed)
print("Total AC gird overload open : ",m)
print("\n")


#4.10

new_4_10 = 0
new_4_10_closed = 0
for item in listOfM:
    if 'Transmission error transducer' in item :
        new_4_10 += 1

print(" Total Transmission error transducer: ",new_4_10)

for item in listOfM:
    if 'Transmission error transducer' in item  and 'closed' in item :
        new_4_10_closed += 1

m = new_4_10 - new_4_10_closed

print("Total Transmission error transducerclosed : ",new_4_10_closed)
print("Total Transmission error transducer open : ",m)
print("\n")


#4.11
# PC-Alive error

new_4_11 = 0
new_4_11_closed = 0
for item in listOfM:
    if 'PC-Alive error' in item :
        new_4_11 += 1

print(" Total PC-Alive error: ",new_4_11)

for item in listOfM:
    if 'PC-Alive error' in item and 'closed' in item :
        new_4_11_closed += 1

m = new_4_11 - new_4_11_closed

print("Total PC-Alive error closed : ",new_4_11_closed)
print("Total PC-Alive error open : ",m)
print("\n")

#4.12


new_4_12 = 0
new_4_12_closed = 0
for item in listOfM:
    if 'Master contactor stuck' in item and not 'battery unit' in item :
        new_4_12 += 1

print(" Total Master contactor stuck: ",new_4_12)

for item in listOfM:
    if ('Master contactor stuck' in item and not 'battery unit' in item) and 'closed' in item :
        new_4_12_closed += 1

m = new_4_12 - new_4_12_closed

print("Total Master contactor stuck closed : ",new_4_12_closed)
print("Total Master contactor stuck open : ",m)
print("\n")


#4.13


new_4_13 = 0
new_4_13_closed = 0
for item in listOfM:
    if 'Filter charge contactor stuck' in item :
        new_4_13 += 1

print(" Total Filter charge contactor stuck: ",new_4_13)

for item in listOfM:
    if 'Filter charge contactor stuck' in item and 'closed' in item :
        new_4_13_closed += 1

m = new_4_13 - new_4_13_closed

print("Total Filter charge contactor stuck closed : ",new_4_13_closed)
print("Total Filter charge contactor stuck open : ",m)
print("\n")

#4.14

new_4_14 = 0
new_4_14_closed = 0
for item in listOfM:
    if 'Battery CAN connexion failure' in item :
        new_4_14 += 1

print(" Total Battery CAN connexion failure: ",new_4_14)

for item in listOfM:
    if 'Battery CAN connexion failure' in item and 'closed' in item :
        new_4_14_closed += 1

m = new_4_14 - new_4_14_closed

print("Total Battery CAN connexion failure closed : ",new_4_14_closed)
print("Total Battery CAN connexion failure open : ",m)
print("\n")


#4.15

new_4_15 = 0
new_4_15_closed = 0
for item in listOfM:
    if 'PLS alive error' in item :
        new_4_15 += 1

print(" Total PLS alive error: ",new_4_15)

for item in listOfM:
    if 'PLS alive error' in item and 'closed' in item :
        new_4_15_closed += 1

m = new_4_15 - new_4_15_closed

print("Total PLS alive error closed : ",new_4_15_closed)
print("Total PLS alive error open : ",m)
print("\n")

#4.16

new_4_16 = 0
new_4_16_closed = 0
for item in listOfM:
    if 'Discrepancy error inverter revision' in item :
        new_4_16 += 1

print(" Total Discrepancy error inverter revision: ",new_4_16)

for item in listOfM:
    if 'Discrepancy error inverter revision' in item and 'closed' in item :
        new_4_16_closed += 1

m = new_4_16 - new_4_16_closed

print("Total Discrepancy error inverter revision closed : ",new_4_16_closed)
print("Total Discrepancy error inverter revision open : " ,m)

print("\n")
print("\n")
print("\n")



total_critical_storage_alert = new_5_1+new_5_2+new_5_3+new_5_4+new_5_5+new_5_6+new_5_7+new_5_8+new_5_9+new_5_10+new_5_11+new_5_12+new_5_13+new_5_14+new_5_15+new_5_16+new_4_1+new_4_2+new_4_3+new_4_4+new_4_5+new_4_6+new_4_7+new_4_8+new_4_9+new_4_10+new_4_11+new_4_12+new_4_13+new_4_14+new_4_15+new_4_16
total_critical_storage_alert_closed = new_5_1_closed+new_5_2_closed+new_5_3_closed+new_5_4_closed+new_5_5_closed+new_5_6_closed+new_5_7_closed+new_5_8_closed+new_5_9_closed+new_5_10_closed+new_5_11_closed+new_5_12_closed+new_5_13_closed+new_5_14_closed+new_5_15_closed+new_5_16_closed+new_4_1_closed+new_4_2_closed+new_4_3_closed+new_4_4_closed+new_4_5_closed+new_4_6_closed+new_4_7_closed+new_4_8_closed+new_4_9_closed+new_4_10_closed+new_4_11_closed+new_4_12_closed+new_4_13_closed+new_4_14_closed+new_4_15_closed+new_4_16_closed
total_critical_storage_alert_open = total_critical_storage_alert - total_critical_storage_alert_closed
print("Total critical_storage : ",total_critical_storage_alert)
print("Total critical_storage_closed : ",total_critical_storage_alert_closed)
print("Total critical_storage_open : ",total_critical_storage_alert_open)
print("\n")
print("88888888888888888 Critical Storage section End 8888888888888")
print("\n")

new_6 = 0
new_6_closed = 0
for item in listOfM:
    if 'External backup required for de_amprion' in item :
        new_6 += 1

print(" Total External backup required for de_amprion: ",new_6)

for item in listOfM:
    if 'External backup required for de_amprion' in item and 'closed' in item :
        new_6_closed += 1

m = new_6 - new_6_closed

print("Total External backup required for de_amprion closed : ",new_6_closed)
print("Total External backup required for de_amprion open : " ,m)

print("\n")
#6.1
new_6_1 = 0
new_6_1_closed = 0
for item in listOfM:
    if "Unit set 'de_amprion' under energy capacity" in item :
        new_6_1 += 1

print(" Total Unit set 'de_amprion' under energy capacity: ",new_6_1)

for item in listOfM:
    if "Unit set 'de_amprion' under energy capacity" in item and 'closed' in item :
        new_6_1_closed += 1

m = new_6_1 - new_6_1_closed

print("Total Unit set 'de_amprion' under energy capacity closed : ",new_6_1_closed)
print("Total Unit set 'de_amprion' under energy capacity open : " ,m)
print("\n")

#6.2
new_6_2 = 0
new_6_2_closed = 0
for item in listOfM:
    if "Unit set 'de_amprion' under required power" in item :
        new_6_2 += 1

print(" Total Unit set 'de_amprion' under required power: ",new_6_2)

for item in listOfM:
    if "Unit set 'de_amprion' under required power" in item and 'closed' in item :
        new_6_2_closed += 1

m = new_6_2 - new_6_2_closed

print("Total Unit set 'de_amprion' under required power closed : ",new_6_2_closed)
print("Total Unit set 'de_amprion' under required power open : " ,m)
print("\n")
print("\n")


total_grid_DE_Orginal = total_alert_de1 + total_critical_storage_alert + new_6 + new_6_1 + new_6_2
print("\n")
print("\n")
print("Total _Grid_DE_Alert : ", total_grid_DE_Orginal)
print("\n")
print("\n")
































































































#*******************************************AA_start_Frome_Here*******************************************************
print("                                           Grid_AA")
print("\n"*2)
#storage Control Storage status error Storage
#Critical storage error The storage system reports a 
#PRL Power Error The amount of power the storage can
#Storage System Error GENERAL_PCS_FAULT
#Storage Control Lost connection to storage System not alive
#Storage power response incorrect Storage is not responding to power requests correctly
#Storage System Error GENERAL_BATTERY_ALARM
#Storage System Error GENERAL_DANGER
#Control Storage status error Storage status error
#Storage System Error GENERAL_BATTERY_FAULT
#Storage System Error GENERAL_COMMUNICATION_FAULT
#Relay cannot reach the unit for nl_tennet
#AcknowledgementDocument tag not found [sentry]
#Failure report from TMH Allocation Agent
#[Prometheus]: tmh.orange.arena has very high memory usage. Memory usage is (>70%)


control_storage_count  = 0
critical_storage_count = 0
prl_power_error_count  = 0
general_pcs_count      = 0
control_lost_count     = 0
storage_power_count    = 0
general_battery_count  = 0
general_danger_count   = 0
control_storage_staus_count = 0
general_battery_fault_count = 0
general_communication_count=0
relay_count            = 0
sentry_count           = 0
orange_count           = 0
tmh_allocation_count   = 0

control_storage_closed  = 0
critical_storage_closed = 0
prl_power_error_closed  = 0
general_pcs_closed      = 0
control_lost_closed     = 0
storage_power_closed    = 0
general_battery_closed  = 0
general_danger_closed   = 0
control_storage_staus_closed = 0
general_battery_fault_closed = 0
general_communication_closed=0
relay_closed            = 0
sentry_closed           = 0
orange_closed           = 0
tmh_allocation_closed   = 0


#Critical storage error The storage system reports a ***********************************************

for item in listOfM:
    if 'Critical storage error The storage system reports a' in item :
        critical_storage_count += 1

print("Total_Critical storage error The storage system reports a : ",critical_storage_count)

for item in listOfM:
    if 'Critical storage error The storage system reports a' in item and 'closed' in item :
         critical_storage_closed += 1

sce = critical_storage_count  - critical_storage_closed

print("Closed : ",critical_storage_closed)
print("Open : ",sce)
print("\n") 


#PRL Power Error The amount of power the storage can************************


for item in listOfM:
    if 'PRL Power Error The amount of power the storage can' in item :
        prl_power_error_count += 1

print("Total_PRL Power Error The amount of power the storage can : ",prl_power_error_count)

for item in listOfM:
    if 'PRL Power Error The amount of power the storage can' in item and 'closed' in item :
         prl_power_error_closed += 1

ppe = prl_power_error_count  - prl_power_error_closed

print("Closed : ",prl_power_error_closed)
print("Open : ",ppe)
print("\n") 

#Storage System Error GENERAL_PCS_FAULT*******************************

for item in listOfM:
    if 'Storage System Error GENERAL_PCS_FAULT' in item :
        general_pcs_count += 1

print("Total_Storage System Error GENERAL_PCS_FAULT : ",general_pcs_count)

for item in listOfM:
    if 'Storage System Error GENERAL_PCS_FAULT' in item and 'closed' in item :
         general_pcs_closed += 1

gpc = general_pcs_count  - general_pcs_closed

print("Closed : ",general_pcs_closed)
print("Open : ",gpc)
print("\n") 

#Storage Control Lost connection to storage System not alive*****************

for item in listOfM:
    if 'Storage Control Lost connection to storage System not alive' in item :
        control_lost_count += 1

print("Total_Storage Control Lost connection to storage System not alive : ",control_lost_count)

for item in listOfM:
    if 'Storage Control Lost connection to storage System not alive' in item and 'closed' in item :
         control_lost_closed += 1

clc = control_lost_count - control_lost_closed

print("Closed : ",control_lost_closed)
print("Open : ",clc)
print("\n") 

#Storage power response incorrect Storage is not responding to power requests correctly*********

for item in listOfM:
    if 'Storage power response incorrect Storage is not responding to power requests correctly' in item :
        storage_power_count += 1

print("Total_Storage power response incorrect Storage is not responding to power requests correctly : ",storage_power_count)

for item in listOfM:
    if 'Storage power response incorrect Storage is not responding to power requests correctly' in item and 'closed' in item :
         storage_power_closed += 1

spc = storage_power_count - storage_power_closed

print("Closed : ",storage_power_closed)
print("Open : ",spc)
print("\n") 


#Storage System Error GENERAL_BATTERY_ALARM***************

for item in listOfM:
    if 'Storage System Error GENERAL_BATTERY_ALARM' in item :
        general_battery_count += 1

print("Total_Storage System Error GENERAL_BATTERY_ALARM : ",general_battery_count)

for item in listOfM:
    if 'Storage System Error GENERAL_BATTERY_ALARM' in item and 'closed' in item :
         general_battery_closed += 1

gbc = general_battery_count - general_battery_closed

print("Closed : ",general_battery_closed)
print("Open : ",gbc)
print("\n") 

#Storage System Error GENERAL_DANGER*******************

for item in listOfM:
    if 'Storage System Error GENERAL_DANGER' in item :
        general_danger_count += 1

print("Total_Storage System Error GENERAL_DANGER : ",general_danger_count)

for item in listOfM:
    if 'Storage System Error GENERAL_DANGER' in item and 'closed' in item :
         general_danger_closed += 1

gdc = general_danger_count - general_danger_closed

print("Closed : ",general_danger_closed)
print("Open : ",gdc)
print("\n") 

#Storage Control Storage status error Storage status error*******************

for item in listOfM:
    if 'Control Storage status error Storage status error' in item :
        control_storage_staus_count += 1

print("Total_Control Storage status error Storage status error : ",control_storage_staus_count)

for item in listOfM:
    if 'Control Storage status error Storage status error' in item and 'closed' in item :
         control_storage_staus_closed += 1

css = control_storage_staus_count - control_storage_staus_closed

print("Closed : ",control_storage_staus_closed)
print("Open : ",css)
print("\n") 

#Storage Storage System Error GENERAL_BATTERY_FAULT*******************

for item in listOfM:
    if 'Storage System Error GENERAL_BATTERY_FAULT' in item :
        general_battery_fault_count += 1

print("Total_Storage System Error GENERAL_BATTERY_FAULT : ",general_battery_fault_count)

for item in listOfM:
    if 'Storage System Error GENERAL_BATTERY_FAULT' in item and 'closed' in item :
         general_battery_fault_closed += 1

gbf = general_battery_fault_count - general_battery_fault_closed

print("Closed : ",general_battery_fault_closed)
print("Open : ",gbf)
print("\n") 

#Storage System Error GENERAL_COMMUNICATION_FAULT*******************

for item in listOfM:
    if 'Storage System Error GENERAL_COMMUNICATION_FAULT' in item :
        general_communication_count += 1

print("Total_Storage System Error GENERAL_COMMUNICATION_FAULT : ",general_communication_count)

for item in listOfM:
    if 'Storage System Error GENERAL_COMMUNICATION_FAULT' in item and 'closed' in item :
         general_communication_closed += 1

gcc = general_communication_count - general_communication_closed

print("Closed : ",general_communication_closed)
print("Open : ",gcc)
print("\n") 

#Relay cannot reach the unit for nl_tennet********************

for item in listOfM:
    if 'Relay cannot reach the unit for nl_tennet' in item :
        relay_count += 1

print("Total_Relay cannot reach the unit for nl_tennet : ",relay_count)

for item in listOfM:
    if 'Relay cannot reach the unit for nl_tennet' in item and 'closed' in item :
         relay_closed += 1

rc = relay_count - relay_closed

print("Closed : ",relay_closed)
print("Open : ",rc)
print("\n") 

#AcknowledgementDocument tag not found [sentry]


for item in listOfM:
    if 'AcknowledgementDocument tag not found' in item and '[sentry]' in item :
        sentry_count += 1

print("Total_AcknowledgementDocument tag not found [sentry] : ",sentry_count)

for item in listOfM:
    if 'AcknowledgementDocument tag not found' in item and '[sentry]' in item and 'closed' in item :
         sentry_closed += 1

sen = sentry_count - sentry_closed

print("Closed : ",sentry_closed)
print("Open : ",sen)
print("\n") 


#[Prometheus]: tmh.orange.arena has very high memory usage. Memory usage is (>70%)


for item in listOfM:
    if 'tmh.orange.arena has very high memory usage. Memory usage is' in item :
        orange_count += 1

print("Total_tmh.orange.arena has very high memory usage. Memory usage is : ",orange_count)

for item in listOfM:
    if 'tmh.orange.arena has very high memory usage. Memory usage is' in item and 'closed' in item :
         orange_closed += 1

ora = orange_count - orange_closed

print("Closed : ",orange_closed)
print("Open : ",ora)
print("\n") 





#Failure report from TMH Allocation Agent**************

for item in listOfM:
    if 'Failure report from TMH Allocation Agent' in item :
        tmh_allocation_count += 1

print("Total_Failure report from TMH Allocation Agent : ",tmh_allocation_count)

for item in listOfM:
    if 'Failure report from TMH Allocation Agent' in item and 'closed' in item :
         tmh_allocation_closed += 1

tmh = tmh_allocation_count - tmh_allocation_closed

print("Closed : ",tmh_allocation_closed)
print("Open : ",tmh)
print("\n") 
print("Total_Grid_AA_Alert : ",control_storage_count+critical_storage_count+prl_power_error_count+general_pcs_count+control_lost_count+storage_power_count+general_battery_count+general_danger_count+relay_count+sentry_count+tmh_allocation_count+orange_count+control_storage_staus_count+general_battery_fault_count+general_communication_count)

print("\n"*2)
#*******************************************Tokai-1_start_Frome_Here*******************************************************
print("                                         Tokai-1:")
print("\n"*2)
#[Tokai1_Douai TU4]: Communications; TU_OBI_ComFlt; TU - At least one loss of comunication
#[Tokai1_Douai TU4]: Environmental; ESS_OBI_0251TT1_HumidTH; ESS - High Humidity
#[Tokai1_Douai TU1]: Battery Fault; Rack_2 Warning- ; Ra2 - At least one warning
#[Tokai2_Elverlingsen_2]: Inverter Fault; INVERTER_9_GRID_FAULT  Inverter 9 has a grid fault or cannot connect
#Unit set 'fr.rte.tokai1' under required power from 2021-10-08 06:45:00+00:00 till 2021-10-08 07:00:00+00:00!
#[Tokai2_Elverlingsen_5]: Safety; Fire AlarmA fire has been detected in the battery container
safty_count                     = 0
Communication_count             = 0
Environmetal_count              = 0
Battery_fault_count             = 0
Inverter_fault_count            = 0
Controller_count                = 0
Unit_set_frrte_tokai1_count     = 0
Prod_has_lost_connection_count  = 0

safty_closed_count                     = 0
Communication_closed_count             = 0
Environmetal_closed_count              = 0
Battery_fault_closed_count             = 0
Inverter_fault_closed_count            = 0
Controller_closed_count                = 0
Unit_set_frrte_tokai1_closed_count     = 0
Prod_has_lost_connection_closed_count  = 0



#                         ***Safty***

for item in listOfM:
    if 'Tokai1_Douai' in item and 'Safety;' in item :
        safty_count += 1

print("Total_safty : ",safty_count)

for item in listOfM:
    if 'Tokai1_Douai' in item and 'Safety;' in item and 'closed' in item :
         safty_closed_count += 1

com = safty_count  - safty_closed_count

print("safty_closed : ",safty_closed_count)
print("safty_open : ",com)
print("\n") 

#                           ***Communication***



for item in listOfM:
    if 'Tokai1_Douai' in item and 'Communications;' in item :
        Communication_count += 1

print("Total_Communication : ",Communication_count)

for item in listOfM:
    if 'Tokai1_Douai' in item and 'Communications;' in item and 'closed' in item :
         Communication_closed_count += 1

com = Communication_count  - Communication_closed_count

print("Communication_closed : ",Communication_closed_count)
print("Communication_open : ",com)
print("\n")        

#                ***Environmental***

for item in listOfM:
    if 'Tokai1_Douai' in item and 'Environmental;' in item :
        Environmetal_count += 1

print("Total_Environmental : ",Environmetal_count)

for item in listOfM:
    if 'Tokai1_Douai' in item and 'Environmental;' in item and 'closed' in item :
         Environmetal_closed_count += 1

env = Environmetal_count - Environmetal_closed_count

print("Environmental_closed : ",Environmetal_closed_count)
print("Environmental_open : ",env)
print("\n")        

#                  ***Battary Fault***

for item in listOfM:
    if 'Tokai1_Douai' in item and 'Battery Fault;' in item :
        Battery_fault_count += 1

print("Total_Battery_Fault : ",Battery_fault_count)

for item in listOfM:
    if 'Tokai1_Douai' in item and 'Battery Fault;' in item and 'closed' in item :
         Battery_fault_closed_count += 1

bat = Battery_fault_count - Battery_fault_closed_count

print("Battery_Fault_closed : ",Battery_fault_closed_count)
print("Battery_Fault_open : ",bat)
print("\n")        

#                 ***Inverter_fault***


for item in listOfM:
    if 'Tokai1_Douai' in item and 'Inverter Fault;' in item :
        Inverter_fault_count += 1

print("Total_Inverter_fault : ",Inverter_fault_count)

for item in listOfM:
    if 'Tokai1_Douai' in item and 'Inverter Fault;' in item and 'closed' in item :
         Inverter_fault_closed_count += 1

inv = Inverter_fault_count - Inverter_fault_closed_count

print("Inverter_fault_closed : ",Inverter_fault_closed_count)
print("Inverter_fault_open : ",inv)
print("\n")

#                ***Controller***


for item in listOfM:
    if 'Tokai1_Douai' in item and 'Controller' in item :
        Controller_count += 1

print("Total_Controller : ",Controller_count)

for item in listOfM:
    if 'Tokai1_Douai' in item and 'Controller' in item and 'closed' in item :
         Controller_closed_count += 1

con = Controller_count - Controller_closed_count

print("Controller_closed : ",Controller_closed_count)
print("Controller_open : ",con)
print("\n")

#                           ***Unit set 'fr.rte.tokai1'***



for item in listOfM:
    if "Unit set 'fr.rte.tokai1'" in item :
        Unit_set_frrte_tokai1_count += 1

print("Total_Unit_set_frrte_tokai1 : ",Unit_set_frrte_tokai1_count)

for item in listOfM:
    if "Unit set 'fr.rte.tokai1'" in item and 'closed' in item :
         Unit_set_frrte_tokai1_closed_count += 1

uni = Unit_set_frrte_tokai1_count - Unit_set_frrte_tokai1_closed_count

print("Unit_set_frrte_tokai1_closed : ",Unit_set_frrte_tokai1_closed_count)
print("Unit_set_frrte_tokai1 : ",uni)
print("\n")


#                               ***Prod:has lost connection***



for item in listOfM:
    if 'prod d28f9121016df6a206832d26f99d8e9c: has lost connection' in item or 'prod 124ea21a09aaaf34607e9aaa2cc36c53: has lost connection' in item or 'prod a40222bd7b99ebc06a8d935b3a26fce3: has lost connection' in item or 'prod e4110f1463cbc5f40d485428a48c7976: has lost connection' in item :
        Prod_has_lost_connection_count += 1

print("Total_Prod_has_lost_connection_tokai1 : ",Prod_has_lost_connection_count)

for item in listOfM:
    if ('prod d28f9121016df6a206832d26f99d8e9c: has lost connection' in item or 'prod 124ea21a09aaaf34607e9aaa2cc36c53: has lost connection' in item or 'prod a40222bd7b99ebc06a8d935b3a26fce3: has lost connection' in item or 'prod e4110f1463cbc5f40d485428a48c7976: has lost connection' in item) and 'closed' in item :
         Prod_has_lost_connection_closed_count += 1

prod = Prod_has_lost_connection_count - Prod_has_lost_connection_closed_count

print("Prod_has_lost_connection_tokai1_closed : ",Prod_has_lost_connection_closed_count)
print("Prod_has_lost_connection_tokai1_open : ",prod)
print("\n")
print("Total_Tokai1_alert : ",safty_count+Communication_count+Environmetal_count+Battery_fault_count+Inverter_fault_count+Controller_count+Unit_set_frrte_tokai1_count+Prod_has_lost_connection_count)

print("\n"*2)
#*******************************************Tokai-1_END_Here*******************************************************

#*******************************************Tokai-2_Start**********************************************************
print("                                         Tokai-2:")
print("\n"*2)
safty_count                     = 0
Communication_count             = 0
Environmetal_count              = 0
Battery_fault_count             = 0
Inverter_fault_count            = 0
Controller_count                = 0
Unit_set_de_amp_tokai2_count    = 0
Prod_has_lost_connection_count  = 0

safty_closed_count                     = 0
Communication_closed_count             = 0
Environmetal_closed_count              = 0
Battery_fault_closed_count             = 0
Inverter_fault_closed_count            = 0
Controller_closed_count                = 0
Unit_set_de_amp_tokai2_closed_count    = 0
Prod_has_lost_connection_closed_count  = 0



#                         ***Safty***

for item in listOfM:
    if 'Tokai2' in item and 'Safety;' in item :
        safty_count += 1

print("Total_safty : ",safty_count)

for item in listOfM:
    if 'Tokai2' in item and 'Safety;' in item and 'closed' in item :
         safty_closed_count += 1

com = safty_count  - safty_closed_count

print("safty_closed : ",safty_closed_count)
print("safty_open : ",com)
print("\n") 

#                           ***Communication***



for item in listOfM:
    if 'Tokai2' in item and 'Communications;' in item :
        Communication_count += 1

print("Total_Communication : ",Communication_count)

for item in listOfM:
    if 'Tokai2' in item and 'Communications;' in item and 'closed' in item :
         Communication_closed_count += 1

com = Communication_count  - Communication_closed_count

print("Communication_closed : ",Communication_closed_count)
print("Communication_open : ",com)
print("\n")        

#                ***Environmental***

for item in listOfM:
    if 'Tokai2' in item and 'Environmental;' in item :
        Environmetal_count += 1

print("Total_Environmental : ",Environmetal_count)

for item in listOfM:
    if 'Tokai2' in item and 'Environmental;' in item and 'closed' in item :
         Environmetal_closed_count += 1

env = Environmetal_count - Environmetal_closed_count

print("Environmental_closed : ",Environmetal_closed_count)
print("Environmental_open : ",env)
print("\n")        

#                  ***Battary Fault***

for item in listOfM:
    if 'Tokai2' in item and 'Battery Fault;' in item :
        Battery_fault_count += 1

print("Total_Battery_Fault : ",Battery_fault_count)

for item in listOfM:
    if 'Tokai2' in item and 'Battery Fault;' in item and 'closed' in item :
         Battery_fault_closed_count += 1

bat = Battery_fault_count - Battery_fault_closed_count

print("Battery_Fault_closed : ",Battery_fault_closed_count)
print("Battery_Fault_open : ",bat)
print("\n")        

#                 ***Inverter_fault***


for item in listOfM:
    if 'Tokai2' in item and 'Inverter Fault' in item :
        Inverter_fault_count += 1

print("Total_Inverter_fault : ",Inverter_fault_count)

for item in listOfM:
    if 'Tokai2' in item and 'Inverter Fault' in item and 'closed' in item :
         Inverter_fault_closed_count += 1

inv = Inverter_fault_count - Inverter_fault_closed_count

print("Inverter_fault_closed : ",Inverter_fault_closed_count)
print("Inverter_fault_open : ",inv)
print("\n")

#                ***Controller***
#[Tokai2_Elverlingsen_3]: ESS heartbeat errors above threshold!

for item in listOfM:
    if ('ESS heartbeat errors above threshold' in item or 'ESS charging power response' in item or 'deviations above threshold' in item or 'ESS discharging power response deviations above threshold' in item or 'SoC is outside boundaries' in item or 'ESS SOCs above max healthy SOC above threshold' in item or 'Controller;' in item) and 'Tokai2' in item :
        Controller_count += 1

print("Total_Controller : ",Controller_count)

for item in listOfM:
    if ('ESS heartbeat errors above threshold' in item or 'ESS charging power response' in item or 'deviations above threshold' in item or 'ESS discharging power response deviations above threshold' in item or 'SoC is outside boundaries' in item or 'ESS SOCs above max healthy SOC above threshold' in item or 'Controller;' in item) and 'Tokai2' in item and 'closed' in item :
         Controller_closed_count += 1

con = Controller_count - Controller_closed_count

print("Controller_closed : ",Controller_closed_count)
print("Controller_open : ",con)
print("\n")

#                           ***de_amp_tokai2_elv_01' under energy capacity'***



for item in listOfM:
    if "Unit set 'de_amp_tokai2_elv_01' under energy capacity" in item or "Unit set 'de_amp_tokai2_elv_01' under required power" in item or "Unit set 'de_amp_tokai2_elv_02' under energy capacity" in item or "Unit set 'de_amp_tokai2_elv_02' under required power" in item or "Unit set 'de_amp_tokai2_elv_03' under energy capacity" in item or "Unit set 'de_amp_tokai2_elv_03' under required power" in item or "Unit set 'de_amp_tokai2_elv_04' under energy capacity" in item or "Unit set 'de_amp_tokai2_elv_04' under required power" in item or "Unit set 'de_amp_tokai2_elv_05' under energy capacity" in item or "Unit set 'de_amp_tokai2_elv_05' under required power" in item or "Unit set 'de_amp_tokai2_elv_06' under energy capacity" in item or "Unit set 'de_amp_tokai2_elv_06' under required power" in item or "Unit set 'de_amp_tokai2_elv_07' under energy capacity" in item or "Unit set 'de_amp_tokai2_elv_07' under required power" in item or "Unit set 'de_amp_tokai2_elv_08' under energy capacity" in item or "Unit set 'de_amp_tokai2_elv_08' under required power" in item :
        Unit_set_de_amp_tokai2_count += 1

print("Total_Unit_set_de_amp_tokai2 : ",Unit_set_de_amp_tokai2_count)

for item in listOfM:
    if ("Unit set 'de_amp_tokai2_elv_01' under energy capacity" in item or "Unit set 'de_amp_tokai2_elv_01' under required power" in item or "Unit set 'de_amp_tokai2_elv_02' under energy capacity" in item or "Unit set 'de_amp_tokai2_elv_02' under required power" in item or "Unit set 'de_amp_tokai2_elv_03' under energy capacity" in item or "Unit set 'de_amp_tokai2_elv_03' under required power" in item or "Unit set 'de_amp_tokai2_elv_04' under energy capacity" in item or "Unit set 'de_amp_tokai2_elv_04' under required power" in item or "Unit set 'de_amp_tokai2_elv_05' under energy capacity" in item or "Unit set 'de_amp_tokai2_elv_05' under required power" in item or "Unit set 'de_amp_tokai2_elv_06' under energy capacity" in item or "Unit set 'de_amp_tokai2_elv_06' under required power" in item or "Unit set 'de_amp_tokai2_elv_07' under energy capacity" in item or "Unit set 'de_amp_tokai2_elv_07' under required power" in item or "Unit set 'de_amp_tokai2_elv_08' under energy capacity" in item or "Unit set 'de_amp_tokai2_elv_08' under required power" in item) and 'closed' in item :
         Unit_set_de_amp_tokai2_closed_count += 1

unii = Unit_set_de_amp_tokai2_count - Unit_set_de_amp_tokai2_closed_count

print("Unit set 'de_amp_tokai2_elv_**' under energy capacity or required power_closed : ",Unit_set_de_amp_tokai2_closed_count)
print("Unit set 'de_amp_tokai2_elv_**' under energy capacity or required power_open : ",unii)
print("\n")


#                               ***Prod:has lost connection***


for item in listOfM:
    if 'prod 7c58111584f4c4e397c17fe23c764130: has lost connection' in item or'prod ff0ef17a6353899639cb31adcf700386: has lost connection' in item or'prod fb28a334fb9b53e105a0c5f7bcb2d8cb: has lost connection' in item or'prod 7df8ec6d0c876faed0789daeebbaa822: has lost connection' in item or'prod d953641b710ce117c426744d61a45edc: has lost connection' in item or 'prod 3757f18d59a698e38535c7260937dee8: has lost connection' in item or 'prod 6d8d955d375109f29b576b3c68d5f6a9: has lost connection' in item or 'prod 583c9a3647ef8ddbcfc5c4af572f1e4c: has lost connection' in item :
        Prod_has_lost_connection_count += 1

print("Total_Prod_has_lost_connection_tokai2 : ",Prod_has_lost_connection_count)

for item in listOfM:
    if ('prod 7c58111584f4c4e397c17fe23c764130: has lost connection' in item or'prod ff0ef17a6353899639cb31adcf700386: has lost connection' in item or'prod fb28a334fb9b53e105a0c5f7bcb2d8cb: has lost connection' in item or'prod 7df8ec6d0c876faed0789daeebbaa822: has lost connection' in item or'prod d953641b710ce117c426744d61a45edc: has lost connection' in item or 'prod 3757f18d59a698e38535c7260937dee8: has lost connection' in item or 'prod 6d8d955d375109f29b576b3c68d5f6a9: has lost connection' in item or 'prod 583c9a3647ef8ddbcfc5c4af572f1e4c: has lost connection' in item) and 'closed' in item :
         Prod_has_lost_connection_closed_count += 1

prod = Prod_has_lost_connection_count - Prod_has_lost_connection_closed_count

print("Prod_has_lost_connection_tokai2_closed : ",Prod_has_lost_connection_closed_count)
print("Prod_has_lost_connection_tokai2_open : ",prod)
print("\n")
print("Total_Tokai2_Alerts : ",safty_count+Communication_count+Environmetal_count+Battery_fault_count+Inverter_fault_count+Prod_has_lost_connection_count+Controller_count+Unit_set_de_amp_tokai2_count)
print("\n"*2)
#*******************************************Tokai-2_End************************************************************


#******************************************Promethues**************************************************************
print("                                     Promethues_part")
print("\n"*2)

Blckbox_bb_count = 0
Blckbox_hs_count = 0
pro_mdex_bb_proc_count = 0
pro_mdex_bb_tran_count = 0
tmh_relay_count = 0
server_rabbit_count = 0
rabbit_bb_count = 0
rabbit_sh_count = 0
aggregator_count = 0
pro_mdex_sh_proc_count = 0
pro_mdex_sh_tran_count = 0
es_down_count = 0
es1_down_count = 0
es2_down_count = 0
es3_down_count = 0
es4_down_count = 0
host_count = 0


Blckbox_bb_closed = 0
Blckbox_hs_closed = 0
pro_mdex_bb_proc_closed = 0
pro_mdex_bb_tran_closed = 0
tmh_relay_closed = 0
server_rabbit_closed = 0
rabbit_bb_closed = 0
rabbit_sh_closed = 0
aggregator_closed = 0
pro_mdex_sh_proc_closed = 0
pro_mdex_sh_tran_closed = 0
es_down_closed = 0
es1_down_closed = 0
es2_down_closed = 0
es3_down_closed = 0
es4_down_closed = 0
host_closed = 0

#**************************************Blackbox in mdex.bb.proc is down*************************


for item in listOfM:
    if 'Blackbox in mdex.bb.proc is down' in item :
        Blckbox_bb_count += 1

print("Total_Blackbox in mdex.bb.proc is down : ",Blckbox_bb_count)

for item in listOfM:
    if 'Blackbox in mdex.bb.proc is down' in item and 'closed' in item :
         Blckbox_bb_closed += 1

blk = Blckbox_bb_count  - Blckbox_bb_closed

print("Blackbox in mdex.bb.proc is down_closed : ",Blckbox_bb_closed)
print("Blackbox in mdex.bb.proc is down_open : ",blk)
print("\n") 


#**************************************Blackbox in mdex.hs.proc is down**************************

for item in listOfM:
    if 'Blackbox in mdex.hs.proc is down' in item :
        Blckbox_hs_count += 1

print("Total_Blackbox in mdex.hs.proc is down : ",Blckbox_hs_count)

for item in listOfM:
    if 'Blackbox in mdex.hs.proc is down' in item and 'closed' in item :
         Blckbox_hs_closed += 1

blk2 = Blckbox_hs_count  - Blckbox_hs_closed

print("Blackbox in mdex.hs.proc is down_closed : ",Blckbox_hs_closed)
print("Blackbox in mdex.hs.proc is down_open : ",blk2)
print("\n")


#**************************************prometheus_mdex.bb.proc is down****************************

for item in listOfM:
    if 'prometheus_mdex.bb.proc is down' in item :
        pro_mdex_bb_proc_count += 1

print("Total_prometheus_mdex.bb.proc is down : ",pro_mdex_bb_proc_count)

for item in listOfM:
    if 'prometheus_mdex.bb.proc is down' in item and 'closed' in item :
         pro_mdex_bb_proc_closed += 1

md = pro_mdex_bb_proc_count  - pro_mdex_bb_proc_closed

print("prometheus_mdex.bb.proc is down_closed : ",pro_mdex_bb_proc_closed)
print("prometheus_mdex.bb.proc is down_open : ",md)
print("\n")

#**************************************prometheus_mdex.bb.tran is down**********************************
for item in listOfM:
    if 'prometheus_mdex.bb.tran is down' in item :
        pro_mdex_bb_tran_count += 1

print("Total_prometheus_mdex.bb.tran is down : ",pro_mdex_bb_tran_count)

for item in listOfM:
    if 'prometheus_mdex.bb.tran is down' in item and 'closed' in item :
         pro_mdex_bb_tran_closed += 1

md2 = pro_mdex_bb_tran_count  - pro_mdex_bb_tran_closed

print("prometheus_mdex.bb.tran is down_closed : ",pro_mdex_bb_tran_closed)
print("prometheus_mdex.bb.tran is down_open : ",md2)
print("\n")


#*************************************Prometheus is not able to collect metrics about tmh-relay on instance proc101:8088 in mdex.hs.proc.


for item in listOfM:
    if 'Prometheus is not able to collect metrics about tmh-relay on instance proc101:8088 in mdex.hs.proc' in item :
        tmh_relay_count += 1

print("Total_Prometheus is not able to collect metrics about tmh-relay on instance proc101:8088 in mdex.hs.proc : ",tmh_relay_count)

for item in listOfM:
    if 'Prometheus is not able to collect metrics about tmh-relay on instance proc101:8088 in mdex.hs.proc' in item and 'closed' in item :
         tmh_relay_closed += 1

tmh = tmh_relay_count  - tmh_relay_closed

print("Prometheus is not able to collect metrics about tmh-relay on instance proc101:8088 in mdex.hs.proc_closed : ",tmh_relay_closed)
print("Prometheus is not able to collect metrics about tmh-relay on instance proc101:8088 in mdex.hs.proc_open : ",tmh)
print("\n")


#***********************************Server rabbit_3_7_1 in production.aggregator is under high load.

for item in listOfM:
    if 'Server rabbit_3_7_1 in production.aggregator is under high load' in item :
        server_rabbit_count += 1

print("Total_Server rabbit_3_7_1 in production.aggregator is under high load : ",server_rabbit_count)

for item in listOfM:
    if 'Server rabbit_3_7_1 in production.aggregator is under high load' in item and 'closed' in item :
         server_rabbit_closed += 1

srb = server_rabbit_count  - server_rabbit_closed

print("Server rabbit_3_7_1 in production.aggregator is under high load_closed : ",server_rabbit_closed)
print("Server rabbit_3_7_1 in production.aggregator is under high load_open : ",srb)
print("\n")

#************************************RabbitMQ cluster in mdex.hs.tran has queue above threshold. Queue is logstash_events in vhost fluentd.


for item in listOfM:
    if 'RabbitMQ cluster in mdex.hs.tran has queue above threshold. Queue is logstash_events in vhost fluentd' in item :
        rabbit_sh_count += 1

print("Total_RabbitMQ cluster in mdex.hs.tran has queue above threshold. Queue is logstash_events in vhost fluentd : ",rabbit_sh_count)

for item in listOfM:
    if 'RabbitMQ cluster in mdex.hs.tran has queue above threshold. Queue is logstash_events in vhost fluentd' in item and 'closed' in item :
         rabbit_sh_closed += 1

rsh = rabbit_sh_count  - rabbit_sh_closed

print("RabbitMQ cluster in mdex.hs.tran has queue above threshold. Queue is logstash_events in vhost fluentd_closed : ",rabbit_sh_closed)
print("RabbitMQ cluster in mdex.hs.tran has queue above threshold. Queue is logstash_events in vhost fluentd_open : ",rsh)
print("\n")



#****************RabbitMQ cluster in mdex.bb.tran has queue above threshold. Queue is logstash_events in vhost fluentd.

for item in listOfM:
    if 'RabbitMQ cluster in mdex.bb.tran has queue above threshold. Queue is logstash_events in vhost fluentd' in item :
        rabbit_bb_count += 1

print("Total_RabbitMQ cluster in mdex.bb.tran has queue above threshold. Queue is logstash_events in vhost fluentd : ",rabbit_bb_count)

for item in listOfM:
    if 'RabbitMQ cluster in mdex.bb.tran has queue above threshold. Queue is logstash_events in vhost fluentd' in item and 'closed' in item :
         rabbit_bb_closed += 1

rbb = rabbit_bb_count  - rabbit_bb_closed

print("RabbitMQ cluster in mdex.bb.tran has queue above threshold. Queue is logstash_events in vhost fluentd_closed : ",rabbit_bb_closed)
print("RabbitMQ cluster in mdex.bb.tran has queue above threshold. Queue is logstash_events in vhost fluentd_open : ",rbb)
print("\n")
#*************************Service nginx in production.aggregator is down

for item in listOfM:
    if 'Service nginx in production.aggregator is down' in item :
        aggregator_count += 1

print("Total_Service nginx in production.aggregator is down : ",aggregator_count)

for item in listOfM:
    if 'Service nginx in production.aggregator is down' in item and 'closed' in item :
         aggregator_closed += 1

aggr = aggregator_count  - aggregator_closed

print("Service nginx in production.aggregator is down_closed : ",aggregator_closed)
print("Service nginx in production.aggregator is down_open : ",aggr)
print("\n")

#**************************prometheus_mdex.hs.proc is down

for item in listOfM:
    if 'prometheus_mdex.hs.proc is down' in item :
        pro_mdex_sh_proc_count += 1

print("Total_prometheus_mdex.hs.proc is down : ",pro_mdex_sh_proc_count)

for item in listOfM:
    if 'prometheus_mdex.hs.proc is down' in item and 'closed' in item :
         pro_mdex_sh_proc_closed += 1

mdhs = pro_mdex_sh_proc_count  - pro_mdex_sh_proc_closed

print("prometheus_mdex.hs.proc is down_closed : ",pro_mdex_sh_proc_closed)
print("prometheus_mdex.hs.proc is down_open : ",mdhs)
print("\n")

#************************************prometheus_mdex.hs.tran is down

for item in listOfM:
    if 'prometheus_mdex.hs.tran is down' in item :
        pro_mdex_sh_tran_count += 1

print("Total_prometheus_mdex.hs.tran is down : ",pro_mdex_sh_tran_count)

for item in listOfM:
    if 'prometheus_mdex.hs.tran is down' in item and 'closed' in item :
         pro_mdex_sh_tran_closed += 1

mdhs2 = pro_mdex_sh_tran_count  - pro_mdex_sh_tran_closed

print("prometheus_mdex.hs.tran is down_closed : ",pro_mdex_sh_tran_closed)
print("prometheus_mdex.hs.tran is down_open : ",mdhs2)
print("\n")

#*******************************Production Elastalert is down


for item in listOfM:
    if 'Production Elastalert is down' in item :
        es_down_count += 1

print("Total_Production Elastalert is down : ",es_down_count)

for item in listOfM:
    if 'Production Elastalert is down' in item and 'closed' in item :
         es_down_closed += 1

es = es_down_count  - es_down_closed

print("Production Elastalert is down_closed : ",es_down_closed)
print("Production Elastalert is down_open : ",es)
print("\n")

#****************Host 193.177.238.83 monitored by Blackbox in production.aggregator is down
for item in listOfM:
    if 'monitored by Blackbox in production.aggregator is down' in item :
        host_count += 1

print("Total_Host 193.177.238.83 monitored by Blackbox in production.aggregator is down : ",host_count)

for item in listOfM:
    if 'monitored by Blackbox in production.aggregator is down' in item and 'closed' in item :
         host_closed += 1

ho = host_count  - host_closed

print("Host ** monitored by Blackbox in production.aggregator is down_closed : ",host_closed)
print("Host ** monitored by Blackbox in production.aggregator is down_open : ",ho)
print("\n")


#********RabbitMQ cluster in tmh.orange.arena has queue above threshold. Queue is logstash_events in vhost fluentd.


for item in listOfM:
    if 'RabbitMQ cluster in tmh.orange.arena has queue above threshold. Queue is logstash_events in vhost fluentd' in item :
        es1_down_count += 1

print("Total_RabbitMQ cluster in tmh.orange.arena has queue above threshold. Queue is logstash_events in vhost fluentd : ",es1_down_count)

for item in listOfM:
    if 'RabbitMQ cluster in tmh.orange.arena has queue above threshold. Queue is logstash_events in vhost fluentd' in item and 'closed' in item :
         es1_down_closed += 1

es1 = es1_down_count  - es1_down_closed

print("RabbitMQ cluster in tmh.orange.arena has queue above threshold. Queue is logstash_events in vhost fluentd_closed : ",es1_down_closed)
print("RabbitMQ cluster in tmh.orange.arena has queue above threshold. Queue is logstash_events in vhost fluentd_open : ",es1)
print("\n")




#**************Prometheus is not able to get information about rabbitmq cluster on instance rabbit_3_7_1 in production.aggregator.

for item in listOfM:
    if 'Prometheus is not able to get information about rabbitmq cluster on instance rabbit_3_7_1 in production.aggregator' in item :
        es2_down_count += 1

print("Total_Prometheus is not able to get information about rabbitmq cluster on instance rabbit_3_7_1 in production.aggregator : ",es2_down_count)

for item in listOfM:
    if 'Prometheus is not able to get information about rabbitmq cluster on instance rabbit_3_7_1 in production.aggregator' in item and 'closed' in item :
         es2_down_closed += 1

es2 = es2_down_count  - es2_down_closed

print("Prometheus is not able to get information about rabbitmq cluster on instance rabbit_3_7_1 in production.aggregator_closed : ",es2_down_closed)
print("Prometheus is not able to get information about rabbitmq cluster on instance rabbit_3_7_1 in production.aggregator_open : ",es2)
print("\n")


#***********************Server storage of proc102 in mdex.hs.proc is almost full. Usage is **%.



for item in listOfM:
    if 'Server storage of proc102 in mdex.hs.proc is almost full. Usage is' in item :
        es3_down_count += 1

print("Total_Server storage of proc102 in mdex.hs.proc is almost full. Usage is : ",es3_down_count)

for item in listOfM:
    if 'Server storage of proc102 in mdex.hs.proc is almost full. Usage is' in item and 'closed' in item :
         es3_down_closed += 1

es3 = es3_down_count  - es3_down_closed

print("Server storage of proc102 in mdex.hs.proc is almost full. Usage is_closed : ",es3_down_closed)
print("Server storage of proc102 in mdex.hs.proc is almost full. Usage is_open : ",es3)
print("\n")




#***************Server storage in tmh.orange.arena will be full in 12 hours.

for item in listOfM:
    if 'Server storage in tmh.orange.arena will be full in 12 hours' in item :
        es4_down_count += 1

print("Total_Server storage in tmh.orange.arena will be full in 12 hours : ",es4_down_count)

for item in listOfM:
    if 'Server storage in tmh.orange.arena will be full in 12 hours' in item and 'closed' in item :
         es4_down_closed += 1

es4 = es4_down_count  - es4_down_closed

print("Server storage in tmh.orange.arena will be full in 12 hours_closed : ",es4_down_closed)
print("Server storage in tmh.orange.arena will be full in 12 hours_open : ",es4)
print("\n")









top_10 = []

for li in listOfM :
    if 'Device' in li :
        top_10.append(li)

# All Remove from file except ID **************************************************************************

#print(listOfM)
#print("\n"*2)

RemoveDash = []
RemoveLine = []
NewM = []

for mac in top_10:
    whatWeNeed = mac.replace("Device ID","")
    whatWeNeed = whatWeNeed.replace("Device","")
    whatWeNeed = whatWeNeed.replace("US","")
    whatWeNeed = whatWeNeed.replace("EU","")
    whatWeNeed = whatWeNeed.replace("Offline","")
    whatWeNeed = whatWeNeed.replace("offline","")
    whatWeNeed = whatWeNeed.replace("Error Connector","")
    whatWeNeed = whatWeNeed.replace("Error Charger","")
    whatWeNeed = whatWeNeed.replace("or","")
    whatWeNeed = whatWeNeed.replace("contains","")
    whatWeNeed = whatWeNeed.replace("is","")
    whatWeNeed = whatWeNeed.replace("closed","")
    whatWeNeed = whatWeNeed.replace("open","")
    whatWeNeed = whatWeNeed.replace(".","")
    whatWeNeed = whatWeNeed.replace(" ","")
    whatWeNeed = whatWeNeed.replace("\t","")
    whatWeNeed = whatWeNeed.replace("\n","")
    RemoveDash.append(whatWeNeed)
 
#print(RemoveDash)        
"""
with open("Device2","w") as g:
    for i in RemoveDash:
        g.write(i)
        g.write("\n")


# Sorting****************************************************************
from collections import Counter
listOfN = []

with open('Device2', 'r') as h:  
    for line_sort in h.readlines():
        listOfN.append(line_sort) 
"""
from collections import Counter

#print(listOfN)
x = sorted(RemoveDash)
Remove = []

#print(x)

for mac in x:
    whatNeed = mac.replace("\n","")
    Remove.append(whatNeed)

print("\n"*2)
#print(Remove)  


c = Counter(Remove)

print(c)


"""
with open("sort","w") as k:
    for i in Remove :
        k.write(i)
        k.write("\n")
"""

with open("Device", 'r+') as f:
   f.truncate(0)
