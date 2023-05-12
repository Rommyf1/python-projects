import math;
import re;

def add_time(start, duration, day=False):

	##PRUEBA
	time_separator = "[: ]";
	original_time_values = re.split(time_separator, start);
	values_to_increment = re.split(time_separator, duration);
	
	hora_original = int(original_time_values[0]);
	minutos_original = int(original_time_values[1]);
	meredium = original_time_values[2];
	horas_extra = int(values_to_increment[0]);
	minutos_extra = int(values_to_increment[1]);
	day_of_week = "";
	
	def minutos_resultantes(minutos, suma_de_minutos):
		return ((minutos+suma_de_minutos)%60);

	def horas_extra_por_minutos(minutos, minutos_extra):
	    return (math.floor((minutos+minutos_extra)/60));

	def horas_resultantes(horas, horas_extra):
		return ((horas+horas_extra)%24);

	def dias_extra_por_horas(horas, horas_extra):
		return math.floor((horas+horas_extra)/24);
	
	def formatear_dias_extra(dias_extra):
		if(dias_extra == 0):
			return "";
		elif(dias_extra == 1):
			return "(next day)";
		elif(dias_extra > 1):
			return ("({} days later)".format(dias_extra));
		return "Error en la función 'dias_extra_por_horas'";


	def formatear_hora(hora, meredium):
		if(hora == 12 and meredium == "AM"):
			hora = 0;
		elif(hora != 12 and meredium == "PM"):
			hora = hora+12;
		return hora;

	def hora_final(hora):
		hora_resultante = {
			"hora": 0,
			"meredium": ""
		};
		
		if(hora == 0):
			hora_resultante["hora"] = 12;
			hora_resultante["meredium"] = "AM";
		elif(hora > 12):
			hora_resultante["hora"] = hora - 12;
			hora_resultante["meredium"] = "PM";
		elif(hora == 12):
			hora_resultante["hora"] = hora;
			hora_resultante["meredium"] = "PM";
		else:
			hora_resultante["hora"] = hora;
			hora_resultante["meredium"] = "AM";
		
		return hora_resultante;

	##Ejecución
	
	minutos_resultante = minutos_resultantes(minutos_original,minutos_extra);
	horas_adicionales = horas_extra_por_minutos(minutos_original,minutos_extra);
	hora_formateada = formatear_hora(hora_original, meredium);
	hora_resultante = horas_resultantes(hora_formateada,(horas_extra+horas_adicionales));
	dias_extra = dias_extra_por_horas(hora_formateada, (horas_extra + horas_adicionales));
	dias_adicionales = formatear_dias_extra(dias_extra);
	formato_hora = hora_final(hora_resultante);

	if(isinstance(day, str)):
		semana = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"];
		index_of_day = semana.index(day.lower());
		new_day_of_week = semana[(index_of_day + dias_extra)%7].capitalize();
		new_time = ("{}:{:0>2} {}, {} {}".format(formato_hora["hora"], minutos_resultante, formato_hora["meredium"], new_day_of_week, dias_adicionales));
	elif(dias_extra == 0):
		if(day):
			new_time = ("{}:{:0>2} {}, {}".format(formato_hora["hora"], minutos_resultante, formato_hora["meredium"], new_day_of_week));
		else:	
			new_time = ("{}:{:0>2} {}".format(formato_hora["hora"], minutos_resultante, formato_hora["meredium"]));
	else:
		new_time = ("{}:{:0>2} {} {}".format(formato_hora["hora"], minutos_resultante, formato_hora["meredium"], dias_adicionales));

	return new_time.strip();