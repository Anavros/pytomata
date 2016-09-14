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

turn = 1
tex_a = gloo.Texture2D(buffer)
tex_b = gloo.Texture2D((SIZE, SIZE))
fbo = gloo.FrameBuffer(tex_b, gloo.RenderBuffer((SIZE, SIZE)))
#fbo.resize(SIZE, SIZE)

# only need to do this once
program['tex'] = tex_a
program['vertex'] = gloo.VertexBuffer(vertices)
program['texcoord'] = gloo.VertexBuffer(texcoords)
program['texel'] = 1.0/SIZE

def main():
    rocket.prep(size=(SIZE, SIZE), scale=SCALE)
    rocket.launch(fps=10)


@rocket.attach
def draw():
    global turn
    turn += 1
    if turn % 2:  # on every other turn
        print("we're doing it!")
        #fbo.activate()
        program.draw('triangle_strip')
    else:
        print("and off")
        #fbo.deactivate()
        program.draw('triangle_strip')
    print(turn)


if __name__ == '__main__':
    main()
