#Las funciones lambda también conocidas como funciones anonimas, este tipo de funciones no pueden
#almacenar una gran catidad de codigo y solo regresan un valor.
#Nota: en estas funciones se puede utilizar una condicional como en el ejemplo siguiente


destacar_valo = lambda comision:"¡${}!".format(comision) if comision > 10000 else comision 
print(destacar_valo(10001))