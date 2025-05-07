import random

class Customer:
    def _init_(self, name, service_time, arrival_time):
        self.name = name
        self.service_time = service_time
        self.arrival_time = arrival_time
        self.waiting_time = 0
        self.turnaround_time = 0

class Bank:
    def _init_(self):
        self.customers = []
        self.current_time = 0
        self.served_customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def serve_customers(self):
        total_waiting_time = 0
        total_turnaround_time = 0
        pending = self.customers.copy()

        print("Customer Queue Before Serving:")
        for c in pending:
            print(f"{c.name} - Service Time: {c.service_time}, Arrival Time: {c.arrival_time}")

        print("\nCustomer\tService Time\tArrival Time\tWaiting Time\tTurnaround Time")

        while pending:

            available = [c for c in pending if c.arrival_time <= self.current_time]

            if not available:
                self.current_time += 1
                continue

            available.sort(key=lambda x: x.service_time)
            current = available[0]

            current.waiting_time = self.current_time - current.arrival_time
            current.turnaround_time = current.waiting_time + current.service_time

            total_waiting_time += current.waiting_time
            total_turnaround_time += current.turnaround_time

            print(f"{current.name}\t\t{current.service_time}\t\t{current.arrival_time}\t\t{current.waiting_time}\t\t{current.turnaround_time}")
            self.current_time += current.service_time

            pending.remove(current)
            self.served_customers.append(current)

        n = len(self.served_customers)
        avg_waiting = total_waiting_time / n
        avg_turnaround = total_turnaround_time / n

        print(f"\nAverage Waiting Time: {avg_waiting:.2f}")
        print(f"Average Turnaround Time: {avg_turnaround:.2f}")

random.seed(1)  
bank = Bank()

for i in range(10):
    name = f"C{i+1}"
    service_time = random.randint(1, 10)
    arrival_time = random.randint(0, 10)
    customer = Customer(name, service_time, arrival_time)
    bank.add_customer(customer)

bank.serve_customers()