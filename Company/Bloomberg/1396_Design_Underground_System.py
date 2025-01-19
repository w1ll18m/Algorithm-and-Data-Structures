class UndergroundSystem:

    def __init__(self):
        self.trip_times = {}
        self.trips = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # map customer to station name and check in time
        self.trips[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # get the station and time that the customer check in at
        startStation, startTime = self.trips[id]
        trip_time = t - startTime

        if startStation not in self.trip_times:
            self.trip_times[startStation] = {}
        if stationName not in self.trip_times[startStation]:
            self.trip_times[startStation][stationName] = [0, 0]
        
        # update total sum and # of trips for trips between startStation and stationName
        self.trip_times[startStation][stationName][0] += trip_time
        self.trip_times[startStation][stationName][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # use total sum and # of trips to calculate the average time between startStation and stationName
        total_sum = self.trip_times[startStation][endStation][0]
        noftrips = self.trip_times[startStation][endStation][1]
        return total_sum / noftrips

'''
checkIn(id, stationName, t) -> checks in customer (id) into a station (stationName) at time t
    - a customer can only be checked into one place at a time

checkOut(id, stationName, t) -> checks out customer (id) into a station (stationName) at time t

getAverageTime(startStation, endStation) -> returns the average time it takes to travel from startStation (A) to endStation (B)
    - computed from direct trips!!! (A to B)
    - time to travel from A to B can be different from time to travel from B to A
    - there will be at least one customer that has travelled from startStation to endStation

we need to keep track of:
(i) check in times for each individual customer 
    - we want to check what stations and time that a customer check in -> map id to [stationName, startTime]
(ii) average times for each station
    - maintain a mapping for trip to total sum of all trip times + # of trips
    - to add a new trip, add trip time to total sum and increment # of trips
    - to return the average time, just divide the total sum by the # of trips

thus checkIn, checkOut, and getAverageTime should all take O(1) time complexity
'''

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)