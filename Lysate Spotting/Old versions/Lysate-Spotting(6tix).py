from opentrons import protocol_api
import json

metadata = {'Protocol Name': 'Lysate Spotting (6 tix)',
            'apiLevel': '2.11',
            'Author': 'U.S. Army DEVCOM CBC - Jacob Mangini',
            'Description': 'This protocol dispenses CFPS reagents onto 15-well tickets in the homemade ticket holder for freezing w/ LN2.'
           }

def run(protocol: protocol_api.ProtocolContext):
    #Tells the robot that the opentrons 96 filter tip rack 20ul is in slot 6
    tips20ul = protocol.load_labware('opentrons_96_filtertiprack_20ul', 6)
    tips200ul = protocol.load_labware('opentrons_96_filtertiprack_200ul', 1)
    #Tells the robot that the opentrons 24 aluminum block with nest 1.5ml snapcap tube rack is in slot 5
    reservoir = protocol.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap', 5)
    #Tells the robot that the temperature module is in slot 4
    temperature_module = protocol.load_module('temperature module', 4)
    #Tells the robot that the custom wellplate is on the temperature module
    wellPlate = temperature_module.load_labware('cbcticket1v4_16_wellplate_3ul')
    
    #Tells the robot to use the left mount to load the p20 single channel gen2 pipette with tips from the 96 filter tip rack 20ul
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips20ul])
    #Tells the robot to use the right mount to load the p300 single channel gen2 pipette with tips from the 96 filter tip rack 200ul
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
    
    #Aspirates 3ul of lysate from well A1 of the opentrons 24 aluminum block with nest 1.5ml snapcap
    p20.aspirate(3, reservoir['A1'])
    #Dispenses the 3ul of lysate into well A1 of the well plate
    p20.dispense(3, wellPlate['A1'])
    #Moves the end of the pipette tip to 2.4mm above the top of well A1 on the well plate
    p20.move_to(wellPlate['A1'].top(z=2.4))
    #Pushes an extra amount of air through the pipette's tip to assure that any remaining droplets are expelled
    p20.blow_out()
    
    #Aspirates 3ul of lysate from well A1 of the opentrons 24 aluminum block wiht nest 1.5ml snapcap
    p20.aspirate(3, reservoir['A1'])
    #Dispenses the 3ul of lysate into well B1 of the well plate
    p20.dispense(3, wellPlate['B1'])
    #Moves the end of the pipette tip to 2.4mm above the top of well B1 on the well plate
    p20.move_to(wellPlate['B1'].top(z=2.4))
    #Pushes an extra amount of air through the pipette's tip to assure that any remaining droplets are expelled
    p20.blow_out()
    
    #Aspirates 3ul of lysate from well A1 of the opentrons 24 aluminum block with nest 1.5ml snapcap
    p20.aspirate(3, reservoir['A1'])
    #Dispenses the 3ul of lysate into well C1 of the well plate
    p20.dispense(3, wellPlate['C1'])
    #Moves the end of the pipette to 2.4mm above the top of well C1 on the well plate
    p20.move_to(wellPlate['C1'].top(z=2.4))
    #Pushes an extra amount of air through the pipette's tip to assure that any remaining droplets are expelled
    p20.blow_out()
    
    #Aspirates 3ul of lysate from well A1 of the opentrons 24 aluminum block with nest 1.5ml snapcap
    p20.aspirate(3, reservoir['A1'])
    #Dispenses the 3 ul of lysate into well A2 of the well plate
    p20.dispense(3, wellPlate['A2'])
    #Moves the end of teh pipette to 2.4mm above the top of well A2 on the well plate
    p20.move_to(wellPlate['A2'].top(z=2.4))
    #Pushes an extra amount of ait through the pipette's tip to assure that any remaining droplets are expelled
    p20.blow_out()
    
    #Aspirates 3ul of lysate from well A1 of the opentrons 24 aluminum block with nest 1.5ml snapcap
    p20.aspirate(3, reservoir['A1'])
    #Dispenses the 3ul of lysate into well B2 of the well plate
    p20.dispense(3, wellPlate['B2'])
    #Moves the end of the pipette to 2.4mm above the top of well B2 on the well plate
    p20.move_to(wellPlate['B2'].top(z=2.4))
    #Pushes an extra amount of ait through the pipette's tip to assure that any remaining droplets are expelled
    p20.blow_out()
    
    #Aspirates 3ul of lysate from well A1 of the opentrons 24 aluminum block with nest 1.5ml snapcap
    p20.aspirate(3, reservoir['A1'])
    #Dispenses the 3ul of lysate into well C2 of the well plate
    p20.dispense(3, wellPlate['C2'])
    #Moves the end of the pipette to 2.4mm above the top of well C2 on the well plate
    p20.move_to(wellPlate['C2'].top(z=2.4))
    #Pushes an extra amount of ait through the pipette's tip to assure that any remaining droplets are expelled
    p20.blow_out()
    
    #Aspirates 3ul of lysate from well A1 of the opentrons 24 aluminum block with nest 1.5ml snapcap
    p20.aspirate(3, reservoir['A1'])
    #Dispenses the 3ul of lysate into well A3 of the well plate
    p20.dispense(3, wellPlate['A3'])
    #Moves the end of the pipette to 2.4mm above the top of well A3 on the well plate
    p20.move_to(wellPlate['A3'].top(z=2.4))
    #Pushes an extra amount of ait through the pipette's tip to assure that any remaining droplets are expelled
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['B3'])
    p20.move_to(wellPlate['B3'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['C3'])
    p20.move_to(wellPlate['C3'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['A4'])
    p20.move_to(wellPlate['A4'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['B4'])
    p20.move_to(wellPlate['B4'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['C4'])
    p20.move_to(wellPlate['C4'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['A5'])
    p20.move_to(wellPlate['A5'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['B5'])
    p20.move_to(wellPlate['B5'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['C5'])
    p20.move_to(wellPlate['C5'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['A6'])
    p20.move_to(wellPlate['A6'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['B6'])
    p20.move_to(wellPlate['B6'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['C6'])
    p20.move_to(wellPlate['C6'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['A7'])
    p20.move_to(wellPlate['A7'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['B7'])
    p20.move_to(wellPlate['B7'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['C7'])
    p20.move_to(wellPlate['C7'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['A8'])
    p20.move_to(wellPlate['A8'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['B8'])
    p20.move_to(wellPlate['B8'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['C8'])
    p20.move_to(wellPlate['C8'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['A9'])
    p20.move_to(wellPlate['A9'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['B9'])
    p20.move_to(wellPlate['B9'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['C9'])
    p20.move_to(wellPlate['C9'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['A10'])
    p20.move_to(wellPlate['A10'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['B10'])
    p20.move_to(wellPlate['B10'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['C10'])
    p20.move_to(wellPlate['C10'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['A11'])
    p20.move_to(wellPlate['A11'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['B11'])
    p20.move_to(wellPlate['B11'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['C11'])
    p20.move_to(wellPlate['C11'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['A12'])
    p20.move_to(wellPlate['A12'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['B12'])
    p20.move_to(wellPlate['B12'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['C12'])
    p20.move_to(wellPlate['C12'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['E1'])
    p20.move_to(wellPlate['E1'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['F1'])
    p20.move_to(wellPlate['F1'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['G1'])
    p20.move_to(wellPlate['G1'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['E2'])
    p20.move_to(wellPlate['E2'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['F2'])
    p20.move_to(wellPlate['F2'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['G2'])
    p20.move_to(wellPlate['G2'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['E3'])
    p20.move_to(wellPlate['E3'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['F3'])
    p20.move_to(wellPlate['F3'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['G3'])
    p20.move_to(wellPlate['G3'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['E4'])
    p20.move_to(wellPlate['E4'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['F4'])
    p20.move_to(wellPlate['F4'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['G4'])
    p20.move_to(wellPlate['G4'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['E5'])
    p20.move_to(wellPlate['E5'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['F5'])
    p20.move_to(wellPlate['F5'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['G5'])
    p20.move_to(wellPlate['G5'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['E6'])
    p20.move_to(wellPlate['E6'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['F6'])
    p20.move_to(wellPlate['F6'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['G6'])
    p20.move_to(wellPlate['G6'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['E7'])
    p20.move_to(wellPlate['E7'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['F7'])
    p20.move_to(wellPlate['F7'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['G7'])
    p20.move_to(wellPlate['G7'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['E8'])
    p20.move_to(wellPlate['E8'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['F8'])
    p20.move_to(wellPlate['F8'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['G8'])
    p20.move_to(wellPlate['G8'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['E9'])
    p20.move_to(wellPlate['E9'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['F9'])
    p20.move_to(wellPlate['F9'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['G9'])
    p20.move_to(wellPlate['G9'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['E10'])
    p20.move_to(wellPlate['E10'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['F10'])
    p20.move_to(wellPlate['F10'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['G10'])
    p20.move_to(wellPlate['G10'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['E11'])
    p20.move_to(wellPlate['E11'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['F11'])
    p20.move_to(wellPlate['F11'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['G11'])
    p20.move_to(wellPlate['G11'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['E12'])
    p20.move_to(wellPlate['E12'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['F12'])
    p20.move_to(wellPlate['F12'].top(z=2.4))
    p20.blow_out()
    
    p20.aspirate(3, reservoir['A1'])
    p20.dispense(3, wellPlate['G12'])
    p20.move_to(wellPlate['G12'].top(z=2.4))
    p20.blow_out()
    
    #Drops the pipette tip in the default trash location which is the robot's 12th slot
    p20.drop_tip()
    
    #Turns off the temperature module
    temperature_module.deactivate()