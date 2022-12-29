from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Mᴋɴ Bᴏᴛᴢ")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app


async def all_plugins():
    # This generates a list of plugins in this folder for the * in __main__ to
    # work.

    from glob import glob
    from os.path import basename, dirname, isfile

    mod_paths = glob(dirname(__file__) + "/*.py")
    all_plugs = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return sorted(all_plugs)
