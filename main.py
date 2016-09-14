#!/usr/bin/env python3.4

import numpy as np
from vispy import gloo, io
import rocket
from rocket.aux import load_shaders

SIZE, SCALE = 256, 2

program = load_shaders('vertex.glsl', 'fragment.glsl')


buffer = np.zeros((SIZE, SIZE, 4), dtype=np.float32)
randmap = np.random.randint(2, size=(SIZE, SIZE))
buffer[..., 0] = randmap
buffer[..., 1] = randmap
buffer[..., 2] = randmap
buffer[..., 3] = randmap
vertices = np.array([
    (-1, +1), (+1, +1),
    (-1, -1), (+1, -1),
], dtype=np.float32)
texcoords = np.array([
    (0, 1), (1, 1),
    (0, 0), (1, 0),
], dtype=np.float32)

turn = 0
tex_a = gloo.Texture2D(buffer)
tex_b = gloo.Texture2D(buffer)
fbo = gloo.FrameBuffer(tex_b)
fbo.resize((SIZE, SIZE))

# only need to do this once
program['tex'] = tex_a
program['vertex'] = gloo.VertexBuffer(vertices)
program['texcoord'] = gloo.VertexBuffer(texcoords)
program['texel'] = 1.0/SIZE


def main():
    rocket.prep(size=(SIZE, SIZE), scale=SCALE)
    rocket.launch(fps=10, autoclear=False, enablealpha=False)


@rocket.attach
def draw():
    global turn
    turn += 1
    if turn % 2 == 0:  # on every other turn
        print(turn, "on")
        fbo.activate()
        gloo.clear(color=True)
        program.draw('triangle_strip')
    else:
        print(turn, "off")
        fbo.deactivate()
        gloo.clear(color=True)
        program.draw('triangle_strip')


if __name__ == '__main__':
    main()
