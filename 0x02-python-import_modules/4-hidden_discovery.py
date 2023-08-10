#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    x = dir(hidden_4)
    for str in x:
        if str[:2] != "__":
            print(str)
