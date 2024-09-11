from abc import ABC, abstractmethod

# Antarmuka untuk perangkat yang bisa dihidupkan/dimatikan
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Antarmuka untuk perangkat yang bisa mengatur suhu
class TemperatureControl(ABC):
    @abstractmethod
    def adjust_temperature(self, temperature: int):
        pass

# Antarmuka untuk perangkat yang bisa merekam video
class VideoRecorder(ABC):
    @abstractmethod
    def record_video(self):
        pass

class SmartLight(Switchable):
    def turn_on(self):
        return "Smart light is turned on"

    def turn_off(self):
        return "Smart light is turned off"

class SecurityCamera(Switchable, VideoRecorder):
    def turn_on(self):
        return "Security camera is turned on"

    def turn_off(self):
        return "Security camera is turned off"

    def record_video(self):
        return "Security camera is recording video"

class SmartThermostat(Switchable, TemperatureControl):
    def turn_on(self):
        return "Smart thermostat is turned on"

    def turn_off(self):
        return "Smart thermostat is turned off"

    def adjust_temperature(self, temperature: int):
        return f"Smart thermostat temperature set to {temperature}°C"

# Penggunaan
light = SmartLight()
print(light.turn_on())
# SmartLight tidak memiliki fungsi record_video, sehingga tidak ada kesalahan.

camera = SecurityCamera()
print(camera.turn_on())
print(camera.record_video())

thermostat = SmartThermostat()
print(thermostat.adjust_temperature(22))
