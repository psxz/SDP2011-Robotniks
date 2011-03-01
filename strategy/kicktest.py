from communication.interface import *
from common.utils import *
from common.world import *
from math import *
from strategy import Strategy
import logging

class KickTest(Strategy):
    "A basic module for testing the kicker"

    def run(self):
        try:
            self.me = self.getSelf() # Find out where I am
        except Exception, e:
            logging.warn("couldn't find self: %s", e)
            return
        try:
            ballPos = self.world.getBall().pos # are we there yet?
        except Exception, e:
            logging.warn("couldn't find ball: %s", e)
            return


        if self.me.pos[0] == 0 or ballPos[0] == 0:
            self.stop()
            print "POS 0"
            return

	if self.canKick(ballPos):
		self.kick()

    def canKick(self, target_pos):
	#	to get the angle between [-pi, pi]
	if self.me.orientation > pi:
		self.me.orientation -= 2*pi

	if dist(self.me.pos, target_pos) < 50:
           	angle_diff = self.me.orientation - atan2(target_pos[1] - self.me.pos[1],
                              (target_pos[0] - self.me.pos[0]))
		if angle_diff > pi:
			angle_diff -= 2*pi
		elif angle_diff < -pi:
			angle_diff += 2*pi

            	if abs(angle_diff) < radians(35):
                	return True
