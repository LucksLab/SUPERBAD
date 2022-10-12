from opentrons import protocol_api

metadata = {'Protocol Name': 'STEM Kit Strip',
            'apiLevel': '2.11',
            'Author': 'U.S. Army DEVCOM CBC - Jacob Mangini',
            'Description': ''}

def run(protocol: protocol_api.ProtocolContext):
    
    #Tells the robot to expect the opentrons 96 filter tip rack 1000ul to be in slot 8
    tips1000ul = protocol.load_labware('opentrons_96_filtertiprack_1000ul', 8)
    #Tells the robot to expect the opentrons 96 filter tip rack 200ul to be in slot 9
    tips200ul = protocol.load_labware('opentrons_96_filtertiprack_200ul', 9)
    #Tells the robot to expect the opentrons 96 filter tip rack 200ul to be in slot 10
    tips200ul2 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 10)
    #Tells the robot to expect the opentrons 15 tube rack falcon 15ml deep to be in slot 7
    reservoir = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', 7)
    #Tells the robot to expect the opentrons 96 aluminum block generic pcr strip 200ul to be in slot 5
    pcr1 = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', 5)
    #Tells the robot to expect the opentrons 96 aluminum block generic pcr strip 200ul to be in slot 5
    pcr2 = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', 6)
    #Tells the robot to expect the temperature module to be in slot 4
    tempMod = protocol.load_module('temperature module', 4)
    #Tells the robot that the nest 96 well plate 2ml deep is on the temperature module
    wellPlate = tempMod.load_labware('nest_96_wellplate_2ml_deep')
    
    #Loads the left pipette mount with the p1000 single channel gen 2 pipette and use tips from the 1000ul 96 filter tip rack
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[tips1000ul])
    #Loads the right pipette mount with the p300 multi channel gen 2 pipette and use tips from the 200ul 96 filter tip rack
    p300 = protocol.load_instrument('p300_multi_gen2', 'right', tip_racks=[tips200ul])
    
    #Sets the temperature module's target temperature to 4
    tempMod.set_temperature(4)
    
    #Sets the counter for the while loop:
    reps = 0
    
    #Uses a while loop to repeat the protocol 10 times
    while reps < 10:
        #Picks up a tip with the p1000 pipette
        p1000.pick_up_tip()

        #Sets the p1000 pipette to aspirate at a flow rate of 137.35ul/s
        p1000.flow_rate.aspirate = 137.35
        #Sets the p1000 pipette to dispense at a flow rate of 137.35ul/s
        p1000.flow_rate.dispense = 137.35
        #Sets the p1000 to aspirate 1mm from the bottom of the wells
        p1000.well_bottom_clearance.aspirate = 1
        #Sets the p1000 to dispence 0.5mm from the bottom of the wells
        p1000.well_bottom_clearance.dispence = 0.5

        #Uses a for loop to iterate through rows B, C, D, E, F, G, and H of the well plate
        for i in range(7):
            #Sets the row index for the run through the for loop. Starts at index 1 (row B) and ends at index 7 (row H)
            row = wellPlate.rows()[i+1]
            #Aspirates 550ul from well A1 of the tube rack with the p1000 pipette
            p1000.aspirate(550, reservoir['A1'])
            #Dispenses 550ul into the well in the first column of the current row with the p1000 pipette
            p1000.dispense(550, row[0])

        #P1000 drops the tip into the default trash location which is the robot's 12th slot
        p1000.drop_tip()

        #Picks up a tip with the p300 pipette
        p300.pick_up_tip()

        #Sets the p300 pipette to aspirate at a flow rate of 94ul/s
        p300.flow_rate.aspirate = 94
        #Sets the p300 pipette to dispense at a flow rate of 94ul/s
        p300.flow_rate.dispense = 94
        #Sets the p20 to aspirate 1mm from the bottom of the wells
        p300.well_bottom_clearance.aspirate = 1
        #Sets the p20 to dispence 0.5mm from the bottom of the wells
        p300.well_bottom_clearance.dispence = 0.5

        #Aspirates 200ul from well A1 of the well plate with the p300 pipette
        p300.aspirate(200, wellPlate['A1'])

        #Uses a for loop iterate through the first 9 columns(1-9) of the generic pcr strip in slot 5
        for i in range(9):
            #Sets the column index for the current run through the for loop. Starts at index 0 (column 1) and ends at index 8 (column 9)
            col = pcr1.columns()[i]
            #Dispenses 20ul into the well in the first row of the current column of the pcr strip with the p300 pipette
            p300.dispense(20, col[0])

        #Moves the p300 pipette to 41.3mm above well A1 of the well plate
        p300.move_to(wellPlate['A1'].top(z=41.3))
        #Pushes an extra amount of air through the pipette's tip to assure that any remaining droplets are expelled
        p300.blow_out()

        #Aspirates 80ul from well A1 of the well plate with the p300 pipette
        p300.aspirate(80, wellPlate['A1'])

        #Uses a for loop to iterate through the last 3 columns(10-12) of the generic pcr strip in slot 5
        for i in range(3):
            #Sets the column index for the current run through the for loop. Starts at index 9 (column 10) and ends at index 11 (column 12)
            col = pcr1.columns()[i+9]
            #Dispenses 20ul into the well in the first row of the current column of the pcr strip with the p300 pipette
            p300.dispense(20, col[0])

        #Moves the p300 pipette to 41.3mm above well A1 of the well plate
        p300.move_to(wellPlate['A1'].top(z=41.3))
        #Pushes an extra amount of air through the pipette's tip to assure that any remaining droplets are expelled
        p300.blow_out()

        #Aspirates 200ul from well A1 of the well plate with the p300 pipette
        p300.aspirate(200, wellPlate['A1'])

        #Uses a for loop to iterate through the first 9 columns(1-9) of the generic pcr strip in slot 6
        for i in range(9):
            #Sets the column index for the current run through the for loop. Starts at index 0 (column 1) and ends at index 8 (column 9)
            col = pcr2.columns()[i]
            #Dispenses 20ul into the well in the first row of the current column of the pcr strip with the p300 pipette
            p300.dispense(20, col[0])

        #Moves the p300 pipette to 41.3mm above well A1 of the well plate
        p300.move_to(wellPlate['A1'].top(z=41.3))
        #Pushes an extra amount of air through the pipette's tip to assure that any remaining droplets are expelled
        p300.blow_out()

        #Aspirates 80ul from well A1 of the well plate with the p300 pipette
        p300.aspirate(80, wellPlate['A1'])

        #Uses a for loop to iterate through the last 3 columns(10-12) of the generic pcr strip in slot 6
        for i in range(3):
            #Sets the column index for the current run through the for loop. Starts at index 9 (column 10) and ends at index 11 (column 12)
            col = pcr2.columns()[i+9]
            #Dispenses 20ul into the well in the first row of the current column of the pcr strip with the p300 pipette
            p300.dispense(20, col[0])

        #Moves the p300 pipetee 41.3mm above well A1 of the well plate
        p300.move_to(wellPlate['A1'].top(z=41.3))
        #Pushes an extra amount of air through the pipette's tip to assure that any remaining droplets are expelled
        p300.blow_out()

        #P300 drops the tip into the default trash location which is the robot's 12th slot
        p300.drop_tip()
        
        #Sends the gantry, z-axes, and plungers to their starting position
        protocol.home()
        
        #Increases amount of reps run by 1
        reps += 1
        
        #Pauses protocol until the user resumes protocol
        protocol.pause("Switch out labware.Then, hit resume to repeat protocol")