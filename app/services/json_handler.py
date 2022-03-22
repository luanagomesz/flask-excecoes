import json
import io
from json import JSONDecodeError
import os
from ..exc import EmailAlreadyExistError, WrongFieldsError
filepath = os.getenv('DATABASE_PATH')

def read_json() -> list:
    path = os.path.abspath(f"./app/{filepath}")

    try:
        with open(path, "r") as json_file:
            return json.load(json_file)
    except JSONDecodeError:
        with open(path, 'w') as json_file:
            json.dump([], json_file)
            return []
    except FileNotFoundError:
        with io.open(os.path.join(path), 'w') as write_file:
            write_file.write(json.dumps([]))
            return []



def nome_corrector(nome: str):
    nome_separated = nome.split(' ')
    corrected_nome = ''
    for i in nome_separated:
        corrected_nome += i.capitalize() + " "
    corrected_nome = corrected_nome[:-1]
    return corrected_nome




def write_json(data) -> list:
    path = os.path.abspath(f"./app/{filepath}")

    try:
        if isinstance(data['nome'], str) and isinstance(data['email'], str):
            json_list = read_json()
            id = 1
            data['nome'] = nome_corrector(data['nome'])
            data['email'] = data['email'].lower()
            for user in json_list:
                if user['email'] == data['email']:
                    raise EmailAlreadyExistError
                if user['id'] == id:
                    id = user['id'] + 1
            data['id'] = id
            json_list.append(data)
            with open(path, 'w') as json_file:
                json.dump(json_list, json_file, indent=2)
            return data
        else:
            raise WrongFieldsError
    except EmailAlreadyExistError as err:
        return err.message
    except WrongFieldsError:
        message = {"wrong_fields": []}
        if not isinstance(data['nome'], str):
            message['wrong_fields'].append({"nome": type(data['nome']).__name__})
        if not isinstance(data['email'], str):
            message['wrong_fields'].append({"email": type(data['email']).__name__})
        return message