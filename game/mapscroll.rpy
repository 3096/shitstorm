init:
    transform buttonzoom:
        zoom 0.16

python early:
    maps = {
        'kitchen': {
            'left': 'bathroom_door',
            'right': 'garden',

            'items': {
                'hydrogenperoxide': {
                    'x': 0.5,
                    'y': 0.5,
                    'width': 0.1,
                    'height': 0.1,
                },
                'gloves': {
                    'x': 0.1,
                    'y': 0.5,
                    'width': 0.1,
                    'height': 0.1,
                },
                'bleach': {
                    'x': 0.5,
                    'y': 0.1,
                    'width': 0.1,
                    'height': 0.1,
                },
            }
        },
        'garden': {
            'left': 'kitchen',
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
        print("????????")
        return (lexer.word(), lexer.rest().split(' '))

    def enter_mapscroll(params, is_next=False):
        print(params)
        current_map, items_needed = params
        renpy.scene()
        renpy.transition(dissolve)
        renpy.show(f"bg {current_map}")
        if is_next:
            renpy.show_screen("mapscroll_screen", current_map=current_map, items_needed=items_needed)
        else:
            renpy.show_screen("mapscroll_screen", current_map=current_map, items_needed={item: True for item in items_needed})
            renpy.ui.interact()

    def pick_up_item(current_map, item_name, items_needed):
        items_needed[item_name] = False
        if not any(items_needed.values()):
            renpy.hide_screen("mapscroll_screen")
            renpy.ui.returns()
            pass
        else:
            enter_mapscroll((current_map, items_needed), True)

    renpy.register_statement("mapscroll", execute=enter_mapscroll, parse=parse_mapscroll)

screen mapscroll_screen(current_map, items_needed):
    if 'right' in maps[current_map]:
        imagebutton:
            auto 'gui/button/arrow_right_%s.png'
            xalign 0.98
            yalign 0.5
            action Function(enter_mapscroll, (maps[current_map]['right'], items_needed), True)
            at buttonzoom
    if 'left' in maps[current_map]:
        imagebutton:
            auto 'gui/button/arrow_left_%s.png'
            xalign 0.02
            yalign 0.5
            action Function(enter_mapscroll, (maps[current_map]['left'], items_needed), True)
            at buttonzoom
    if 'up' in maps[current_map]:
        imagebutton:
            auto 'gui/button/arrow_up_%s.png'
            xalign 0.5
            yalign 0.02
            action Function(enter_mapscroll, (maps[current_map]['up'], items_needed), True)
            at buttonzoom
    if 'down' in maps[current_map]:
        imagebutton:
            auto 'gui/button/arrow_down_%s.png'
            xalign 0.5
            yalign 0.95
            action Function(enter_mapscroll, (maps[current_map]['down'], items_needed), True)
            at buttonzoom
    if 'items' in maps[current_map]:
        for item_name, item_info in maps[current_map]['items'].items():
            if items_needed[item_name]:
                imagebutton:
                    idle f'images/item {item_name}.png'
                    xalign item_info['x']
                    yalign item_info['y']
                    if item_name in items_needed:
                        action Function(pick_up_item, current_map, item_name, items_needed)
                    else:
                        pass  # TODO: tell john he's stupid
                    at buttonzoom
