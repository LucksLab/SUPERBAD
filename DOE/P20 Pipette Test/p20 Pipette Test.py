from opentrons import protocol_api
import csv

metadata = {'apiLevel': '2.11',
            'Author': 'U.S. Army DEVCOM CBC - Jacob Mangini'}

csv_file = '''
aspirate_rate,dispense_rate,blow_out_rate,mixed_amount,times_mixed,blow_out_height,touch_tip_height,dispense_height
19.99333333,8.76,1.36,19.35,0,-12.4,-20.3,10.1
20,0.86,1.54,20,0,-0.8,-20.3,10.2
20,8.793333333,1.34,18.79,0,0,-20.3,10
19.98,5.92,1.333333333,16.92,0,-0.6,-20.3,9.6
20,9.426666667,1.333333333,17.78,0,-1.3,-20.3,11.8
'''

def run(protocol: protocol_api.ProtocolContext):
    #Tells the robot to expect the opentrons 96 filter tip rack 20ul to be in slot 9
    tips20ul = protocol.load_labware('opentrons_96_filtertiprack_20ul', 9)
    #Tells the robot to expect the opentrons 15 tube rack falcon 15ml deep to be in slot 7
    reservoir = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', 7)
    #Tells the robot to expect the temperature module to be in slot 4
    tempMod = protocol.load_module('temperature module', 4)
    #Tells the robot to expect the opentrons 96 aluminum block generic pcr strip 200ul on the temperature module
    pcr1 = tempMod.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul')
    
    #Loads the right pipette mount with the p20 single channel gen 2 pipette and use tips from the 20ul 96 filter tip rack
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips20ul])
    
    #Sets the temperature module's target temperature to 4
    tempMod.set_temperature(4)
    
    #Splits the file into a list by splitting the data at line breaks
    #[1:] skips the first blank line
    csv_data = csv_file.splitlines()[1:]
    #Reads the csv file and maps what is read into a dictionary (key, value)
    csv_reader = csv.DictReader(csv_data)

    #Sets the column index at 0 for dispensing into the pcr strip well plate
    col_index = 0

    #A for loop that iterates through each line of the csv file
    for csv_row in csv_reader:
        
        #Sets the amount to mix to the given amount in the csv file
        mix_amount = float(csv_row['mixed_amount'])
        #Sets the number of times to mix to the given number in the csv file
        mix_times = int(csv_row['times_mixed'])
        #Sets the p20's aspiration flow rate to the given rate in the csv file
        p20.flow_rate.aspirate = float(csv_row['aspirate_rate'])
        #Sets the p20's dispense flow rate to the given rate in the csv file
        p20.flow_rate.dispense = float(csv_row['dispense_rate'])
        #Sets the p20's well bottom clearance (height from bottom of well) when dispensing
        p20.well_bottom_clearance.dispense = float(csv_row['dispense_height'])
        #Sets the p20's blow out flow rate to the given rate in the csv file
        p20.flow_rate.blow_out = float(csv_row['blow_out_rate'])
        #Sets the height for the blow out step to the given rate in the csv file
        blowout_height = float(csv_row['blow_out_height'])
        #Sets the height for the touch tip step to the given rate in the csv file
        touchtip_height = float(csv_row['touch_tip_height'])
        
        #For loop iterates through all 8 rows (A-H) of the generic pcr strip plate
        for i in range(8):
            
            #P20 pipette picks up a tip from the 20uL tip rack on slot 9
            p20.pick_up_tip()

            #Sets the row index of the Deepwell plate and the column index of the pcr strip well plate
            #wellPlate_row = wellPlate.rows()[row_index]
            curr_col = pcr1.columns()[col_index]

            #Only tells the robot to mix the solution if the mix_times parameter is greater than 0
            if (mix_times > 0):
                #Sets the flow rate of for aspirate and dispense of the p20 pipette to its default rate of 7.56uL/s
                p20.flow_rate.aspirate = 7.56
                p20.flow_rate.dispense = 7.56

                #Mixes the given amount the given number of times in the first well of the current row of the Deepwell plate
                p20.mix(mix_times, mix_amount, reservoir['A1'])

            #Aspirates 20uL from the first well of the current row of the Deepwell Plate in slot 4
            p20.aspirate(20, reservoir['A1'])
            #Dispenses 20uL into the well at the current row of the current column into the pcr strip well plat in slot 5
            p20.dispense(20, curr_col[i])
            #Moves the p20 pipette to the given blow out height of the well at the current
            #row of the current column of the pcr strip well plate in slot 5
            p20.move_to(curr_col[i].top(z = blowout_height))
            #Pushes an extra amount of air through the pipette's tip to assure that any
            #remaining droplets are expelled at its current location
            p20.blow_out()
            #Touch's the currently attached tip to 4 opposite edges of the given well at the given height parameter
            p20.touch_tip(curr_col[i], v_offset = touchtip_height)

            #P20 pipette drops tip in the Robot's default trash bin in slot 12
            p20.drop_tip()
            
        #Increases the column index by 1
        col_index += 1

    #Deactivates the temperature module
    tempMod.deactivate()