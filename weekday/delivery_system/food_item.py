class FoodItem:
    def __init__(self, name, slots_required, time_required):
        self._name = name
        self._slots_required = slots_required
        self._time_required = time_required
    
    @property
    def name(self):
        return self._name

    @property
    def slots_required(self):
        return self._slots_required

    @property
    def time_required(self):
        return self._time_required
