#version 120

attribute vec2 vert;

void main(void) {
    gl_Position = vec4(vert, 0.0, 1.0);
}
