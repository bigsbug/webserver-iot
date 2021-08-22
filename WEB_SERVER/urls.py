from django.urls import path

from .views import (
    index,
    Get_Device,
    New_Command,
    Get_Command,
    New_Button,
    Get_Buttons,
    Get_Data,
    CUD_Device,
)

urlpatterns = [
    path("", index),

    # Device urls
    path("get_devices/", Get_Device.as_view(), name="DEVICE"),
    path("cud_device/", CUD_Device.as_view(), name="CUD_DEVICE"),

    # Data urls
    path("data/", Get_Data.as_view(), name="GET_DATA"),

    # Commands urls
    path("new_command/", New_Command.as_view(), name="SET_Command"),
    path("get_command/", Get_Command.as_view(), name="SET_Command"),

    # Buttons urls
    path("new_button/", New_Button.as_view(), name="New_BUTTON"),
    path("get_buttons/", Get_Buttons.as_view(), name="Get_BUTTONS"),
]