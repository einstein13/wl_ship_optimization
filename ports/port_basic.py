
class port():
    coordinates = [0,0]
    wares = []

    def set_coordinates(self,coordinates):
        self.coordinates[0] = coordinates[0]
        self.coordinates[1] = coordinates[1]
        return

    def read_coordinates(self):
        return self.coordinates

    def copy(self, all_wares=None):
        new_port = port()
        new_port.coordinates[0] = self.coordinates[0]
        new_port.coordinates[1] = self.coordinates[1]
        if all_wares is None:
            for ware in self.wares:
                new_port.wares.append(ware.copy())
        else:
            for ware in self.wares:
                position=find_first(ware,all_wares)
                new_port.wares.append(all_wares[position])
        return new_port

