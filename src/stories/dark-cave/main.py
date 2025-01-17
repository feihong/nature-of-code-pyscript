from choosy import Scene, init

class Start(Scene):
    """
    Dark Cave

    You arrive at the mouth of a dark and enigmatic cave.

    - Sleep
    - Enter
    - Why
    """

class Enter(Scene):
    """
    Enter the cave

    You take a deep breath and walk into the cave. Your eyes quickly adjust to
    the darkness and you make quick progress. After ten minutes, you find that
    the passage in front of you forks into two tunnels.

    - Left
    - Right
    """

class Sleep(Scene):
    """
    Go back home and sleep

    You trudge home and crawl back into bed. When you wake up, you realize you
    really have nothing better to do than go back to that cave.

    - Start
    """

class Why(Scene):
    """
    Why am I here?

    You can't remember why you came here. You apparently have the memory of a
    gold fish.

    - Start
    """

    def update(state, scene):
        scene.visible = False

class Left(Scene):
    """
    The left tunnel

    You go down the left tunnel. You become helplessly lost, and that's the last
    anyone ever heard of you.
    """

class Right(Scene):
    """
    The right tunnel

    You go down the right tunnel. Eventually, you stumble over a skeleton
    holding a hard drive. You pry the hard drive from the corpse's bony hands
    and once you take it home, you discover that it contains 100 million dollars
    in Bitcoin.

    Congratulations! You've struck it rich.
    """

init()
