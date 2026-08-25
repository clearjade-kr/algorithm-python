from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the cars based on the position
        N = len(position)
        # position, speed, time
        cars = [(position[i], speed[i], (target - position[i]) / speed[i]) for i in range(N)]
        cars.sort(key = lambda l: l[0], reverse=True)
        
        list_fleets = []
        for car in cars:
            if not list_fleets:
                list_fleets.append(car)

            # Current car is before fleet, if car reaching target is faster - the car catches the fleet
            # else, the car would be another fleet
            if car[2] > list_fleets[-1][2]:
                list_fleets.append(car)

        return len(list_fleets)


if __name__ == "__main__":
    sol = Solution()
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    target = 12

    # position = [4,6]
    # speed = [3,2]
    # target = 10
    print(sol.carFleet(target=target, position=position, speed=speed))
