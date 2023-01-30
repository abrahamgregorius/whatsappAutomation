1. flow masuk ke profile settings
three circle button : {com.whatsapp:id/menuitem_overflow}
text: "Settings" {com.whatsapp:id/title}
profile info : {com.whatsapp:id/profile_info}

-> profile picture : {com.whatsapp:id/change_photo_btn}
    // on progress
    - icon (camera, gallery, avatar): {com.whatsapp:id/icon}
    - click "gallery" di icon
    - click "GALLERY" di menu
    - push photo
    - click "All photos"
    - click the most recent (index="1", description="Photo")
    - click "Done"
    - return to home activity


-> nama : {com.whatsapp:id/profile_info_name_card}
    - Type status
    - Click {com.whatsapp:id/save_button}

-> bio : {com.whatsapp:id/profile_info_status_card}
    -> custom status: {com.whatsapp:id/status_layout}
        - Type status
        - Click {com.whatsapp:id/save_button}
