
exec('movements_parameters.py') # np_pop , vec_length , vec_colums , pin_HL , pin_rot , deg_HL , deg_rot
DATA_ARDUINO = open('movements_data','wb')
nb_mv = len(pin_HL)*len(deg_HL)+len(pin_rot)*len(deg_rot)
DATA_ARDUINO.write(

0xBB0xCC0x000x110x1E0x010x0C0x900xFF0XC0

0 11 30
1 12 90





while True :
    
    
