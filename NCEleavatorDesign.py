from Minheap import minHeap
import time


class Building(object):
    """docstring for Building"""

    def __init__(self, N, NumElev):
        super().__init__()
        self.N = N
        self.NumElev = NumElev
        self._Elevator_List = minHeap(key=None)

    @property
    def N(self):
        return self._N

    @N.setter
    def N(self, N):
        if N <= 0:
            raise ValueError
            print("Building must at least have 1 floor")
        else:
            self._N = N

    @property
    def NumElev(self):
        return self.__NumElev

    @NumElev.setter
    def NumElev(self, NumElev):
        self._NumElev = NumElev
        for i in range(self._NumElev):
            self._Elevator_List.buildHeap(
                [Elevator(self, elevator_num=i) for i in range(self._NumElev)], key=lambda x: x.elevator_num)

    def ElevatorCall(self, floor):
        self._Elevator_List.reconstructHeap(key=lambda x: x.FS)
        # Need a max heap here
        pass


class Elevator(object):
    """docstring for Elevator"""

    def __init__(self, building, elevator_num, floor=0, motion=0, people=0):
        super().__init__()
        self.floor = floor
        self.motion = motion
        self.building = building
        self.elevator_num = elevator_num
        self._timeTravelFloor = 6  # seconds

    @property
    def elevator_num(self):
        return self._elevator_num

    @elevator_num.setter
    def elevator_num(self, elevator_num):
        self._elevator_num = elevator_num

    @property
    def building(self):
        return self._building

    @building.setter
    def building(self, building):
        if building is None:
            print("No building assigned")
        else:
            self._building = building

    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, floor):
        self._floor = floor

    @property
    def motion(self):
        return self._motion

    @motion.setter
    def motion(self, motion):
        self._motion = motion

    @property
    def FS(self, floor, call):
        agreement = 1 if(self.motion >= 0 and call >= 0) else - \
            1 if (self.motion < 0 and call < 0) else 0
        convinience = ((floor >= self.floor) * 1 if agreement >
                       0 else 0) or ((floor < self.floor) * 1 if agreement < 0 else 0)
        d = abs(self.building.N - self.floor)
        # If the elevator is below (above) floor and moving up/still (down) and
        # call is in same direction
        if convinience:
            fs = (self.building.N + 2) - d
        else:
            # If elevator is above (below) floor  and it is already moving up
            # (down)
            if (self.floor > floor and self.motion == 1) or (self.floor < floor and self.motion == -1):
                fs = 1
            # If the elevator is below (above) floor and moving up/still (down)
            # and call is in opposite direction
            else:
                fs = (self.building.N + 1) - d
        return fs

    def move(self, floors):
        if not (self.floor + floors > self.building.N or self.floor + floors < 0):
            self.floor += floors

            # set the motion equal to either +/-1
            self.motion = floors // floors
            time.sleep(abs(floors) * self._timeTravelFloor)
            self.motion = 0
        else:
            raise ValueError
            print("Cannot move that many floors")
