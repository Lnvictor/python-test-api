import os


def find_cpf_in_blacklist(cpf):
    with open(os.getcwd() + '/blacklist.txt', 'r') as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        return cpf in lines