from opentrons import protocol_api
import csv

metadata = {'apiLevel': '2.11',
            'Author': 'U.S. Army DEVCOM CBC - Jacob Mangini'}

def run(protocol: protocol_api.ProtocolContext):
    #Tells the robot to expect the opentrons 96 filter tip rack 20ul to be in slot 9
    tips20ul = protocol.load_labware('opentrons_96_filtertiprack_20ul', 9)
    #Tells the robot to expect the opentrons 96 filter tip rack 1000ul to be in slot 8
    tips1000ul = protocol.load_labware('opentrons_96_filtertiprack_1000ul', 8)
    #Tells the robot to expect the opentrons 15 tube rack falcon 15ml deep to be in slot 7
    reservoir = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', 7)
    #Tells the robot to expect a temperature module on slot 4
    tempMod = protocol.load_module('temperature module', 4)
    #Tells the robot to expect the opentrons nest 96 deepwell plate on the temperature module in slot 4
    deepwell_plate = tempMod.load_labware('nest_96_wellplate_2ml_deep')
    #Tells the robot to expect a temperature module on slot 6
    tempMod2 = protocol.load_module('temperature module', 6)
    #Tells the robot to expect the opentrons 96 aluminum block generic pcr strip 200ul on the temperature module in slot 6
    pcr = tempMod2.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul')
    
    #Loads the right pipette mount with the p20 multi channel gen 2 pipette and use tips from the 20ul 96 filter tip rack
    p20 = protocol.load_instrument('p20_multi_gen2', 'left', tip_racks=[tips20ul])
    #Loads the left pipette mount with the p1000 single channel gen 2 pipette and use tips from the 1000ul 96 filter tip rack
    p1000 = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tips1000ul])
    
    #Sets the temperature modules's target temperature to 4
    tempMod.set_temperature(4)
    tempMod2.set_temperature(4)
    
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
    
    #For loop iterates through all 8 rows (A-H) of the deepwell plate on slot 4
    #changing tips after each dispense
    for i in range(8):
        #Sets the current row index of the deepwell plate
        row = deepwell_plate.rows()[i]

        #P1000 pipette picks up a tip from the 1000ul tip rack on slot 8
        p1000.pick_up_tip()

        #Aspirates 1000ul from well A1 of the tube rack with the p1000 pipette
        p1000.aspirate(1000, reservoir['A1'])
        #Dispenses 1000ul into the well in the first column of the current row with the p1000 pipette
        p1000.dispense(1000, row[0])

        #P1000 pipette drops tip in the Robot's default trash bin in slot 12
        p1000.drop_tip()
    
    #For loop that runs the amount of times equivalent to the amount of plates you want to run
    for n in range(11):
        #For loop iterates through all 12 columns of the generic pcr strip plate in slot 6
        #changes tips after each dispense
        for x in range(12):
            #Sets the column index of the generic pcr strip plate
            col = pcr.columns()[x]

            #P20 pipette picks up tips from the 20uL tip rack on slot 9
            p20.pick_up_tip()

            #Aspirates 6uL of reagent from the 1st column of the Deepwell Plate in slot 4 at 19.98uL/s
            p20.aspirate(6, deepwell_plate['A1'])
            #Dispenses 6uL into the current column of the pcr strip well plate in slot 6 at 5.92uL/s
            p20.dispense(6, col[0])
            #Moves the p20 pipette to 0.6mm below the top of the wells in the current
            #column of the pcr strip well plate in slot 6
            p20.move_to(col[0].top(z = blowout_height))
            #Pushes an extra amount of air through the pipette's tip to assure that any
            #remaining droplets are expelled at its current location
            p20.blow_out()
            #Touch's the currently attached tip to 4 opposite edges of the given well at 20.3mm below the top of the well
            p20.touch_tip(col[0], v_offset = touchtip_height)

            #P20 pipette drops its tips in the Robot's default trash bin in slot 12
            p20.drop_tip()
            
        #Tells the robot to return to its starting (home) position
        protocol.home()
        
        #Pauses protocol until the user resumes protocol
        #During this pause the user must replace the generic pcr strip plate on slot 5
        #and replace the empty box of 20uL filter tips with a new box of 20uL filter tips on slot 9
        protocol.pause("Switch out labware. Then, hit resume to repeat protocol")

        #Resets the tip rack to be a new box of tips
        p20.reset_tipracks()
    
    #Deactivates the temperature modules
    tempMod.deactivate()
    tempMod2.deactivate()