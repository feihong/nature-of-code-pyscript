import re
import types
from pyscript import HTML
from pyscript.web import page, h2, p, div

# Dict containing all scenes, indexed by class name
scenes = {}

class SceneMetaClass(type):
    def __new__(cls, clsname, bases, attrs):
        if '__doc__' in attrs:
            text = attrs['__doc__'].strip()
            title, rest = text.split('\n', 1)
            attrs['title'] = title.strip()

            if m := re.search(r'\s\- ', rest):
                body = rest[:m.start()].strip()
                attrs['body'] = '\n'.join(line.strip() for line in body.splitlines())
                choices = rest[m.start():].strip()
                attrs['choices'] = [line.strip()[2:] for line in choices.splitlines()]
            else:
                attrs['body'] = rest.strip()
                attrs['choices'] = []

            attrs['update'] = attrs.get('update', lambda _state, _scene: None)
            attrs['visible'] = True
            attrs['seen_count'] = 0

        new_class = super().__new__(cls, clsname, bases, attrs)

        if '__doc__' in attrs:
            assert clsname not in scenes
            scenes[clsname] = new_class

        return new_class

class Scene(object, metaclass=SceneMetaClass):
    pass

def init(**kwargs):
    # Check that there's a Start scene
    assert 'Start' in scenes, 'You must have scene class called Start'

    # Check that all choice names are valid scenes
    for name, scene in scenes.items():
        for choice in scene.choices:
            assert choice in scenes, f'Invalid choice in scene {name}: {choice}'

    # Transform choices to list of classes
    for scene in scenes.values():
        scene.choices = [scenes[choice] for choice in scene.choices]

    state = types.SimpleNamespace(**kwargs)
    render(scenes['Start'], state)

def choice_div(scene, state, title=None):
    title = title if title else scene.title
    return div('➣ ' + title,
               style={'cursor': 'pointer'},
               on_click=lambda _evt: render(scene, state))

def render(scene, state):
    page.append(h2(scene.title))
    para = p()
    para.innerHTML = scene.body
    page.append(para)

    scene.update(state, scene)

    choices = [c for c in scene.choices if c.visible]

    if len(choices) == 1:
        page.append(choice_div(choices[0], state, title='Continue'))
    else:
        for choice_scene in choices:
            page.append(choice_div(choice_scene, state))
