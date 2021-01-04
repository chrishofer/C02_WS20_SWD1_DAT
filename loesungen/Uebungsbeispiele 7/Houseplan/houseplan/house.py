from typing import List
import abc

class RoomOpening(abc.ABC):
    def __init__(self, posx: float, posy:float, width: float, height: float):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height

class Window(RoomOpening):
    def __init__(self, posx: float, posy:float, width: float, height: float, can_be_opened: bool):
        super().__init__(posx, posy, width, height)
        self.can_be_opened = can_be_opened

class Door(RoomOpening):
    def __init__(self, posx: float, posy:float, width: float, height: float, room1: "Room", room2: "Room"):
        super().__init__(posx, posy, width, height)
        self.room1 = room1
        self.room2 = room2

class HouseDoor(Door):
    def __init__(self, posx: float, posy:float, width: float, height: float, room1: "Room", security_door: bool):
        super().__init__(posx, posy, width, height, room1, None)
        self.security_door = security_door

class BalconyDoor(Door):
    def __init__(self, posx: float, posy:float, width: float, height: float, room1: "Room", tiltable: bool):
        super().__init__(posx, posy, width, height, room1, None)
        self.tiltable = tiltable

class Room:
    def __init__(self, type: str, area: float):
        self.type = type
        self.area = area
        self.openings = {}

    def add_opening(self, orientation: str, opening: RoomOpening):
        self.openings.setdefault(orientation, []).append(opening)
    def __repr__(self):
        return f'{self.type} {self.area}'

class House:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room: Room):
        self.rooms.setdefault(room.type, []).append(room)

    def get_window_area_facing_orientation(self, orientation: str) -> float:
        area = 0

        for rList in self.rooms.values():
            for room in rList:
                ops = room.openings.get(orientation, [])
                for op in ops:
                    if type(op) == Window:
                        area += op.height * op.width
        return area

    def get_number_of_openings_in_room_type(self, type: str) -> int:
        nr_openings = 0
        for room in self.rooms.get(type, []):
            for orient in room.openings.values():
                nr_openings += len(orient)
        return nr_openings

    def get_all_connected_rooms(self, room: Room) -> List[Room]:
        rooms = []

        for openings in room.openings.values():
            for op in openings:
                if type(op) == Door:
                    if op.room1 != None and op.room1 != room:
                        rooms.append(op.room1)
                    if op.room2 != None and op.room2 != room:
                        rooms.append(op.room2)

        return rooms


if __name__ == '__main__':
    # try yourself
    pass