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
            'left': 'bedroom',
            'right': 'kitchen',
        },
        'bathroom': {
            'down': 'bathroom_door',
        },
        'bedroom': {
            'right': 'bathroom_door',
            'up': 'closet',
        },
        'closet': {
            'down': 'bedroom',
        },
    }

    def parse_mapscroll(lexer):
        return lexer.rest()

    def enter_mapscroll(current_map):
        renpy.scene()
        renpy.show(f"bg {current_map}")
        renpy.show_screen("mapscroll", current_map=current_map)
        renpy.ui.interact()

    renpy.register_statement("mapscroll", parse=parse_mapscroll, execute=enter_mapscroll)

screen mapscroll(current_map):
    imagebutton:
        auto 'gui/button/arrow_right_%s.png'
        xalign 0.98
        yalign 0.5
        action Show("previous")
        at buttonzoom

    imagebutton:
        auto 'gui/button/arrow_left_%s.png'
        xalign 0.02
        yalign 0.5
        action Show("previous")
        at buttonzoom
