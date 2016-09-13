#version 120

uniform sampler2D tex;
uniform float texel;

void main(void) {
    float x = gl_TexCoord[0].x;
    float y = gl_TexCoord[0].y;

    // If the alpha channel is 1.0, the cell is alive.
    // Assumes all alpha values are either 0.0 or 1.0.
    float sum = 0.0;
    sum += texture2D(tex, vec2(x,       y+texel)).a;  // n
    sum += texture2D(tex, vec2(x,       y-texel)).a;  // s
    sum += texture2D(tex, vec2(x+texel, y)).a;        // e
    sum += texture2D(tex, vec2(x-texel, y)).a;        // w
    sum += texture2D(tex, vec2(x+texel, y+texel)).a;  // ne
    sum += texture2D(tex, vec2(x-texel, y+texel)).a;  // nw
    sum += texture2D(tex, vec2(x+texel, y-texel)).a;  // se
    sum += texture2D(tex, vec2(x-texel, y-texel)).a;  // sw

    if(sum > 3.9) {
        gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
    } else {
        gl_FragColor = vec4(0.0, 0.0, 1.0, 1.0);
    }
}
