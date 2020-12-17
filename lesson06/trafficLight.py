from itertools import cycle

import time

class TrafficLight():

    _color = ['RED', 'YELLOW', 'GREEN', 'YELLOW']

    def running(self):
        for el in cycle(self._color):
            if el == 'RED':
                now = int(time.time())
                while now + 7 > int(time.time()):
                    print("\033[31m {}" .format(el))
            if el == 'YELLOW':
                now = int(time.time())
                while now + 2 > int(time.time()):
                    print("\033[33m {}" .format(el))
            if el == 'GREEN':
                now = int(time.time())
                while now + 5 > int(time.time()):
                    print("\033[32m {}" .format(el))



tl = TrafficLight()

print(tl.running())
