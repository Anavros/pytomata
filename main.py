#!/usr/bin/env python3.4

import rocket
from rocket.aux import build_program

program = build_program('vertex.glsl', 'fragment.glsl')


def main():
    rocket.prep()
    rocket.launch()


@rocket.attach
def update():
    print("hello")


@rocket.attach
def draw():
    pass

if __name__ == '__main__':
    main()
