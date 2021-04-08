
import unittest

import raakabed.objects


class Test(unittest.TestCase):
    
    def setUp(self):
        self._objects = raakabed.objects.Objects('../raakabed/objects_raaka_trs80.json')


    def test_get_by_name(self):
        serp = self._objects.get_object_by_name('SERPENT_LIVE')
        
        exp = raakabed.objects.Object(name='SERPENT_LIVE', word='SERPEN', location='NOWHERE', bits='u..P....', max_points=60, current_points=60, short_name='SERPENT', score=0, description='A LARGE SERPENT LIES COILED ON THE FLOOR. ', handler_if_first_noun=[['switch', [['compare_input_to(phrase)', 'ATTACK ...P.... WITH .v......', ['while_pass:', [['set_VAR_to_first_noun()'], ['compare_to_second_noun(object)', 'SWORD'], ['switch', [['is_less_equal_last_random(value)', 153, ['while_pass:', [['print(msg)', 'YOUR'], ['print_second_noun'], ['print(msg)', "SINKS TO THE HILT IN THE SERPENT'S SCALY BODY!"], ['attack_VAR(points)', 17]]]], ['is_less_equal_last_random(value)', 204, ['while_pass:', [['print(msg)', 'YOUR'], ['print_second_noun'], ['print(msg)', 'THROWS A SHOWER OF SPARKS AS IT GLANCES OFF THE WALL! ']]]], ['is_less_equal_last_random(value)', 255, ['while_pass:', [['print(msg)', "THE SERPENT'S HEAD IS SEVERED FROM HIS BODY! A MAGNIFICENT BLOW!"], ['attack_VAR(points)', 255]]]]]]]]], ['compare_input_to(phrase)', 'EAT u....... * *', ['print(msg)', 'BETTER KILL IT FIRST!']]]]], handler_if_second_noun=None, handler_every_turn=[['while_pass:', [['while_fail:', [['while_pass:', [['execute_and_reverse_status:'], ['is_in_pack_or_current_room(object)', 'PLAYER'], ['switch', [['compare_input_to(phrase)', 'WEST * * *', ['execute_phrase(phrase,first_noun,second_noun)', '"04: WEST * * *"', '??00', '??00']], ['compare_input_to(phrase)', 'EAST * * *', ['execute_phrase(phrase,first_noun,second_noun)', '"03: EAST * * *"', '??00', '??00']], ['compare_input_to(phrase)', 'NORTH * * *', ['execute_phrase(phrase,first_noun,second_noun)', '"01: NORTH * * *"', '??00', '??00']], ['compare_input_to(phrase)', 'SOUTH * * *', ['execute_phrase(phrase,first_noun,second_noun)', '"02: SOUTH * * *"', '??00', '??00']]]], ['print2(msg)', 'THE SERPENT PURSUES YOU AND']]], ['print2(msg)', 'THE SERPENT ']]], ['while_pass:', [['is_in_pack_or_current_room(object)', 'PLAYER'], ['set_VAR(object)', 'PLAYER'], ['switch', [['is_less_equal_last_random(value)', 51, ['while_pass:', [['print2(msg)', 'STRIKES, POISON COURSES THROUGH YOUR VEINS!'], ['attack_VAR(points)', 20]]]], ['is_less_equal_last_random(value)', 153, ['print2(msg)', 'STRIKES, YOU DODGE HIS LUNGE! ']], ['is_less_equal_last_random(value)', 204, ['while_pass:', [['print2(msg)', 'COILS RAPIDLY AROUND YOU AND CONSTRICTS!'], ['attack_VAR(points)', 20]]]], ['is_less_equal_last_random(value)', 255, ['print2(msg)', 'GATHERS ITSELF FOR AN ATTACK. ']]]]]]]]], handler_on_death=[['while_pass:', [['print2(msg)', 'THE SERPENT IS DEAD. '], ['swap(object_a,object_b)', 21, 22]]]])

        self.assertTrue(serp==exp)
        
    def test_is_object_in_room_or_held_by_active(self):
        
        # Move the player to the Vault (where the unpulled lever is)
        self._objects.player_object.location = 'Vault'
        self._objects.active_object = self._objects.player_object
        
        # Simple "is in the room"
        obj = self._objects.get_object_by_name('LEVER_UNPULLED')                                
        here = self._objects.is_object_in_room_or_held_by_active(obj, 'Vault')    
        self.assertTrue(here)
        
        # Simple "is held by"
        obj = self._objects.get_object_by_name('POTION')
        obj.location = None
        obj.held_by_name = 'PLAYER'        
        here = self._objects.is_object_in_room_or_held_by_active(obj, 'Vault')    
        self.assertTrue(here)
        
        # Simple "not in room or held by"
        
        obj = self._objects.get_object_by_name('RUG')      
        here = self._objects.is_object_in_room_or_held_by_active(obj, 'Vault')    
        self.assertFalse(here)
        
        # Test being held by active a couple of levels deep
        obj.held_by_name = 'POTION'
        obj.location = None
        here = self._objects.is_object_in_room_or_held_by_active(obj, 'Vault')    
        self.assertTrue(here)
        
        # Test being held by other object in room a couple of levels
        obj.held_by_name = 'LEVER_UNPULLED'
        here = self._objects.is_object_in_room_or_held_by_active(obj, 'Vault')    
        self.assertTrue(here)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()