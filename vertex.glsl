#version 120

attribute vec2 vertex;
attribute vec2 texcoord;

void main(void) {
    gl_Position = vec4(vertex, 0.0, 1.0);
    gl_TexCoord[0] = vec4(texcoord, 0.0, 0.0);
}
