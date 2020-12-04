class IndianCensus:
    def __init__(self):
        self.state = "State"
        self.population = "Population"
        self.area = "AreaInSqKm"
        self.density = "DensityPerSqKm"

    def __repr__(self):
        return self.state + "," + self.population + "," + self.density + "," + self.area
 
class IndianStateCode:
    def __init__(self):
        self.state = "StateName"
        self.state_code = "StateCode"

    def __repr__(self):
        return self.state + "," + self.state_code
