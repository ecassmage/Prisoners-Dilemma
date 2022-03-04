def getConfig(keepComments=False) -> dict:
    import json
    import os
    filename = ''

    for file in os.listdir(os.path.dirname(os.path.abspath(os.curdir))):
        if len(file) > 5 and file[-5:] == ".json":
            filename = file
            break
    else:
        raise FileNotFoundError("a .json file was not located")
        exit()

    try:
        file = open(os.path.abspath(os.curdir) + '\\' + filename)
    except FileNotFoundError:
        file = open(os.path.dirname(os.path.abspath(os.curdir)) + '\\' + filename)

    jsonFile = json.load(file)
    file.close()
    __cleaningJSON(jsonFile, keepComments)
    return jsonFile


def __cleaningJSON(jsonFile, keepComments):
    if not keepComments:
        __removeComments(jsonFile)
    jsonFile['number of players'] = len(jsonFile['players'])
    jsonFile['rewards'].update({f"{jsonFile['number of players']} defect": jsonFile['rewards'][f"all defect"]})
    jsonFile['punishments'].update({f"{jsonFile['number of players']} defect": jsonFile['punishments'][f"all defect"]})
    jsonFile['rewards'].pop(f"all defect")
    jsonFile['punishments'].pop(f"all defect")
    jsonFile['exhaustive settings'] = jsonFile.get('exhaustive settings', {"exhaustive settings": {}})
    if jsonFile['number of defections'] == 0:
        print("You broke the number of defections rule")
        exit()


def __removeComments(jsonFile):
    if type(jsonFile) is dict:
        __removeCommentsDict(jsonFile)
    else:
        __removeCommentsList(jsonFile)


def __removeCommentsDict(jsonFile: dict):
    string = "#COMMENT"
    for key in list(jsonFile.keys()):
        if type(key) is str and key[:len(string)] == string:
            jsonFile.pop(key)
        elif type(jsonFile[key]) is dict:
            __removeCommentsDict(jsonFile[key])
        elif type(jsonFile[key]) is list:
            __removeCommentsList(jsonFile[key])


def __removeCommentsList(jsonFile: list):
    string = "#COMMENT"
    for key in jsonFile:
        if type(key) is str and key[:len(string)] == string:
            jsonFile.pop(key)
        elif type(key) is dict:
            __removeCommentsDict(key)
        elif type(key) is list:
            __removeCommentsList(key)


if __name__ == '__main__':
    dictionary = getInformation()
    print(dictionary)
