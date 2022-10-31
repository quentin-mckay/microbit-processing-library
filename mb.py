add_library('serial')

sketch = None

serial = None

accel_x = 0
accel_y = 0
accel_z = 0
light_level = 0
is_up = False
is_down = False
is_left = False
is_right = False
is_face_up = False
is_face_down = False
buttonA_is_pressed = False
buttonB_is_pressed = False
pin0_is_touched = False
pin1_is_touched = False
pin2_is_touched = False

event = None

raw_x = 0
raw_y = 0
raw_z = 0
raw_light_level = 0.0

smoothing = 0.9


def init(sketch_object, serial_object, connect_method='auto'):
	global sketch, serial
	sketch = sketch_object
	serial = serial_object

	# if 3rd argument is omitted, find the port automatically
	# if 3rd argument is given, use that number as port number
	if connect_method == 'auto':
		port_index = auto_find_port()
	else:
		show_ports()
		port_index = connect_method

	port_name = serial.list()[port_index]

	serial(sketch, port_name, 115200).bufferUntil(10)

	print('Listening on port {}'.format(port_name))


def parse(e, print_message = False):
	global accel_x, accel_y, accel_z, light_level
	global raw_x, raw_y, raw_z, raw_light_level
	global is_up, is_down, is_left, is_right, is_face_up, is_face_down, buttonA_is_pressed, buttonB_is_pressed, pin0_is_touched, pin1_is_touched, pin2_is_touched
	global event

	event = ''

	message = e.readString().strip()

	if print_message:
		print(message)
	
	m = message.split()

	if len(m) == 1:
		name = m[0].encode('utf-8')  # # unicode to str
		event = name
	elif len(m) == 15:
		raw_x = int(m[0])
		raw_y = int(m[1])
		raw_z = int(m[2])
		light_level = int(m[3])
		is_up = to_bool(m[4])
		is_down = to_bool(m[5])
		is_left = to_bool(m[6])
		is_right = to_bool(m[7])
		is_face_up = to_bool(m[8])
		is_face_down = to_bool(m[9])
		buttonA_is_pressed = to_bool(m[10])
		buttonB_is_pressed = to_bool(m[11])
		pin0_is_touched = to_bool(m[12])
		pin1_is_touched = to_bool(m[13])
		pin2_is_touched = to_bool(m[14])


		# =======================
		easing = 1 - smoothing

		accel_x = lerp(accel_x, raw_x, easing)
		accel_y = lerp(accel_y, raw_y, easing)
		accel_z = lerp(accel_z, raw_z, easing)
		light_level = lerp(light_level, raw_light_level, easing)


def to_bool(str):
	return str == 'True'

def show_ports():
	printArray(Serial.list())

def auto_find_port():
	for index, port_string in enumerate(serial.list()):
		if '/dev/cu.usbmodem' in port_string:
			return index
	
	print("Oops, couldn't auto find port with /dev/cu.usbmodem")
	print("Use mb.show_ports() or printArray(Serial.list()) to find your port")



# def init(sketch_object, serial_object, port_index):
# 	global sketch, serial
# 	sketch = sketch_object
# 	serial = serial_object

# 	serial(sketch, serial.list()[port_index], 115200).bufferUntil(10)