## Import all the libraries
import pyglet as pg

## UI Class.
class Interface:
    def add_screen(self, screen, batch):
        id                  = len(self.surfaces)+1
        self.making_surface = 1
        self.surfaces[id]   = {
            "screen": screen,
            "batch":  batch
        }
        return id

    def __init__(self, screen, batch):
        self.screen          = screen
        self.batch           = batch
        self.surfaces        = {}
        self.making_surface  = 0
        self.main_surf_id    = self.add_screen(screen, batch)
        self.is_doublebuffer = 1
        self.area_cache      = {}
        self.draw_queue      = {}
        self.anchors         = {}
        self.base_label      = pg.text.Label(
            text  = "",
            x     = 0,
            y     = 0,
            z     = 0,
            batch = self.batch
        )
        self.labels          = {}
        self.used_labels     = {}
        self.label_queue     = {}
        self.layers          = {}

        for i in range(-16,16):
            self.layers[i] = pg.graphics.Group(order=i)
    
    def get_anchor(self,pos,win_w,win_h,anchor,surf_w,surf_h,can_cache):
        anchor_id   = f"{anchor},win{win_w}x{win_h},surf{surf_w}x{surf_h},pos{pos}"

        new_pos = pos.copy()
        if can_cache:
            if not anchor_id in self.anchors:
                new_pos[1] = (win_h - surf_h) - pos[1] # This is a pygame household btw
                if "right" in anchor:
                    new_pos[0] = (win_w - surf_w) - pos[0]
                if "bottom" in anchor:
                    new_pos[1] = pos[1]
                if "centerX" in anchor:
                    new_pos[0] = (win_w/2 - surf_w/2) + pos[0]
                if "centerY" in anchor:
                    new_pos[1] = (win_h/2 - surf_h/2) + pos[1]
                if "center" in anchor:
                    new_pos[0] = (win_w/2 - surf_w/2) + pos[0]
                    new_pos[1] = (win_h/2 - surf_h/2) + pos[1]
                self.anchors[anchor_id]=new_pos
            else:
                new_pos = self.anchors[anchor_id]
        return new_pos

    def blit(self, surface, pos, clip=0, anchor="", opacity = 1, layer = 0, scroll=[0,0], scale=[1,1], blit_in="main", can_cache = 1, rot = 0):
        # the origin for the position is topleft. surface is a sprite.
        new_pos     = pos[:]
        path        = surface.get_path()
        img         = surface.get()
        new_opacity = int(opacity * 255)
        img.scale_x, img.scale_y = scale

        if clip:
            ## Clipping
            cx, cy, cw, ch = clip
            cy = surface.height - cy - ch

            if can_cache:
                id = f"{path}{cx}{cy}{cw}{ch}"
                if not id in self.area_cache:
                    img = img.get_region(cx, cy, cw, ch)
                    self.area_cache[id] = img
                else:
                    img = self.area_cache[id]
        
        ## Anchoring
        if blit_in  == "main":
            blit_in =  self.main_surf_id
        anchor = anchor.split(" ")
        
        screen = self.surfaces[blit_in]["screen"]
        batch  = self.surfaces[blit_in]["batch"]
        
        win_w, win_h = screen.get_size()
        new_pos      = self.get_anchor(pos,win_w,win_h,anchor,img.width,img.height,1)
        
        ## Detect if i'm even visible and change position
        id  = len(self.draw_queue)
        if scroll != [0, 0]:
            img = img.get_region(
                scroll[0] % img.width, 
                scroll[1] % img.height,
                img.width,             
                img.height             
            )
        
        if new_pos[0] > win_w or new_pos[1] > win_h or new_pos[0] < -img.width or new_pos[1] < -img.height:
            pass
        else:
            if layer > 15:
                layer = 15
            self.draw_queue[id] = pg.sprite.Sprite(img, x=new_pos[0], y=new_pos[1], z=layer, batch=batch, group=self.layers[layer])
            self.draw_queue[id].scale_x, self.draw_queue[id].scale_y = scale
            if rot:
                self.draw_queue[id].rotation =  rot            
                self.draw_queue[id].x        += img.width      
                self.draw_queue[id].y        += img.height     
                self.draw_queue[id].anchor_x =  img.width  // 2
                self.draw_queue[id].anchor_y =  img.height // 2
            if new_opacity > 0:
                self.draw_queue[id].opacity  = new_opacity
            else:
                self.draw_queue[id].opacity  = 0
    
    def render(self, text, pos, blit_in="main", layer=5, anchor=""):
        if blit_in == "main":
            blit_in =  self.main_surf_id
        id                   = len(self.label_queue)
        self.label_queue[id] = [text, pos, blit_in, layer, anchor]
    
    def flip(self):
        ## === 1. Process label queue ===
        for key, lab_dat in self.label_queue.items():  # Proper iteration over dict
            text    = lab_dat[0]
            pos     = lab_dat[1]
            blit_in = lab_dat[2]
            layer   = lab_dat[3]
            anchor  = lab_dat[4]
            screen  = self.surfaces[blit_in]["screen"]
            batch   = self.surfaces[blit_in]["batch"]

            # Reuse an unused label or create a new one
            label_id = -1
            for i, label in enumerate(self.labels):
                if i not in self.used_labels:
                    label_id = i
                    self.used_labels[i] = i
                    break

            if label_id == -1:
                label_id = len(self.labels)
                # Create a new label based on self.base_label
                base = self.base_label
                new_label = pg.text.Label(
                    text,
                    font_name=base.font_name,
                    font_size=25,
                    z=layer,
                    color=base.color,
                    batch=batch,
                    anchor_x=base.anchor_x,
                    anchor_y=base.anchor_y,
                    group=self.layers[layer]
                )
                new_pos                  = self.get_anchor(pos, screen.get_size()[0], screen.get_size()[1], anchor.split(" "), new_label.content_width, new_label.content_height, 1)
                new_label.x, new_label.y = new_pos
                self.labels[len(self.labels)] = new_label
            else:
                # Reuse existing label
                label_obj                = self.labels[label_id]
                new_pos                  = self.get_anchor(pos, screen.get_size()[0], screen.get_size()[1], anchor.split(" "), label_obj.content_width, label_obj.content_height, 1)
                label_obj.x, label_obj.y = new_pos
                label_obj.text           = text
                label_obj.z              = layer
                label_obj.group          = self.layers[layer]

        # Clear queues for next frame
        self.label_queue.clear()
        self.used_labels.clear()

        ## === 2. Draw batches ===
        if not self.making_surface:
            for surf in self.surfaces.values():
                surf["batch"].draw()
            self.draw_queue.clear()

        self.making_surface = 0

        ## === 3. Flip/update window ===
        for i in self.surfaces:
            screen = self.surfaces[i]["screen"]
            if self.is_doublebuffer:
                self.screen.flip()
            else:
                self.screen.update()
        for i in self.labels:
            label_obj                = self.labels[i]
            label_obj.x, label_obj.y = -500,-500
    
    def fill(self, color="black"):
        for i in self.surfaces:
            screen = self.surfaces[i]["screen"]
            screen.clear()
    
    def close(self):
        for i in self.surfaces:
            screen = self.surfaces[i]["screen"]
            screen.close()
        self.surfaces = {}