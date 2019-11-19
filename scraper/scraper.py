from typing import List, Dict

from auth_request import auth_get, SHUTTLE_URL


class Route:
    color: str
    id: int
    name: str
    description: str

    def __init__(self, color: str, id: int, name: str, description: str, **kwargs):
        self.name = name
        self.color = color
        self.id = id
        self.description = description

    def __str__(self):
        return (f"------------\n"
                f"Name: {self.name} \n"
                f"Color: {self.color} \n"
                f"ID: {self.id} \n"
                f"Description: {self.description} \n"
                f"------------")


def get_routes():
    res = auth_get(f"{SHUTTLE_URL}/routes")
    l_routes: List[Dict] = res.json()
    routes: List[Route] = [Route(**d_route) for d_route in l_routes]
    return routes


def get_shuttle_locations(routes: List[Route]):
    for route in routes:
        print(route.name)
        res = auth_get(f"{SHUTTLE_URL}/routes/{route.id}/vehicles")
        l_shuttles: List[Dict] = res.json()
        print(l_shuttles)


if __name__ == "__main__":
    routes = get_routes()
    get_shuttle_locations(routes)
