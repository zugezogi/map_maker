class Layout():
    def __init__(self, active_layers_in_frame) -> None:
        self.active_layers_in_frame = active_layers_in_frame
        self.layout_name = 'Export'
        self.rectangle = Rectangle(310, 5, 0, 0)

    def create(self):
        self.remove_all_layouts()
        self.set_layout_type()
        self.add_scale_bar
        self.add_legend()

    def add_map(self):
        self.map = 7
        pass
    
    def add_legend(self):
        x = self.active_layers_in_frame
        pass

    def add_scale_bar(self):
        x = self.map
        y = self.layout_name
        pass

    def set_layout_type(self):
        pass
    
    def remove_all_layouts(self):
        pass


class Rectangle:
    def __init__(self, x: float, y: float, w: float,  h: float) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

