# -*- coding: utf-8 -*-
# @Author: asura9527
# @Date:   2021-11-16
# @Last Modified by:   asura9527
# @Last Modified time: 2021-11-16

import gym

class FooEnv(gym.Env):
    """ This is a simple envirionment """

    def __init__(self) -> None:
        super(FooEnv).__init__()
        self.seed()

    def seed(self):
        print("seed")
        pass

    def step(self, action):
        print("step")
        reward = 0
        done = False
        return None, reward, done, {}

    def reset(self):
        print("reset")
        pass
    
    def render(self):
        return True

    def close(self):
        pass
 
