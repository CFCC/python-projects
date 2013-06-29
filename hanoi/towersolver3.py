# AH
class Ring(object):
    def __init__(self, size):
        self.size = size
        self.position = [1, self.size]

    def __repr__(self):
        return str(self.size)

class HPeg(object):
    def __init__(self, number):
        self.number = number
        self.rings = [0, 0, 0]

    def __repr__(self):
        repr_val = self.get_rings_display()
        if repr_val == "Error":
            return "A given ring value is out of acceptable range"
        elif repr_val == "Not set":
            return "Ring values not set"
        else:
            return repr_val
        
    def get_rings_display(self):
        returnstr = ""
        if not self.rings:
            returnstr = "Not set"
            return returnstr
        current_ring = self.rings[0]
        if current_ring == 0:
            returnstr += "|"
        elif current_ring == 1:
            returnstr += "1"
        elif current_ring == 2:
            returnstr += "2"
        elif current_ring == 3:
            returnstr += "3"
        else:
            returnstr = "Error"
            return returnstr

        returnstr += "    "
        current_ring = self.rings[1]
        if current_ring == 0:
            returnstr += "|"
        elif current_ring == 1:
            returnstr += "1"
        elif current_ring == 2:
            returnstr += "2"
        elif current_ring == 3:
            returnstr += "3"
        else:
            returnstr = "Error"
            return returnstr

        returnstr += "    "
        current_ring = self.rings[2]
        if current_ring == 0:
            returnstr += "|"
        elif current_ring == 1:
            returnstr += "1"
        elif current_ring == 2:
            returnstr += "2"
        elif current_ring == 3:
            returnstr += "3"
        else:
            returnstr = "Error"

        return returnstr

    def set_rings(self, pos1, pos2, pos3):
        if not pos1 == 0:
            self.rings[0] = pos1.size
        else:
            self.rings[0] = 0
        if not pos2 == 0:
            self.rings[1] = pos2.size
        else:
            self.rings[1] = 0
        if not pos3 == 0:
            self.rings[2] = pos3.size
        else:
            self.rings[2] = 0

def display_rows():
    global move_count
    print "Move {0}\n\n{1}\n{2}\n{3}\n".format(move_count, row1, row2, row3)
    move_count += 1
    
def make_move(rows):
    row1.set_rings(rows[0], rows[3], rows[6])
    row2.set_rings(rows[1], rows[4], rows[7])
    row3.set_rings(rows[2], rows[5], rows[8])
    display_rows()
    print "Press enter for next move"
    raw_input()

move_count = 0
ring1 = Ring(1)
ring2 = Ring(2)
ring3 = Ring(3)
row1 = HPeg(1)
row2 = HPeg(2)
row3= HPeg(3)

print "Three-ring Towers of Hanoi solver"
print "1 = small ring"
print "2 = medium ring"
print "3 = large ring\n"

make_move([ring1, ring2, ring3, 0, 0, 0, 0, 0, 0])
make_move([0, ring2, ring3, 0, 0, ring1, 0, 0, 0])
make_move([0, 0, ring3, 0, 0, ring1, 0, 0, ring2])
make_move([0, ring1, ring3, 0, 0, 0, 0, 0, ring2])
make_move([0, ring1, ring3, 0, 0, ring2, 0, 0, 0])
make_move([0, 0, ring3, 0, ring1, ring2, 0, 0, 0])
make_move([0, 0, 0, 0, ring1, ring2, 0, 0, ring3])
make_move([0, 0, ring1, 0, 0, ring2, 0, 0, ring3])
make_move([0, 0, ring1, 0, 0, 0, 0, ring2, ring3])
make_move([0, 0, 0, 0, 0, 0, ring1, ring2, ring3])

print "Finished"
