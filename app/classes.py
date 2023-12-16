type Project = dict[str, list[str]]

def save_project_images(layer_names_of_projects: Project, zoom: float, dpi: float) -> None:
    for project in layer_names_of_projects:
        save_images_for_active_partial_areas(layer_names_of_projects[project], zoom, dpi)

def save_images_for_active_partial_areas(layer_names, zoom, dpi) -> None:
    set_visibility(layer_names)
    active_area_names = active_partial_area_names()
    for area_name in active_area_names:
            zoom_to(area_name, zoom)
            Layout(layer_names_in_area(area_name, layer_names)).create()
            save_active_area(dpi, output_path(layer_names, area_name))

def output_path(layer_names, area_name):
    pass


def layer_names_in_area(partial_area_name, layer_names):
    return give_overlap_list(partial_area_name, layer_names)

def give_overlap_list(x, y):
    pass

def set_visibility(layers):
    pass

def zoom_to(area, zoom):
    pass

def save_active_area(dpi, path):
    pass

def active_partial_area_names() -> list[str]:
    return ['r']



class Rectangle:
    def __init__(self, x: float, y: float, w: float,  h: float) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

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











##############
class ImageMaker:
    def __init__(self,  layer_names: list[str], zoom, dpi) -> None:
        self.layer_names = layer_names
        self.active_area_names = active_partial_area_names()
        self.zoom = zoom
        self.dpi =dpi

    def save_active_areas(self) -> None:
        for area_name in self.active_area_names:
            Frame(area_name, self.layer_names, self.zoom).create()
            save_active_area(self.dpi, self.output_path(area_name))

    def output_path(self, partial_area_name):
        path = str((partial_area_name, self.layer_names))
        return path
    

class Frame:
    """Frame sets visible layers, position, zoom, legend and scalebar"""
    def __init__(self, partial_area_name: str, layer_names: list[str], zoom: float) -> None:
        self.partial_area_name = partial_area_name
        self.layer_names = layer_names
        self.zoom = zoom
    
    def active_layer_names_in_frame(self):
        return give_overlap_list(self.partial_area_name, self.layer_names)

    def create(self):
        set_visibility(self.layer_names)
        zoom_to(self.partial_area_name, self.zoom)
        Layout(self.active_layer_names_in_frame()).create()

