
class Singleton(object):
	_instance = None
	
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = object.__new__(cls, *args, **kwargs)
		
		return cls._instance

	
class Empleado(Singleton):
	nombre = u""
		
_empleado = Empleado()
_empleado_1 = Empleado()
 
_empleado.nombre = u"Jared"
_empleado_1.nombre = u"Lupe"
print(_empleado.nombre, _empleado_1.nombre)



#1
