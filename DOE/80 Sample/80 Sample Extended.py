from opentrons import protocol_api
import csv

metadata = {'apiLevel': '2.11',
            'Author': 'U.S. Army DEVCOM CBC - Jacob Mangini'}

#The csv file that has all the parameters that will be read and used in this protocol
#The first line is the order the values are given and what the key to those values are
csv_file = '''
aspirate_rate,dispense_rate,blow_out_rate,mixed_amount,times_mixed,blow_out_height,touch_tip_height,dispense_height
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
    #Tells the robot to expect the opentrons 96 filter tip rack 1000ul to be in slot 8
    #tips1000ul = protocol.load_labware('opentrons_96_filtertiprack_1000ul', 8)
    #Tells the robot to expect the opentrons 96 filter tip rack 200ul to be in slot 9
    tips200ul = protocol.load_labware('opentrons_96_filtertiprack_200ul', 9)
    #Tells the robot to expect the opentrons 15 tube rack falcon 15ml deep to be in slot 7
    reservoir = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', 7)
    #Tells the robot to expect the temperature module to be in slot 4
    tempMod = protocol.load_module('temperature module', 4)
    #Tells the robot to expect the opentrons 96 aluminum block generic pcr strip 200ul on the temperature module
    pcr1 = tempMod.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul')
    #Tells the robot that the nest 96 well plate 2ml deep is on the temperature module
    #wellPlate = tempMod.load_labware('nest_96_wellplate_2ml_deep')
    
    #Loads the left pipette mount with the p1000 single channel gen 2 pipette and use tips from the 1000ul 96 filter tip rack
    #p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[tips1000ul])
    #Loads the right pipette mount with the p300 multi channel gen 2 pipette and use tips from the 200ul 96 filter tip rack
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips200ul])
    
    #Sets the temperature module's target temperature to 4
    tempMod.set_temperature(4)
    
    #Picks up a tip with the p1000 pipette
    #p1000.pick_up_tip()

    #Sets the p1000 pipette to aspirate at a flow rate of 137.35ul/s
    #p1000.flow_rate.aspirate = 137.35
    #Sets the p1000 pipette to dispense at a flow rate of 137.35ul/s
    #p1000.flow_rate.dispense = 137.35
    #Sets the p1000 to aspirate 1mm from the bottom of the wells
    #p1000.well_bottom_clearance.aspirate = 1
    #Sets the p1000 to dispence 0.5mm from the bottom of the wells
    #p1000.well_bottom_clearance.dispense = 0.5

    #Uses a for loop to iterate through rows A, B, C, D, E, F, G, and H of the well plate
    #for i in range(8):
        #Sets the row index for the run through the for loop. Starts at index 0 (row A) and ends at index 7 (row H)
        #row = wellPlate.rows()[i]
        #Aspirates 300ul from well A1 of the tube rack with the p1000 pipette
        #p1000.aspirate(300, reservoir['A1'])
        #Dispenses 300ul into the well in the first column of the current row with the p1000 pipette
        #p1000.dispense(300, row[0])

    #P1000 drops the tip into the default trash location which is the robot's 12th slot
    #p1000.drop_tip()
    
    #Splits the file into a list by splitting the data at line breaks
    #[1:] skips the first blank line
    csv_data = csv_file.splitlines()[1:]
    #Reads the csv file and maps what is read into a dictionary (key, value)
    csv_reader = csv.DictReader(csv_data)
    
    #Sets the row and column index at 0 for dispensing into the pcr strip well plate
    col_index = 8
    row_index = 6
    
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