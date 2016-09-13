#!/usr/bin/env python3.4

import numpy as np
from vispy import gloo, io
import rocket
from rocket.aux import load_shaders

SIZE, SCALE = 256, 2

program = load_shaders('vertex.glsl', 'fragment.glsl')
texture = np.random.randint(0, 255, size=(SIZE, SIZE), dtype=np.uint8)
vertices = np.array([
    (-1, +1), (+1, +1),
    (-1, -1), (+1, -1),
], dtype=np.float32)
texcoords = np.array([
    (0, 1), (1, 1),
    (0, 0), (1, 0),
], dtype=np.float32)


def main():
    rocket.prep(size=(SIZE, SIZE), scale=SCALE)
    rocket.launch(fps=10)


@rocket.attach
def update():
    #global texture
    #texture = np.random.randint(0, 255, size=(SIZE, SIZE), dtype=np.uint8)
    pass


@rocket.attach
def draw():
    program['texel'] = 1.0/SIZE
    program['tex'] = gloo.Texture2D(texture)
    program['vertex'] = gloo.VertexBuffer(vertices)
    program['texcoord'] = gloo.VertexBuffer(texcoords)
    program.draw('triangle_strip')


if __name__ == '__main__':
    main()
