class Layers:
    visible = None  # uninitialized state

    @classmethod    
    def set_visible(cls, layers) -> None:
        if cls.visible is not None: 
            cls.hide_all()

        if layers != cls.visible:
            cls.visible = layers.copy()
            print('change active layers')

    @classmethod
    def hide_all(cls) -> None:
        if cls.visible:
            cls.visible = []
            print('hide layers')


class Layers1:
    visible = []

    @classmethod    
    def set_visible(cls, layers):
        if cls.visible != layers:
            cls.hide_all()
            cls.add_to_visible(layers)

    @classmethod
    def hide_all(cls):
        cls.visible = []
        pass
    
    @classmethod
    def add_to_visible(cls, layers):
        print('changed')
        cls.visible.extend(layers)
        pass

class Layers2:
    def __init__(self) -> None:
        self.hide_all()

    def set_visible(self, layers: list[str]):
        if self.visible != layers:
            self.hide_all()
            self.add_to_visible(layers)

    def hide_all(self):
        self.visible = []
        pass
    
    def add_to_visible(self, layers):
        print('changed')
        self.visible.extend(layers)
        pass


class Layers4:
    active = []
    visible = []

    def set_visible(self, layers: list[str]):
        if self.visible != layers:
            self.hide_all()
            self.add_to_visible(layers)


    def hide_all(self):
        self.visible = []
        self.active = []
        pass
    
    def add_to_visible(self, layers):
        print('changed')
        self.visible.extend(layers)
        pass
