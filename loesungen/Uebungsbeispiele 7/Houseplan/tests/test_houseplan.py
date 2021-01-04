import unittest
from houseplan.house import Room, Door, House, Window, HouseDoor

class HousePlanTest(unittest.TestCase):

    def setUp(self) -> None:
        # create simple house
        #   F               F
        #   S   T   G   T   WK  F
        #           G
        # F S   T   G   E-T

        self.corridor = Room("CORRIDOR", 15);
        self.master_bed = Room("BEDROOM", 13);
        self.second_bed = Room("BEDROOM", 11);
        self.eatin_kitchen = Room("EATINKITCHEN", 27);
        self.eatin_kitchen.add_opening("EAST", Window(20, 30, 50, 100, True))
        self.eatin_kitchen.add_opening("NORTH", Window(20, 30, 50, 100, True))
        self.master_bed.add_opening("NORTH", Window(22, 30, 50, 100, True))
        self.second_bed.add_opening("WEST", Window(25, 30, 50, 100, True))
        self.corridor.add_opening("EAST", HouseDoor(20, 40, 100, 200, self.corridor, True))

        d = Door(20, 30, 90, 200, self.corridor, self.eatin_kitchen)
        self.corridor.add_opening("EAST", d)
        self.eatin_kitchen.add_opening("WEST", d)

        d = Door(40, 30, 90, 200, self.master_bed, self.corridor)
        self.corridor.add_opening("WEST", d)
        self.master_bed.add_opening("EAST", d)
        d = Door(70, 30, 90, 200, self.second_bed, self.corridor)
        self.corridor.add_opening("WEST", d)
        self.second_bed.add_opening("EAST", d)

        self.h = House()
        self.h.add_room(self.corridor);
        self.h.add_room(self.master_bed);
        self.h.add_room(self.second_bed);
        self.h.add_room(self.eatin_kitchen);



    # Tests könnten noch viel ausführlicher sein
    # Es wird nur grob grundlegende Funktionalität getestet
    def test_get_window_area(self):
        erg = self.h.get_window_area_facing_orientation("NORTH")
        self.assertEqual(erg, 10000)

    def test_get_all_connected(self):
        erg = self.h.get_all_connected_rooms(self.corridor)
        self.assertEqual(len(erg), 3)
        self.assertIn(self.master_bed, erg)
        self.assertIn(self.second_bed, erg)
        self.assertIn(self.eatin_kitchen, erg)

    def test_get_number_of_openings(self):
        erg = self.h.get_number_of_openings_in_room_type("BEDROOM")
        self.assertEqual(erg, 4)



if __name__ == '__main__':
    unittest.main()
