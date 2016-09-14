#version 120

uniform float texel;
uniform sampler2D show_buffer;

vec4 get(float x, float y) {
    float s = gl_TexCoord[0].s + (x*texel);
    float t = gl_TexCoord[0].t + (y*texel);
    vec4 value = texture2D(show_buffer, vec2(s, t));
    return value;
}

void moore(void) {
    float sum = 0.0;
    sum += get( 0.0, +1.0).r; // n
    sum += get( 0.0, -1.0).r; // s
    sum += get(+1.0,  0.0).r; // e
    sum += get(-1.0,  0.0).r; // w
    sum += get(+1.0, +1.0).r; // ne
    sum += get(-1.0, +1.0).r; // nw
    sum += get(+1.0, -1.0).r; // se
    sum += get(-1.0, -1.0).r; // sw

    if(sum > 3.9) {
        gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
    } else {
        gl_FragColor = vec4(0.0, 0.0, 1.0, 1.0);
    }
}

void main(void) {
    moore();
    //gl_FragColor = texture2D(tex, gl_TexCoord[0].xy);
    //gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
}
