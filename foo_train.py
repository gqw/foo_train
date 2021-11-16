# -*- coding: utf-8 -*-
# @Author: asura9527
# @Date:   2021-11-16
# @Last Modified by:   asura9527
# @Last Modified time: 2021-11-16

import gym

from env.foo_env import FooEnv

def main():
    env = gym.make('Foo-v0')
    env.reset()
    
    for _ in range(1000):
        # is_open = env.render()
        # if is_open == False:
        #     break

        _, _, done, _ = env.step({})
        if done == True:
            env.reset()
    env.close()

if __name__ == '__main__':
    main()
