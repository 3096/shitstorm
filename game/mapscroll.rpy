init:
    transform buttonzoom:
        zoom 0.16

python early:
    maps = {
        'kitchen': {
            'left': 'bathroom_door',
            'right': 'garden',
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
        return lexer.rest()

    def enter_mapscroll(current_map, is_next=False):
        renpy.scene()
        renpy.transition(dissolve)
        renpy.show(f"bg {current_map}")
        renpy.show_screen("mapscroll_screen", current_map=current_map)
        if not is_next:
            renpy.ui.interact()

    renpy.register_statement("mapscroll", parse=parse_mapscroll, execute=enter_mapscroll)

screen mapscroll_screen(current_map):
    if 'right' in maps[current_map]:
        imagebutton:
            auto 'gui/button/arrow_right_%s.png'
            xalign 0.98
            yalign 0.5
            action Function(enter_mapscroll, maps[current_map]['right'], True)
            at buttonzoom
    if 'left' in maps[current_map]:
        imagebutton:
            auto 'gui/button/arrow_left_%s.png'
            xalign 0.02
            yalign 0.5
            action Function(enter_mapscroll, maps[current_map]['left'], True)
            at buttonzoom
    if 'up' in maps[current_map]:
        imagebutton:
            auto 'gui/button/arrow_up_%s.png'
            xalign 0.5
            yalign 0.02
            action Function(enter_mapscroll, maps[current_map]['up'], True)
            at buttonzoom
    if 'down' in maps[current_map]:
        imagebutton:
            auto 'gui/button/arrow_down_%s.png'
            xalign 0.5
            yalign 0.98
            action Function(enter_mapscroll, maps[current_map]['down'], True)
            at buttonzoom
