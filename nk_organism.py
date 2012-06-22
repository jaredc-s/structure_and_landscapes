import nk_model
import mixins
import bitstring_organism

class Organism(bitstring_organism):
     def __init__(self, value, look_up_table):
         self.look_up_table = look_up_table
         super(Organism, self).__init__(self, value)

