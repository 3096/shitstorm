init:
    transform buttonzoom:
        zoom 0.16

$ maps = {
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
