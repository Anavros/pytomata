#!/usr/bin/env python3.4

import numpy as np
from vispy import gloo, io
import rocket
from rocket.aux import load_shaders

SIZE, SCALE = 256, 2

step = load_shaders('vertex.glsl', 'step.f.glsl')
show = load_shaders('vertex.glsl', 'show.f.glsl')


show_img = np.zeros((SIZE, SIZE, 4), dtype=np.float32)
step_img = np.zeros((SIZE, SIZE, 4), dtype=np.float32)
randmap = np.random.randint(2, size=(SIZE, SIZE))
show_img[..., 0] = randmap
show_img[..., 1] = randmap
show_img[..., 2] = randmap
show_img[..., 3] = randmap
vertices = np.array([
    (-1, +1), (+1, +1),
    (-1, -1), (+1, -1),
], dtype=np.float32)
texcoords = np.array([
    (0, 1), (1, 1),
    (0, 0), (1, 0),
], dtype=np.float32)

flip = False
show_tex = gloo.Texture2D(show_img)
step_tex = gloo.Texture2D(step_img)
step_target = gloo.FrameBuffer(step_tex)
step_target.resize((SIZE, SIZE))

show['vertex'] = gloo.VertexBuffer(vertices)
show['texcoord'] = gloo.VertexBuffer(texcoords)
step['vertex'] = gloo.VertexBuffer(vertices)
step['texcoord'] = gloo.VertexBuffer(texcoords)

step['texel'] = 1.0/SIZE
show['step_buffer'] = step_tex
step['show_buffer'] = show_tex


def main():
    rocket.prep(size=(SIZE, SIZE), scale=SCALE)
    rocket.launch(fps=10, autoclear=False, enablealpha=False)


@rocket.attach
def draw():
    global flip
    if flip:
        show['step_buffer'] = show_tex
        step['show_buffer'] = step_tex
        flip = False
    else:
        show['step_buffer'] = step_tex
        step['show_buffer'] = show_tex
        flip = True
    step_target.activate()
    step.draw('triangle_strip')
    step_target.deactivate()
    show.draw('triangle_strip')


if __name__ == '__main__':
    main()
