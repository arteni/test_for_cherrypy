import random

class Switchers():

    def create_random_data(self):
        json_to_return = {"data_s1": random.randint(1, 999),
                          "data_s2": random.randint(1, 999),
                          "data_s3": random.randint(1, 999),
                          "data_s4": random.randint(1, 999),
                          "data_s5": random.randint(1, 999),
                          "data_s6": random.randint(1, 999),
                          "data_s7": random.randint(1, 999)}
        return json_to_return
