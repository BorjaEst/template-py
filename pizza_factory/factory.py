import threading
import uuid


class Factory:
    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location
        self.machines = {}

    def buy_machine(self) -> uuid.UUID:
        id = uuid.uuid4()
        self.machines[id] = Machine(id)
        return id

    def make(self, order, recipe):
        machines = self.machines.values()
        available = (x for x in machines if not x.running)
        return next(available).start(order, recipe)


class Machine:
    def __init__(self, id) -> None:
        threading.Thread.__init__(self)
        self.id = id
        self.order = None

    @property
    def running(self):
        if self.order:
            return self.order.is_alive()
        else:
            return False

    def make(self, order, recipe):
        print(f"Machine {self.id}: Making {order}")
        order = Order(order, recipe)
        return order.start()


class Order(threading.Thread):
    def __init__(self, order, recipe) -> None:
        threading.Thread.__init__(self)
        self.order = order
        self.recipe = recipe

    def run(self):
        return self.order(self.recipe)
