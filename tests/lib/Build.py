from utils import cont_cmd

class Build:
    
    def build_containers(self):
        """Build the SDK containers."""
        cont_cmd('./../builder/build_container')
