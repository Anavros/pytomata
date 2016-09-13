#!/usr/bin/env python3.4

import numpy as np
from vispy import gloo, io
import rocket
from rocket.aux import load_shaders

program = load_shaders('vertex.glsl', 'fragment.glsl')
vertices = np.array([
    (-1, +1), (+1, +1),
    (-1, -1), (+1, -1),
], dtype=np.float32)


def main():
    rocket.prep()
    rocket.launch()


@rocket.attach
def draw():
    program['vert'] = gloo.VertexBuffer(vertices)
    program.draw('triangle_strip')


if __name__ == '__main__':
    main()
