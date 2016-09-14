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
    sum += get( 0.0, +1.0).a; // n
    sum += get( 0.0, -1.0).a; // s
    sum += get(+1.0,  0.0).a; // e
    sum += get(-1.0,  0.0).a; // w
    sum += get(+1.0, +1.0).a; // ne
    sum += get(-1.0, +1.0).a; // nw
    sum += get(+1.0, -1.0).a; // se
    sum += get(-1.0, -1.0).a; // sw
    float alive = get(0.0, 0.0).a;

    if(alive > 0.5) {
        // live cell
        if(1.5 < sum && sum < 3.5) {
            // stays alive
            gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0);
        } else {
            // dies
            gl_FragColor = vec4(0.0, 0.0, 0.0, 0.0);
        }
    } else {
        // dead cell
        if(2.5 < sum && sum < 3.5) {
            // new cell is born
            gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0);
        } else {
            // stays dead
            gl_FragColor = vec4(0.0, 0.0, 0.0, 0.0);
        }
    }
}

void main(void) {
    moore();
    //gl_FragColor = texture2D(tex, gl_TexCoord[0].xy);
    //gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
}
