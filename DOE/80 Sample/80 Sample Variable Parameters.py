from opentrons import protocol_api
import csv

metadata = {'apiLevel': '2.11',
            'Author': 'U.S. Army DEVCOM CBC - Jacob Mangini'}

#The csv file that has all the parameters that will be read and used in this protocol
#The first line is the order the values are given and what the key to those values are
csv_file = '''
aspirate_rate,dispense_rate,blow_out_rate,mixed_amount,times_mixed,blow_out_height,touch_tip_height,dispense_height
275.5,10,300,20,0,-8.639,-20.3,2.178
75.4,10,20,20,0,-16.3,0,20.3
300,300,196,20,0,-16.3,0,0.5
194.3,10,300,99,10,-16.3,0,0.5
300,10,154,84.6,10,-16.3,-20.3,20.3
10,300,300,20,0,-16.3,-20.3,3.564
46.4,300,162.4,20,10,-0.652,0,20.3
300,124.7,300,200,10,-8.15,0,20.3
255.2,229.1,20,200,10,-20.3,-19.894,20.3
147.9,300,142.8,95.4,5,-8.476,-11.368,9.504
10,300,44.8,41.4,0,-16.3,-8.12,0.5
300,127.6,252,20,5,-16.3,-2.03,8.118
63.8,10,300,64.8,0,0,-20.3,14.85
300,300,300,131.4,0,0,0,9.306
145,142.1,154,90,5,-7.987,-10.962,10.098
300,10,300,200,10,0,-20.3,16.434
142.1,142.1,154,88.2,5,-8.15,-10.962,10.098
300,300,20,200,10,0,-10.556,3.762
121.8,300,300,20,10,-16.3,-8.12,20.3
300,10,271.6,14.4,10,-3.749,-8.323,20.3
255.2,10,20,20,6,-11.573,-16.24,20.3
10,69.6,240.8,20,0,-16.3,-17.661,0.5
300,147.9,300,109.8,4,0,-9.947,0.5
300,145,156.8,200,0,0,-20.3,20.3
300,147.9,300,109.8,4,0,-9.947,0.5
10,10,196,171,0,0,-20.3,18.216
10,10,154,200,10,-16.3,-11.571,8.712
10,300,162.4,25.2,10,-11.247,-20.3,0.5
95.7,10,300,200,5,0,-7.714,20.3
10,10,300,73.8,0,-16.3,0,20.3
10,10,300,20,10,0,0,8.514
300,10,30.8,200,0,-16.3,-4.872,3.168
300,840,78.4,20,10,-6.194,-11.571,17.82
10,300,20,46.8,4,0,-9.541,7.722
10,139.2,20,200,0,0,0,9.108
10,10,20,99,10,0,-6.699,0.5
300,10,20,12.6,3,-16.3,-20.3,0.5
300,10,20,200,9,-16.3,-15.022,0.5
145,142.1,154,90,5,-7.987,-10.962,10.098
300,300,300,200,0,-16.3,0,7.92
147.9,95.7,154,104.4,0,-6.357,0,10.89
142.1,300,151.2,200,10,0,0,18.81
145,142.1,154,90,5,-7.987,-10.962,10.098
300,300,300,200,6,-16.3,-20.3,8.514
10,194.3,300,99,10,0,-20.3,20.3
275.5,10,20,169.2,0,0,-20.3,0.5
10,203,300,20,4,-6.357,0,0.5
300,10,20,200,10,-16.3,-1.015,20.3
10,275.5,300,171,10,-16.3,0,12.672
165.3,98.6,20,20,6,0,-20.3,12.276
147.9,300,50.4,200,3,-16.3,0,20.3
300,300,20,91.8,10,-14.996,0,8.712
10,300,300,200,0,-6.031,-3.045,20.3
165.3,124.7,300,200,0,-16.3,-12.992,0.5
300,10,238,20,0,0,-2.03,0.5
81.2,168.2,53.2,64.8,0,-16.3,-20.3,20.3
145,142.1,154,88.2,5,-7.987,-10.962,10.098
153.7,156.6,20,200,10,-16.3,-20.3,0.5
145,142.1,154,90,5,-7.987,-10.962,10.098
10,110.2,95.2,95.4,8,-11.247,0,20.3
92.8,10,20,20,0,-6.846,0,0.5
10,300,20,20,10,-15.485,-20.3,20.3
133.4,10,20,20,10,-16.3,0,8.316
10,10,20,171,0,-10.758,-20.3,4.752
300,300,20,20,6,0,0,0.5
300,10,72.8,200,5,-9.291,0,0.5
300,217.5,20,20,0,-9.454,-8.526,20.3
300,300,128.8,20,7,0,-20.3,20.3
10,10,100.8,20,0,0,-13.398,20.3
300,300,300,10.8,10,-11.247,-18.067,0.5
124.7,10,20,200,10,-3.749,-20.3,20.3
147.9,300,142.8,95.4,5,-8.476,-11.368,9.504
10,203,20,200,3,-16.3,-4.06,0.5
300,10,20,64.8,5,0,0,20.3
121.8,300,300,20,0,0,-20.3,0.5
10,300,196,200,5,-0.326,-20.3,0.5
10,10,20,102.6,3,-14.833,0,0.5
10,10,300,20,8,-14.507,-20.3,0.5
275.5,300,20,200,0,-6.194,-19.488,0.5
118.9,10,300,171,3,-16.3,-20.3,20.3
'''

def run(protocol: protocol_api.ProtocolContext):
    #Tells the robot to expect the opentrons 96 filter tip rack 200ul to be in slot 9
    tips200ul = protocol.load_labware('opentrons_96_filtertiprack_200ul', 9)
    #Tells the robot to expect the opentrons 15 tube rack falcon 15ml deep to be in slot 7
    reservoir = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', 7)
    #Tells the robot to expect the temperature module to be in slot 4
    tempMod = protocol.load_module('temperature module', 4)
    #Tells the robot to expect the opentrons 96 aluminum block generic pcr strip 200ul on the temperature module
    pcr1 = tempMod.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul')
    
    #Loads the right pipette mount with the p300 single channel gen 2 pipette and use tips from the 200ul 96 filter tip rack
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips200ul])
    
    #Sets the temperature module's target temperature to 4
    tempMod.set_temperature(4)
    
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
        
        #P300 pipette picks up a tip from the 200uL tip rack on slot 9
        p300.pick_up_tip()
        
        #Sets the row index of the Deepwell plate and the column index of the pcr strip well plate
        #wellPlate_row = wellPlate.rows()[row_index]
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
            p300.mix(mix_times, mix_amount, reservoir['A1'])
        
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
        p300.aspirate(20, reservoir['A1'])
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