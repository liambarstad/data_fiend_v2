import yaml

class YamlValidator:

    def find(strang):
        f = open("./secrets.yml", "r")
        y = yaml.load(f)
        return y[strang]

