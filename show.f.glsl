#version 120

uniform sampler2D step_buffer;

void main(void) {
    gl_FragColor = texture2D(step_buffer, gl_TexCoord[0].xy);
    //gl_FragColor = vec4(0.0, 0.0, 1.0, 1.0);
}
