from abc import ABC, abstractmethod

# Antarmuka besar untuk semua perangkat pintar
class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def adjust_temperature(self, temperature: int):
        pass

    @abstractmethod
    def record_video(self):
        pass

class SmartLight(SmartDevice):
    def turn_on(self):
        return "Smart light is turned on"

    def turn_off(self):
        return "Smart light is turned off"
    
    # Lampu pintar tidak perlu mengatur suhu atau merekam video
    def adjust_temperature(self, temperature: int):
        raise NotImplementedError("Smart light cannot adjust temperature")
    
    def record_video(self):
        raise NotImplementedError("Smart light cannot record video")

class SecurityCamera(SmartDevice):
    def turn_on(self):
        return "Security camera is turned on"

    def turn_off(self):
        return "Security camera is turned off"
    
    # Kamera keamanan tidak memerlukan pengaturan suhu
    def adjust_temperature(self, temperature: int):
        raise NotImplementedError("Security camera cannot adjust temperature")

    def record_video(self):
        return "Security camera is recording video"

# Penggunaan
light = SmartLight()
print(light.turn_on())
# Ini akan menyebabkan error karena lampu pintar tidak dapat merekam video.
# print(light.record_video())

camera = SecurityCamera()
print(camera.record_video())
