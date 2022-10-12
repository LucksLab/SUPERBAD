from opentrons import protocol_api

metadata = {'apiLevel': '2.11',
            'Author': 'U.S. Army DEVCOM CBC - Jacob Mangini'}

def run(protocol: protocol_api.ProtocolContext):
    #Tells the robot to expect the opentrons 96 filter tip rack 20ul to be in slot 9
    tips20ul = protocol.load_labware('opentrons_96_filtertiprack_20ul', 9)
    #Tells the robot to expect the opentrons 96 filter tip rack 200ul to be in slot 8
    tips200ul = protocol.load_labware('opentrons_96_filtertiprack_200ul', 8)
    #Tells the robot to expect the opentrons 15 tube rack falcon 15ml deep to be in slot 7
    reservoir = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', 7)
    #Tells the robot to expect the temperature module to be in slot 4
    tempMod = protocol.load_module('temperature module', 4)
    #Tells the robot to expect the opentrons 96 aluminum block generic pcr strip 200ul on the temperature module
    pcr = tempMod.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul')
    #Tells the robot to expect the nest 96 deep well plate 2ml in slot 5
    deepwell = protocol.load_labware('nest_96_wellplate_2ml_deep', 5)
    
    #Loads the left pipette mount with the p20 multi channel gen 2 pipette and to use tips from the 20ul 96 filter tip rack
    p20 = protocol.load_instrument('p20_multi_gen2', 'left', tip_racks=[tips20ul])
    #Loads the right pipette mount with the p300 single channel gen 2 pipette and to use tips from the 200ul 96 filter tip rack
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips200ul])
    
    #Sets the temperature module's target temperature to 4
    tempMod.set_temperature(4)
    
    #P300 picks up a tip from the 200ul tip rack in slot 8
    p300.pick_up_tip()
    
    #Uses a for loop to put 100uL of the reagent in to the first well of each row of the deepwell plate
    for i in range(8):
        row = deepwell.rows()[i]
        
        p300.aspirate(100, reservoir['A1'])
        p300.dispense(100, row[0])
        
    #P300 drops its tip into the robot's default trash bin in slot 12
    p300.drop_tip()
    
    #Sets the p20's aspiration flow rate to 19.98 uL/s
    p20.flow_rate.aspirate = 19.98
    #Sets the p20's dispense flow rate to 5.92 uL/s
    p20.flow_rate.dispense = 5.92
    #Sets the p20's well bottom clearance (height from bottom of well) when dispensing to 9.6 mm
    p20.well_bottom_clearance.dispense = 9.6
    #Sets the p20's blow out flow rate to 1.333333 uL/s
    p20.flow_rate.blow_out = 1.333333
    #Sets the height for the blow out step to -0.6 mm
    blowout_height = -0.6
    #Sets the height for the touch tip step to -20.3 mm
    touchtip_height = -20.3
    
    #Uses a for loop to iterate through columns 1, 2, and 3 of the generic pcr strip plate in slot 5
    #changing tips after each dispense
    for z in range(3):
        #Sets the current column index of the generic pcr strip plate
        col = pcr.columns()[z]
        
        #P20 multi channel pipette picks up a column of tips from the 20uL tip rack in slot 9
        p20.pick_up_tip()
        
        #Aspirates 6uL of the reagent from column 1 (A1-H1) of the deepwell plate at 19.98uL/s
        p20.aspirate(6, deepwell['A1'])
        #Dispenses 6uL of the reagent into the current column of the generic pcr strip plate at 5.92uL/s
        p20.dispense(6, col[0])
        #Moves the p20 pipette to 0.6mm below the top of the wells in the current
        #column of the pcr strip well plate in slot 5
        p20.move_to(col[0].top(z = blowout_height))
        #Pushes an extra amount of air through the pipette's tip to assure that any
        #remaining droplets are expelled at its current location
        p20.blow_out()
        #Touch's the currently attached tip to 4 opposite edges of the given well at 20.3mm below the top of the well
        p20.touch_tip(col[0], v_offset = touchtip_height)
        
        #P20 multi channel pipette drops its tips in the robot's default trash bin in slot 12
        p20.drop_tip()
        
    #P20 multi channel pipette picks of a column of tips from the 20uL tip rack in slot 9
    p20.pick_up_tip()
    
    #Uses a for loop to iterate through columns 4, 5, and 6 of the generic pcr strip plate in slot 5
    #keeping the same tips for each dispense
    for y in range(3):
        #Sets the current column index of the generic pcr strip plate
        col = pcr.columns()[x+3]
        
        #Aspirates 6uL of the reagent from column 1 (A1-H1) of the deepwell plate at 19.98uL/s
        p20.aspirate(6, deepwell['A1'])
        #Dispenses 6uL of the reagent into the current column of the generic pcr strip plate at 5.92uL/s
        p20.dispense(6, col[0])
        #Moves the p20 pipette to 0.6mm below the top of the wells in the current
        #column of the pcr strip well plate in slot 5
        p20.move_to(col[0].top(z = blowout_height))
        #Pushes an extra amount of air through the pipette's tip to assure that any
        #remaining droplets are expelled at its current location
        p20.blow_out()
        #Touch's the currently attached tip to 4 opposite edges of the given well at 20.3mm below the top of the well
        p20.touch_tip(col[0], v_offset = touchtip_height)
        
    #P20 multi channel pipette drops its tips into the robot's default trash bin in slot 12
    p20.drop_tip()
            
    #P20 pipette picks up a tip from the 20uL tip rack on slot 9
    p20.pick_up_tip()

    #Aspirates 20uL from each well in the 1st column (A1-H1) of the Deepwell Plate in slot 4 at 19.98uL/s
    p20.aspirate(20, deepwell['A1'])

    #For loop iterates through columns 7, 8, and 9 of the generic pcr strip plate in slot 5
    #putting 6uL of the starting 20uL of the reagent in each column
    for x in range(3):
        #Sets the current column index of the generic pcr strip plate
        col = pcr.columns()[i+6]

        #Dispenses 6uL into all rows of the current column of the pcr strip well plate in slot 5 at 5.92uL/s
        p20.dispense(6, col[0])
                
    #Dispenses the remaining 2uL of reagent back into the first column (A1-H1) of the deepwell plate
    p20.dispense(2, deepwell['A1'])
    #Moves the p20 pipette to 0.6mm below the top of the wells in the current
    #column of the deepwell plate in slot 4
    p20.move_to(deepwell['A1'].top(z = blowout_height))
    #Pushes an extra amount of air through the pipette's tip to assure that any
    #remaining droplets are expelled at its current location
    p20.blow_out()
    #Touch's the currently attached tip to 4 opposite edges of the given well at 20.3mm below the top of the well
    p20.touch_tip(deepwell['A1'], v_offset = touchtip_height)

    #Aspirates 20uL of the reagent from column 1 (A1-H1) of the deepwell plate at 19.98uL/s
    p20.aspirate(20, deepwell['A1'])
    
    #For loop iterates through columns 10, 11, and 12 of the generic pcr strip plate in slot 5
    #putting 6uL of the starting 20uL of the reagent in each column
    for n in range(3):
        #Sets the current column index of the generic pcr strip plate
        col = pcr.columns()[n+9]
        
        #Dispenses 6uL into all rows of the current column of the pcr strip well plate in slot 5 at 5.92uL/s
        p20.dispense(6, col[0])
    
    #P20 multi channel pipette drops its tips in the Robot's default trash bin in slot 12
    p20.drop_tip()

    #Deactivates the temperature module
    tempMod.deactivate()