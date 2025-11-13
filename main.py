tiles.set_tilemap(tilemap("""
    emptylevel
"""))


def on_a_pressed():
    if (0) == (1):
        bigTurkey.vy = -300
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite, location):
    global freeTurkeys
    info.change_score_by(1)
    tiles.set_tile_at(location, assets.tile("""
        transparency16
        """))
    freeTurkeys = sprites.create(img("""
        .
        """), SpriteKind.rescued)
    tiles.place_on_tile(freeTurkeys, location)
    freeTurkeys.follow(sprite)
    carnival.on_game_over_expanded(carnival.WinTypes.TIMED)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        cage
        """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        transparency16
        """),
    on_overlap_tile2)

freeTurkeys: Sprite = None
bigTurkey: Sprite = None
DAPCEP.splash()
scene.set_background_color(9)
bigTurkey = sprites.create(img("""
        ........................
        ..................beb...
        .................beb....
        .....bbb......bbbbbb....
        .....b2b.....bbeeeeeb...
        .bb..b2bb...bbed1feedf..
        bbbb.b22b...bee1ffed4c..
        bb4bbb22b...beedfbdd44..
        .b44bb22bb..deeeee44444b
        .bb44bb222b.beeee44444b.
        ..bb44bbb22bcbeeee22eb..
        ....bb44c4cecbeee2222...
        bbbbbbbb442ceeeeeeeeb...
        b2222222eeeeeeeeeeeeb...
        bb222b4ceeeeeeeeeeeeeb..
        .bbbb444eeeeeeeceeeeeb..
        ...bb4dceeeeeeeceeeeeb..
        ..bb44bdcdeeeeeceeeeeb..
        ..bbbbcddccbdecceeeeeb..
        ......bbbdcccdeeeeeebb..
        .......bbccccccceeebb...
        ........bbbcccccbbbb....
        ..........bbbbbbb44.....
        ........................
        """),
    SpriteKind.player)
sprite_on_screen = 1
controller.move_sprite(bigTurkey, 100, 0)
bigTurkey.ay = 500
scene.camera_follow_sprite(bigTurkey)
tiles.place_on_random_tile(bigTurkey, assets.tile("""
    start
    """))
carnival.start_timer()