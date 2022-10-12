from opentrons import protocol_api

metadata = {'Protocol Name': 'Lysate Spotting (6 tix)',
            'apiLevel': '2.11',
            'Author': 'U.S. Army DEVCOM CBC - Jacob Mangini',
            'Description': 'This protocol dispenses CFPS reagents onto 15-well tickets in the homemade ticket holder for freezing w/ LN2.'
           }

def run(protocol: protocol_api.ProtocolContext):
    #Tells the robot that the opentrons 96 filter tip rack 20ul is in slot 6
    tips20ul = protocol.load_labware('opentrons_96_filtertiprack_20ul', 6)
    #Tells the robot that the opentrons 96 filter tip rack 200ul is in 
    tips200ul = protocol.load_labware('opentrons_96_filtertiprack_200ul',1)
    #Tells the robot that the opentrons 24 aluminum block with nest 1.5ml snapcap tube rack is in slot 5
    reservoir = protocol.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap', 5)
    #Tells the robot that the temperature module is in slot 4
    temperature_module = protocol.load_module('temperature module', 4)
    #Tells the robot that the custom wellplate is on the temperature module
    wellPlate = temperature_module.load_labware('cbcticket1v4_16_wellplate_3ul')
    
    #Tells the robot to use the left mount to load the p20 single channel gen2 pipette with tips from the 96 filter tip rack 20ul
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips20ul])
    #Tells the robot to use the left mount to load the p300 single channel gen2 pipette with tips from the 96 filter tip rack 200ul
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips200ul])
    
    #Sets the temperature target to 4
    temperature_module.set_temperature(4)
    
    #Picks up a tip
    p20.pick_up_tip()
    #Sets the p20 pipette to have an aspirate flow rate of 3.78
    p20.flow_rate.aspirate = 3.78
    #Sets the p20 pipette to have a dispense flow rate of 3.78
    p20.flow_rate.dispense = 3.78
    #Sets the p20 to have a blow out flow rate of 3.78
    p20.flow_rate.blow_out = 3.78
    #Sets the p20 to aspirate 1mm from the bottom of the wells
    p20.well_bottom_clearance.aspirate = 1
    #Sets the p20 to dispence 0.5mm from the bottom of the wells
    p20.well_bottom_clearance.dispence = 0.5

    #Uses a for loop to iterate through all 12 columns of the well plate
    for i in range(12):
        #Sets col to the index of the next well to be used
        col = wellPlate.columns()[i]
        #Uses a for loop to itterate through rows A, B, and C of the well plate
        for x in range(3):
            #Sets row to the index of the next well to be used
            row = wellPlate.rows()[x]
            #Aspirates 3ul of lysate from well A1 of the opentrons 24 aluminum block with nest 1.5ml snapcap
            p20.aspirate(3, reservoir['A1'])
            #Dispenses the 3ul of lysate into the well at the current row index in the current column index of the well plate
            p20.dispense(3, row[i])
            ##Moves the end of the pipette tip to 1mm above the top of the current row index in the current column index of the well plate
            p20.move_to(row[i].top(z=1))
            #Pushes an extra amount of air through the pipette's tip to assure that any remaining droplets are expelled
            p20.blow_out()
            #Moves the p20 pipette to the top of well A1 of the tube rack
            p20.move_to(reservoir['A1'].top())
            #Pushes an extra amount of air through the pipette's tip to assure that any remaining droplets are expelled
            p20.blow_out()
            #Touches the end of the pipette to the side of well A1 of the tube rack 4 times
            p20.touch_tip(reservoir['A1'])
  
    #Uses a for loop to iterate through all 12 columns of the well plate
    for y in range(12):
        #Sets col to the index of the next well to be used
        col = wellPlate.columns()[y]
        #Uses a for loop to itterate through rows E, F, and G of the well plate
        for z in range(3):
            #Sets row to the index of the next well to be used
            row = wellPlate.rows()[z+4]
            #Aspirates 3ul of lysate from well A1 of the opentrons 24 aluminum block with nest 1.5ml snapcap
            p20.aspirate(3, reservoir['A1'])
            #Dispenses the 3ul of lysate into the well at the current row index in the current column index of the well plate
            p20.dispense(3, row[y])
            ##Moves the end of the pipette tip to 1mm above the top of the current row index in the current column index of the well plate
            p20.move_to(row[y].top(z=1))
            #Pushes an extra amount of air through the pipette's tip to assure that any remaining droplets are expelled
            p20.blow_out()
            #Moves the p20 pipette to the top of well A1 of the tube rack
            p20.move_to(reservoir['A1'].top())
            #Pushes an extra amount of air through the pipette's tip to assure that any remaining droplets are expelled
            p20.blow_out()
            #Touches the end of the pipette to the side of well A1 of the tube rack 4 times
            p20.touch_tip(reservoir['A1'])
        
    #Drops the pipette tip in the default trash location which is the robot's 12th slot
    p20.drop_tip()
    
    #Turns off the temperature module
    temperature_module.deactivate()    