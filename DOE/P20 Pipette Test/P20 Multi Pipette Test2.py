from opentrons import protocol_api

metadata = {'apiLevel': '2.11',
            'Author': 'U.S. Army DEVCOM CBC - Jacob Mangini'}

def run(protocol: protocol_api.ProtocolContext):
    #Tells the robot to expect the opentrons 96 filter tip rack 20ul to be in slot 9
    tips20ul = protocol.load_labware('opentrons_96_filtertiprack_20ul', 9)
    #Tells the robot to expect the opentrons 96 filter tip rack 200ul to be in slot 8
    tips200ul = protocol.load_labware('opentrons_96_filtertiprack_200ul', 8)
    #Tells the robot to expect the temperature module to be in slot 4
    tempMod = protocol.load_module('temperature module', 4)
    #Tells the robot to expect the nest 96 deep well plate 2ml in slot 5
    pcr = tempMod.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul')
    
    #Loads the left pipette mount with the p20 multi channel gen 2 pipette and to use tips from the 20ul 96 filter tip rack
    p20 = protocol.load_instrument('p20_multi_gen2', 'left', tip_racks=[tips20ul])
    #Loads the right pipette mount with the p300 single channel gen 2 pipette and to use tips from the 200ul 96 filter tip rack
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips200ul])
    
    #Sets the temperature module's target temperature to 4
    tempMod.set_temperature(4)
        
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
        
    #For loop iterates through columns 2, 3, and 4 of the generic pcr strip plate on the temp mod in slot 4
    #changes tips after each column is dispensed into
    for y in range(3):
        #Sets the current column of the generic pcr strip plate
        col = pcr.columns()[y+1]
        
        #P20 multi channel pipette picks up a column of tips from the 20uL tip rack in slot 9
        p20.pick_up_tip()
        
        #Aspirates 6uL of the reagent from column 1 (A1-H1) of the generic pcr strip plate at 19.98uL/s
        p20.aspirate(6, pcr['A1'])
        #Dispenses 6uL of the reagent into the current column of the generic pcr strip plate at 5.92uL/s
        p20.dispense(6, col[0])
        #Moves the p20 pipette to 0.6mm below the top of the wells in the current
        #column of the pcr strip well plate in slot 4
        p20.move_to(col[0].top(z = blowout_height))
        #Pushes an extra amount of air through the pipette's tip to assure that any
        #remaining droplets are expelled at its current location
        p20.blow_out()
        #Touch's the currently attached tip to 4 opposite edges of the given well at 20.3mm below the top of the well
        p20.touch_tip(col[0], v_offset = touchtip_height)
        
        #P20 multi channel pipette drops its tips into the robot's default trash bin in slot 12
        p20.drop_tip()
        
    #P20 multi channel pipette picks up a column of tips from the 20uL tip rack in slot 9
    p20.pick_up_tip()
    
    #For loop iterates through columns 5, 6, and 7 of the generic pcr strip plate in slot 4
    #keeping the same tips for each column
    for y in range(3):
        #Sets the current column index of the generic pcr strip plate
        col = pcr.columns()[y+4]
        
        #Aspirates 6uL of the reagent from the first column of the generic pcr strip plate at 19.98uL/s
        p20.aspirate(6, pcr['A1'])
        #Dispenses 6uL of the reagent into the current column of the generic pcr strip plate at 5.92uL/s
        p20.dispense(6, col[0])
        #Moves the p20 pipette to 0.6mm below the top of the wells in the current
        #column of the pcr strip well plate in slot 4
        p20.move_to(col[0].top(z = blowout_height))
        #Pushes an extra amount of air through the pipette's tip to assure that any
        #remaining droplets are expelled at its current location
        p20.blow_out()
        #Touch's the currently attached tip to 4 opposite edges of the given well at 20.3mm below the top of the well
        p20.touch_tip(col[0], v_offset = touchtip_height)
        
    #P20 multi channel pipette drops its tips into the robot's default trash bin in slot 12
    p20.drop_tip()
    
    #P20 multi channel pipette picks up a column of tips from the 20uL tip rack in slot 9
    p20.pick_up_tip()
    
    #Count keeps track of how many columns have been dispensed into
    #Used to change the P20 multi channel pipette's tips after every 2 columns
    count = 1
    
    #For loop iterates through columns 8, 9, 10, and 11 of the generic pcr strip plate in slot 4
    #changes tips after every 2 columns dispensed into
    for y in range(4):
        #Sets the current column index of the generic pcr strip plate
        col = pcr.columns()[y+7]
        
        #Determines whether the P20 multi channel pipette needs to get a new tip
        #Will need a new tip after every 2 columns therefor when count is odd
        if(count % 2 != 0):
            p20.pick_up_tip()
        
        #Aspirates 6uL of the reagent from the first column (A1-H1) of the generic pcr strip plate at 19.98uL/s
        p20.aspirate(6, pcr['A1'])
        #Dispenses 6uL of teh reagent into the current column of the generic pcr strip plate at 5.92uL/s
        p20.dispense(6, col[0])
        #Moves the p20 pipette to 0.6mm below the top of the wells in the current
        #column of the pcr strip well plate in slot 4
        p20.move_to(col[0].top(z = blowout_height))
        #Pushes an extra amount of air through the pipette's tip to assure that any
        #remaining droplets are expelled at its current location
        p20.blow_out()
        #Touch's the currently attached tip to 4 opposite edges of the given well at 20.3mm below the top of the well
        p20.touch_tip(col[0], v_offset = touchtip_height)
        
        #Determines whether the P20 multi channel pipette needs to drop its tips into the robot's default trash bin in slot 12
        #Drops tips after every 2 columns therefor when count is even
        if (count % 2 == 0):
            p20.drop_tip()
            
        #Increments count by 1
        count += 1

    #Deactivates the temperature module
    tempMod.deactivate()