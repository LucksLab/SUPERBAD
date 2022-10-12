from opentrons import protocol_api
import csv

metadata = {'apiLevel': '2.11',
            'Author': 'U.S. Army DEVCOM CBC - Jacob Mangini'}

#The csv file that has all the parameters that will be read and used in this protocol
#The first line is the order the values are given and what the key to those values are
csv_file = '''
aspirate_rate,dispense_rate,blow_out_rate,mixed_amount,times_mixed,blow_out_height,touch_tip_height,dispense_height
275.5,10,300,20,0,-8.639,-20.3,-18.067
75.4,10,20,20,0,-16.3,0,0
300,300,196,20,0,-16.3,0,-20.3
194.3,10,300,99,10,-16.3,0,-20.3
300,10,154,84.6,10,-16.3,-20.3,0
10,300,300,20,0,-16.3,-20.3,-16.646
46.4,300,162.4,20,10,-0.652,0,0
300,124.7,300,200,10,-8.15,0,0
255.2,229.1,20,200,10,-20.3,-19.894,0
147.9,300,142.8,95.4,5,-8.476,-11.368,-10.556
10,300,44.8,41.4,0,-16.3,-8.12,-20.3
300,127.6,252,20,5,-16.3,-2.03,-11.977
63.8,10,300,64.8,0,0,-20.3,-5.075
300,300,300,131.4,0,0,0,-10.759
145,142.1,154,90,5,-7.987,-10.962,-9.947
300,10,300,200,10,0,-20.3,-3.451
142.1,142.1,154,88.2,5,-8.15,-10.962,-9.947
300,300,20,200,10,0,-10.556,-16.443
121.8,300,300,20,10,-16.3,-8.12,0
300,10,271.6,14.4,10,-3.749,-8.323,0
255.2,10,20,20,6,-11.573,-16.24,0
10,69.6,240.8,20,0,-16.3,-17.661,-20.3
300,147.9,300,109.8,4,0,-9.947,-20.3
300,145,156.8,200,0,0,-20.3,0
300,147.9,300,109.8,4,0,-9.947,-20.3
10,10,196,171,0,0,-20.3,-1.624
10,10,154,200,10,-16.3,-11.571,-11.368
10,300,162.4,25.2,10,-11.247,-20.3,-20.3
95.7,10,300,200,5,0,-7.714,0
10,10,300,73.8,0,-16.3,0,0
10,10,300,20,10,0,0,-11.571
300,10,30.8,200,0,-16.3,-4.872,-17.052
300,840,78.4,20,10,-6.194,-11.571,-2.03
10,300,20,46.8,4,0,-9.541,-12.383
10,139.2,20,200,0,0,0,-10.962
10,10,20,99,10,0,-6.699,-20.3
300,10,20,12.6,3,-16.3,-20.3,-20.3
300,10,20,200,9,-16.3,-15.022,-20.3
145,142.1,154,90,5,-7.987,-10.962,-9.947
300,300,300,200,0,-16.3,0,-12.18
147.9,95.7,154,104.4,0,-6.357,0,-9.135
142.1,300,151.2,200,10,0,0,-1.015
145,142.1,154,90,5,-7.987,-10.962,-9.947
300,300,300,200,6,-16.3,-20.3,-11.571
10,194.3,300,99,10,0,-20.3,0
275.5,10,20,169.2,0,0,-20.3,-20.3
10,203,300,20,4,-6.357,0,-20.3
300,10,20,200,10,-16.3,-1.015,0
10,275.5,300,171,10,-16.3,0,-7.308
165.3,98.6,20,20,6,0,-20.3,-7.714
147.9,300,50.4,200,3,-16.3,0,0
300,300,20,91.8,10,-14.996,0,-11.368
10,300,300,200,0,-6.031,-3.045,0
165.3,124.7,300,200,0,-16.3,-12.992,-20.3
300,10,238,20,0,0,-2.03,-20.3
81.2,168.2,53.2,64.8,0,-16.3,-20.3,0
145,142.1,154,88.2,5,-7.987,-10.962,-9.947
153.7,156.6,20,200,10,-16.3,-20.3,-20.3
145,142.1,154,90,5,-7.987,-10.962,-9.947
10,110.2,95.2,95.4,8,-11.247,0,0
92.8,10,20,20,0,-6.846,0,-20.3
10,300,20,20,10,-15.485,-20.3,0
133.4,10,20,20,10,-16.3,0,-11.774
10,10,20,171,0,-10.758,-20.3,-15.428
300,300,20,20,6,0,0,-20.3
300,10,72.8,200,5,-9.291,0,-20.3
300,217.5,20,20,0,-9.454,-8.526,0
300,300,128.8,20,7,0,-20.3,0
10,10,100.8,20,0,0,-13.398,0
300,300,300,10.8,10,-11.247,-18.067,-20.3
124.7,10,20,200,10,-3.749,-20.3,0
147.9,300,142.8,95.4,5,-8.476,-11.368,-10.556
10,203,20,200,3,-16.3,-4.06,-20.3
300,10,20,64.8,5,0,0,0
121.8,300,300,20,0,0,-20.3,-20.3
10,300,196,200,5,-0.326,-20.3,-20.3
10,10,20,102.6,3,-14.833,0,-20.3
10,10,300,20,8,-14.507,-20.3,-20.3
275.5,300,20,200,0,-6.194,-19.488,-20.3
118.9,10,300,171,3,-16.3,-20.3,0
'''

def run(protocol: protocol_api.ProtocolContext):
    #Tells the robot to expect the opentrons 96 filter tip rack 1000ul to be in slot 8
    tips1000ul = protocol.load_labware('opentrons_96_filtertiprack_1000ul', 8)
    #Tells the robot to expect the opentrons 96 filter tip rack 200ul to be in slot 9
    tips200ul = protocol.load_labware('opentrons_96_filtertiprack_200ul', 9)
    #Tells the robot to expect the opentrons 15 tube rack falcon 15ml deep to be in slot 7
    reservoir = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', 7)
    #Tells the robot to expect the opentrons 96 aluminum block generic pcr strip 200ul to be in slot 5
    pcr1 = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', 5)
    #Tells the robot to expect the opentrons 96 aluminum block generic pcr strip 200ul to be in slot 5
    #pcr2 = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', 6)
    #Tells the robot to expect the temperature module to be in slot 4
    tempMod = protocol.load_module('temperature module', 4)
    #Tells the robot that the nest 96 well plate 2ml deep is on the temperature module
    wellPlate = tempMod.load_labware('nest_96_wellplate_2ml_deep')
    
    #Loads the left pipette mount with the p1000 single channel gen 2 pipette and use tips from the 1000ul 96 filter tip rack
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[tips1000ul])
    #Loads the right pipette mount with the p300 multi channel gen 2 pipette and use tips from the 200ul 96 filter tip rack
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips200ul])
    
    #Sets the temperature module's target temperature to 4
    tempMod.set_temperature(4)
    
    #Picks up a tip with the p1000 pipette
    p1000.pick_up_tip()

    #Sets the p1000 pipette to aspirate at a flow rate of 137.35ul/s
    p1000.flow_rate.aspirate = 137.35
    #Sets the p1000 pipette to dispense at a flow rate of 137.35ul/s
    p1000.flow_rate.dispense = 137.35
    #Sets the p1000 to aspirate 1mm from the bottom of the wells
    p1000.well_bottom_clearance.aspirate = 1
    #Sets the p1000 to dispence 0.5mm from the bottom of the wells
    p1000.well_bottom_clearance.dispense = 0.5

    #Uses a for loop to iterate through rows A, B, C, D, E, F, G, and H of the well plate
    for i in range(8):
        #Sets the row index for the run through the for loop. Starts at index 0 (row A) and ends at index 7 (row H)
        row = wellPlate.rows()[i]
        #Aspirates 300ul from well A1 of the tube rack with the p1000 pipette
        p1000.aspirate(300, reservoir['A1'])
        #Dispenses 300ul into the well in the first column of the current row with the p1000 pipette
        p1000.dispense(300, row[0])

    #P1000 drops the tip into the default trash location which is the robot's 12th slot
    p1000.drop_tip()
    
    #P300 pipette picks up a tip from the 200uL tip rack on slot 9
    p300.pick_up_tip()
    
    #Splits the file into a list by splitting the data at line breaks
    #[1:] skips the first blank line
    csv_data = csv_file.splitlines()[1:]
    #Reads the csv file and maps what is read into a dictionary (key, value)
    csv_reader = csv.DictReader(csv_data)
    
    #Sets the row and column index at 0 for dispensing into the pcr strip well plate
    col_index = 0
    row_index = 0
    
    #A for loop that iterates through each line of the csv file
    for csv_row in csv_reader:
        
        #Sets the row index of the Deepwell plate and the column index of the pcr strip well plate
        wellPlate_row = wellPlate.rows()[row_index]
        curr_col = pcr1.columns()[col_index]
        
        #Sets the number of times to mix to the given number in the csv file
        mix_times = int(csv_row['times_mixed'])
        
        #Only tells the robot to mix the solution if the mix_times parameter is greater than 0
        if (mix_times > 0):
            #Sets the amount to mix to the given amount in the csv file
            mix_amount = float(csv_row['mixed_amount'])
        
            #Sets the flow rate of for aspirate and dispense of the p300 pipette to its default rate of 92.86uL/s
            p300.flow_rate.aspirate = 92.86
            p300.flow_rate.dispense = 92.86
        
            #Mixes the given amount the given number of times in the first well of the current row of the Deepwell plate
            p300.mix(mix_times, mix_amount, wellPlate_row[0])
        
        #Sets the p300's aspiration flow rate to the given rate in the csv file
        p300.flow_rate.aspirate = float(csv_row['aspirate_rate'])
        #Sets the p300's dispense flow rate to the given rate in the csv file
        p300.flow_rate.dispense = float(csv_row['dispense_rate'])
        #Sets the p300's well bottom clearance (height from bottom of well) when dispensing
        p300.well_bottom_clearance.dispense = float(csv_row['dispense_height'])
        #Sets the p300's blow out flow rate to the given rate in the csv file
        p300.flow_rate.blow_out = float(csv_row['blow_out_rate'])
        #Sets the height for the blow out step to the given rate in the csv file
        blowout_height = float(csv_row['blow_out_height'])
        #Sets the height for the touch tip step to the given rate in the csv file
        touchtip_height = float(csv_row['touch_tip_height'])
        
        #Aspirates 20uL from the first well of the current row of the Deepwell Plate in slot 4
        p300.aspirate(20, wellPlate_row[0])
        #Dispenses 20uL into the well at the current row of the current column into the pcr strip well plat in slot 5
        p300.dispense(20, curr_col[row_index])
        #Moves the p300 pipette to the given blow out height of the well at the current
        #row of the current column of the pcr strip well plate in slot 5
        p300.move_to(curr_col[row_index].top(z = blowout_height))
        #Pushes an extra amount of air through the pipette's tip to assure that any remaining droplets are expelled at its current location
        p300.blow_out()
        #Touch's the currently attached tip to 4 opposite edges of the given well at the given height parameter
        p300.touch_tip(curr_col[row_index], v_offset = touchtip_height)
        
        #Increases the row index by 1 so the next time through the loop it fills the next row in the current column
        row_index += 1
        
        #Determines if all the rows in the current column have been filled
        #and if so increases the column index by 1 and sets the row index back to 0
        #so that it starts filling in row 1 of the next column next time through the loop
        if (row_index > 7):
            col_index += 1
            row_index = 0
            
    #P300 pipette drops tip in the Robot's default trash bin in slot 12
    p300.drop_tip()
    
    #Deactivates the temperature module
    tempMod.deactivate()