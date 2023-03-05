from pydantic import BaseModel


class Agent(BaseModel):
    os = "Android"
    device_platform = "android"
    os_version = ""
    os_api = ""
    device_model = ""
    device_brand = ""
    device_manufacturer = ""
    process_name = ""
    sid = ""
    rom_version = ""
    apm_version = ""
