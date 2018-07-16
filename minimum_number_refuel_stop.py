class Station:
    memo = dict()
    carry = 0
    def __init__(self, carry, memo=dict()):
        self.carry = carry
        self.memo = memo
    
    
import bisect
class Solution:
    
    def find_le(self, a, x):
        'Find rightmost value less than or equal to x'
        i = bisect.bisect_right(a, x)
        if i:
            return i
        else:
            return -1
    
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        
        import sys
        search_array =[0]
        new_stations = [Station(startFuel, {0: 0})]
        for i in range(len(stations)):
            search_array.append(stations[i][0])
            init_station = Station(stations[i][1], dict())
            new_stations.append(init_station)
        print(search_array)
        # new_stations[1].memo[100] = 50 
        # for i in new_stations:
        #     print(">>>>>", i.memo)
        min_station = sys.maxsize
        for i in range(len(new_stations)):
            currentStation = new_stations[i]
            # print(search_array[i], currentStation.memo, currentStation.carry )
            for station_pass_num, current_fuel in currentStation.memo.items():
                reach_position = search_array[i] + current_fuel + currentStation.carry
                if reach_position >= target:
                    min_station = min(min_station, station_pass_num)
                j = self.find_le(search_array, reach_position) # return the leftmost larger
                # print(search_array, reach_position, "reach_position",station_pass_num,"i",i, "index found", j)
                if j == -1:
                    return -1
                # print("Before update")
                # for k in new_stations:
                #     print(k.memo)                
                for update_idx in range(i+1, j):
                    # print("update_idx", update_idx, new_stations[update_idx].memo)
                    # print("not update_idx", update_idx+1, new_stations[update_idx+1].memo)
                    
                    if station_pass_num + 1 not in new_stations[update_idx].memo:
                        new_stations[update_idx].memo[station_pass_num + 1] = reach_position - search_array[update_idx]
                        # print("inside", new_stations[update_idx].memo)
                        # print("inside", new_stations[update_idx+1].memo)
                        
                        
                        # for station in new_stations:
                            # print("inside", station.memo)
                    else:   
                        current_val = new_stations[update_idx].memo[station_pass_num + 1]
                        new_stations[update_idx].memo[station_pass_num + 1] = max(current_val, reach_position - search_array[update_idx])
                    # print("after update_idx", update_idx, new_stations[update_idx].memo)
                    # print("After update")
                    # for station in new_stations:
                        # print(station.memo)
        if min_station == sys.maxsize:
            return -1
        return min_station
        

print(Solution().minRefuelStops(1,1,[[10,100]]))