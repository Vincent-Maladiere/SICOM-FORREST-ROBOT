
exec('movements_parameters.py') # np_pop , vec_length , vec_colums , pin_HL , pin_rot , deg_HL , deg_rot
DATA_ARDUINO = open('movements_data','wb')
nb_mv = len(pin_HL)*len(deg_HL)+len(pin_rot)*len(deg_rot)

while True :
