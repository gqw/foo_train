# -*- coding: utf-8 -*-
# @Author: asura9527
# @Date:   2021-11-16
# @Last Modified by:   asura9527
# @Last Modified time: 2021-11-16

from gym.envs.registration import register

register(
    id="Foo-v0",
    entry_point="env.foo_env:FooEnv"
)

