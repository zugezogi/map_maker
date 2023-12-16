from layout import Layout



type ProjectLayers = dict[str, list[str]]



class Project:
    def __init__(self, project_layers: ProjectLayers) -> None:
        self.project_layers = project_layers
        active_area_names = self.active_partial_area_names()

    def save_images(self, zoom=0.3, dpi=300):
        for key in self.project_layers:
            for area_name in self.active_partial_area_names():
                Frame(area_name, self.project_layers[key], zoom).create()
                self.save_active_area(dpi)

    def active_partial_area_names(self) -> list[str]:
        return ['r']
    
    def save_active_area(self, dpi):
        pass

class Layers:
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

class Frame:
    """Frame sets visible layers, position, zoom, legend and scalebar"""
    def __init__(self, partial_area_name: str, layer_names: list[str], zoom: float) -> None:
        self.partial_area_name = partial_area_name
        self.layer_names = layer_names
        self.zoom = zoom
    
    def create(self):
        Layers().set_visible(self.layer_names)
        self.zoom_to()
        Layout(self.active_layer_names_in_frame()).create()

    def zoom_to(self):
        pass 

    def active_layer_names_in_frame(self):
        return give_overlap_list(self.partial_area_name, self.layer_names)






############## OLD
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
    




class Layers3:
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

class Layers2:
    active = []
    def __init__(self) -> None:
        self.hide_all()

    def set_visible(self, layers: list[str]):
        if self.visible != layers:
            self.hide_all()
            self.add_to_visible(layers)
      
    def set_active(self, layers):
        if cls.active != layers:
            self.hide_all()
            self.add_to_visible(layers)
        cls.active.extend(layers)

    @classmethod        
    def activate(cls, layers):
        cls.active.extend(layers)

    def hide_all(self):
        self.visible = []
        pass
    
    def add_to_visible(self, layers):
        print('changed')
        self.visible.extend(layers)
        pass



def save_project_images(layer_names_of_projects: ProjectLayers, zoom: float, dpi: float) -> None:
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
