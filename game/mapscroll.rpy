init:
    transform buttonzoom(level=0.16):
        zoom level

python early:
    maps = {
        'kitchen': {
            'left': 'bathroom_door',
            'right': 'garden',

            'items': {
                'hydrogenperoxide': {
                    'x': 0.5,
                    'y': 0.5,
                    "zoom": 0.16
                },
                'bleach': {
                    'x': 0.5,
                    'y': 0.1,
                    "zoom": 0.16
                },
            }
        },
        'garden': {
            'left': 'kitchen',
            'items': {
                'gloves': {
                    'x': 0.75,
                    'y': 0.69,
                    "zoom": 0.16
                },
                'tarp': {
                    'x': 0.0,
                    'y': 1.1,
                    "zoom": 0.7
                }
            }
        },
        'bathroom_door': {
            'up': 'bathroom',
            'left': 'mil_room',
            'right': 'kitchen',
        },
        'bathroom': {
            'down': 'bathroom_door',
        },
        'mil_room': {
            'right': 'bathroom_door',
            'up': 'closet',
        },
        'closet': {
            'down': 'mil_room',
        },
    }

    def parse_mapscroll(lexer):
        subblock_lexer = lexer.subblock_lexer()

        with subblock_lexer.catch_error():
            subblock_lexer.advance()
            items_needed = set(subblock_lexer.rest().split())

            mapscroll_events = {}
            while subblock_lexer.advance():
                    event_name, trigger_name, label_name = subblock_lexer.rest().split()
                    if trigger_name not in mapscroll_events:
                        mapscroll_events[trigger_name] = {}
                    mapscroll_events[trigger_name][event_name] = label_name

            return items_needed, mapscroll_events

    def set_current_map(map_name):
        global mapscroll_current_map
        mapscroll_current_map = map_name
        renpy.scene()
        renpy.transition(dissolve)
        renpy.show(f"bg {map_name}")

    def enter_mapscroll(params, is_next=False):
        items_needed, mapscroll_events = params
        set_current_map(mapscroll_current_map)
        if is_next:
            renpy.show_screen("mapscroll_screen", mapscroll_events=mapscroll_events, items_needed=items_needed)
        else:
            _window_hide()
            renpy.call_screen("mapscroll_screen", mapscroll_events=mapscroll_events, items_needed=items_needed)

    def handle_map_change(map_name, mapscroll_events, items_needed):
        if map_name in mapscroll_events:
            if 'before_enter' in mapscroll_events[map_name]:
                renpy.jump(mapscroll_events[map_name]['before_enter'])
                return mapscroll_events[map_name]['before_enter']

            if 'on_enter' in mapscroll_events[map_name]:
                set_current_map(map_name)
                renpy.jump(mapscroll_events[map_name]['on_enter'])
                return mapscroll_events[map_name]['on_enter']

        global mapscroll_current_map
        mapscroll_current_map = map_name
        enter_mapscroll((items_needed, mapscroll_events), True)

    def pick_up_item(item_name, mapscroll_events, items_needed):
        if item_name in mapscroll_events and 'before_pickup' in mapscroll_events[item_name]:
            renpy.jump(mapscroll_events[item_name]['before_pickup'])
            return mapscroll_events[item_name]['before_pickup']

        mapscroll_items_picked.add(item_name)
        if item_name in mapscroll_events and 'on_pickup' in mapscroll_events[item_name]:
            renpy.jump(mapscroll_events[item_name]['on_pickup'])
            return mapscroll_events[item_name]['on_pickup']
        else:
            enter_mapscroll((items_needed, mapscroll_events), True)

    renpy.register_statement("mapscroll", block=True, execute=enter_mapscroll, parse=parse_mapscroll)


# savegame variables
default mapscroll_current_map = "kitchen"
default mapscroll_items_picked = set()


screen mapscroll_screen(mapscroll_events, items_needed):
    if 'right' in maps[mapscroll_current_map]:
        imagebutton:
            auto 'gui/button/arrow_right_%s.png'
            xalign 0.98
            yalign 0.5
            action Function(handle_map_change, maps[mapscroll_current_map]['right'], mapscroll_events, items_needed)
            at buttonzoom
    if 'left' in maps[mapscroll_current_map]:
        imagebutton:
            auto 'gui/button/arrow_left_%s.png'
            xalign 0.02
            yalign 0.5
            action Function(handle_map_change, maps[mapscroll_current_map]['left'], mapscroll_events, items_needed)
            at buttonzoom
    if 'up' in maps[mapscroll_current_map]:
        imagebutton:
            auto 'gui/button/arrow_up_%s.png'
            xalign 0.5
            yalign 0.02
            action Function(handle_map_change, maps[mapscroll_current_map]['up'], mapscroll_events, items_needed)
            at buttonzoom
    if 'down' in maps[mapscroll_current_map]:
        imagebutton:
            auto 'gui/button/arrow_down_%s.png'
            xalign 0.5
            yalign 0.95
            action Function(handle_map_change, maps[mapscroll_current_map]['down'], mapscroll_events, items_needed)
            at buttonzoom
    if 'items' in maps[mapscroll_current_map]:
        for item_name, item_info in maps[mapscroll_current_map]['items'].items():
            if item_name not in mapscroll_items_picked:
                imagebutton:
                    idle f'images/item {item_name}.png'
                    xalign item_info['x']
                    yalign item_info['y']
                    if item_name in items_needed or item_name in mapscroll_events:
                        action Function(pick_up_item, item_name, mapscroll_events, items_needed)
                    else:
                        pass  # TODO: tell john he's stupid
                    at buttonzoom(item_info['zoom'])
