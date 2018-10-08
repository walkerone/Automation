# Author:zhang
# -*- coding:utf-8 -*-
class Flight(object):
    """
    flight
    """
    def __init__(self, name):
        self.flight_name = name


    def flight_status(self):
        print("checking flight_status %s" % self.flight_name)
        return 0

    @property
    def checking_flight_status(self):
        status = self.flight_status()
        if status == 0:
            print("flight is cacle")
        elif status == 1:
            print("flight is qi fei")
        elif status == 2:
            print("flight is arrived")

    @checking_flight_status.setter
    def change_status(self,status):
        status_dict={
            0:"cacle",
            1:"qi fei",
            2:"arrived"
        }
        status_dict.get(status)

    def __call__(self):
        print("call hahh")
fly=Flight("CA90")
fly.checking_flight_status
fly.change_status=2
fly.checking_flight_status

print(fly.__doc__)
fly()