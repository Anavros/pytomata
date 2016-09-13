#!/usr/bin/env python3.4

import rocket


def main():
    rocket.prep()
    rocket.launch()


@rocket.attach
def update():
    print("hello")


if __name__ == '__main__':
    main()
