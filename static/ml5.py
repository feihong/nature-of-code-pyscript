from pyscript import ffi
import js

version = js.ml5.version

def wrap_callback(callback, create_proxy=True):
    """
    Wrap the callback function so that it always receives two arguments
    """
    def wrapped_callback(*args):
        if len(args) == 1:
            callback(args[0], None)
        else:
            callback(args[0], args[1])

    return ffi.create_proxy(wrapped_callback) if create_proxy else wrapped_callback

class imageClassifier:
    def __init__(self, modelName, **options):
        self._classifier = js.ml5.imageClassifier(modelName, ffi.to_js(options))

    def classifyStart(self, media, callback, kNumber=None):
        self._classifier.classifyStart(media, kNumber, wrap_callback(callback))

    def classifyStop(self):
        self._classifier.classifyStop()

    def classify(self, media, callback=None, kNumber=None):
        wrapped_callback = wrap_callback(callback) if callback else None
        return self._classifier(media, kNumber, wrapped_callback)

class faceMesh:
    def __init__(self, **options):
        self._mesh = js.ml5.faceMesh(ffi.to_js(options))

    def detectStart(self, media, callback):
        self._mesh.detectStart(media, wrap_callback(callback))

    def detectStop(self):
        self._mesh.detectStop()

    def detect(self, media, callback):
        self._mesh.detect(media, callback)

    def getTriangles(self):
        return self._mesh.getTriangles()
