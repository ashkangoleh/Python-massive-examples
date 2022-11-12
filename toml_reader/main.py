"""
Toml parser
"""
# python 3.11
import tomllib



def main()->None:
    with open("./example.toml","rb") as toml:
        data = tomllib.load(toml)
        print(data)
        
        


if __name__ == "__main__":
    main()