try:
    from w1thermsensor import W1ThermSensor, errors


    def read_temp() -> float:
        try:
            sensor = W1ThermSensor()
            temperature = float(sensor.get_temperature())
            return temperature
        except errors.NoSensorFoundError as e:
            print(f"No sensor was found\n\n{e}")
        except errors.SensorNotReadyError as e:
            print(f"Sensor is not ready yet")
        except Exception as e:
            print(f"Had error:\n\n{e}")
except Exception as e:
    print(e)
    print("Using default read_temp function")

    def read_temp() -> float:
        try:
            temperature = float(input("Enter fridge temp: "))
            return temperature
        except ValueError:
            print("That is not a valid number")


# The below code is kept for reference
# _______________________________________________________________________________________________________________________
# import glob
# from time import sleep
#
# # Thermometer reader is taken from this tutorial:
# # https://thepihut.com/blogs/raspberry-pi-tutorials/gpio-and-python-79-temperature-sensor
#
#
# base_dir = '/sys/bus/w1/devices/'
#
# device_folder = glob.glob(base_dir + '28*')[0]
#
# device_file = device_folder + '/w1_slave'
#
#
# def read_temp_raw():
#
#     f = open(device_file, 'r')
#
#     lines = f.readlines()
#
#     f.close()
#
#     return lines
#
#
# def read_temp() -> float:
#     lines = read_temp_raw()
#
#     while lines[0].strip()[-3:] != 'YES':
#
#         sleep(0.2)
#
#         lines = read_temp_raw()
#
#     equals_pos = lines[1].find('t=')
#
#     if equals_pos != -1:
#
#         temp_string = lines[1][equals_pos+2:]
#
#         temp_c = float(temp_string) / 1000.0
#
#         return temp_c
