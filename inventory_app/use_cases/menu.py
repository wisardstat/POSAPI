from sqlalchemy.orm import Session, aliased
from sqlalchemy import or_, and_, func 
from ..entity import menu as et_menu , sub_menu as et_submenu , group_user_menu


def get_menus_by_group_user_id(db: Session, group_user_id: str):

   print('group_user_id=>',group_user_id)
   
   group_user_menus = db.query(group_user_menu.GroupUserMenu).filter(group_user_menu.GroupUserMenu.group_user_id == group_user_id).all()
   
   print('group_user_menus=>',group_user_menus)      

   main_menu_ids = set(gum.menu_id for gum in group_user_menus if gum.sub_menu_id is None)

   main_menus = db.query(et_menu.Menu).filter(et_menu.Menu.id.in_(main_menu_ids)).all()
   
   print('main_menus=>',main_menus)    

   menu_data = []
   for menu in main_menus:
 
      accessible_sub_menu_ids = [gum.sub_menu_id for gum in group_user_menus if gum.sub_menu_id is not None and gum.menu_id == menu.id]

      if accessible_sub_menu_ids:
        sub_menus = db.query(et_submenu.SubMenu).filter(
            et_submenu.SubMenu.parent_id == menu.id,
            et_submenu.SubMenu.id.in_(accessible_sub_menu_ids)
        ).all()
      else: 
         sub_menus = db.query(et_submenu.SubMenu).filter(
            et_submenu.SubMenu.parent_id == menu.id
         ).all()
            
      print('menu.menu_name=>',menu.menu_name)    

      menu_dict = {
            "title": menu.menu_name,
            "icon": sub_menus[0].icon,
            "type": "sub",
            "active": False,
            "children": [],
      }

      for sub_menu in sub_menus:
            menu_dict["children"].append({
               "title": sub_menu.title,
               "icon": sub_menu.icon,
               "type": sub_menu.type,
               "path": sub_menu.path,
               "bookmark": sub_menu.bookmark
            })

      menu_data.append(menu_dict)

        
   return menu_data