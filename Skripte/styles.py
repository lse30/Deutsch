class StyleProfile:
    def __init__(self, dark_mode=False):
        self.standard_font = ('Bahnschrift', 14)
        self.flash_font = ('Bahnschrift', 25, 'bold')

        self.result_text = 'snow'

        if dark_mode:
            self.background = '#080808'
            self.on_background = '#FFFFFF'
            self.surface = '#222222'
            self.on_surface = '#FFFFFF'
            self.primary = '#61497d'
            self.secondary = '#BB86FC'
            self.on_secondary = '#000000'
            self.entry_background = '#BB86FC'
            self.success_green = '#5aac4e'
            self.failure_red = '#c93922'
        else:
            self.primary = '#02203d'
            self.secondary = '#0352a1'
            self.on_secondary = '#000000'
            self.background = '#EBEBEB'
            self.surface = '#c5d9ed'
            self.on_background = '#000000'
            self.on_surface = '#000000'
            self.entry_background = '#EBEBEB'
            self.success_green = '#079412'
            self.failure_red = '#BD0606'