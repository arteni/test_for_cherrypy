import random


class Sensor_api():

    def create_random_data(self):
        json_to_return = {"data1": random.randint(1, 999),
                          "data2": random.randint(1, 999),
                          "data3": random.randint(1, 999),
                          "data4": random.randint(1, 999),
                          "data5": random.randint(1, 999),
                          "data6": random.randint(1, 999),
                          "data7": random.randint(1, 999)}
        return json_to_return
