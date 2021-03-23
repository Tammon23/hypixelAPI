import requests
import json
apikey = ""


def get_api_key_info(key):
    """
    Gets the key owner, limit, queries preformed in the past minute and total queries
    :return:
    """
    params = {"key": key}
    r = requests.get(f"https://api.hypixel.net/key", params=params)
    r = json.loads(r.content)
    if r['success']:
        return r['record']
    return None


def get_username_history(uuid):
    """
    Gets the username history of a user and the time they were changed at
    :param uuid:
    :return:
    """
    r = requests.get(f"https://api.mojang.com/user/profiles/{uuid}/names")
    if r.status_code != 200:
        return None
    return json.loads(r.content)


def username_to_uuid(username):
    """
    Gets the uuid of a provided username
    :param username:
    :return:
    """
    r = requests.get("https://api.mojang.com/users/profiles/minecraft/" + username)
    if r.status_code != 200:
        return None
    return json.loads(r.content)['id']


if __name__ == "__main__":
    print(get_api_key_info(apikey))
